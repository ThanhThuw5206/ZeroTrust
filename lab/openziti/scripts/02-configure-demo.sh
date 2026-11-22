#!/usr/bin/env bash
set -Eeuo pipefail
source "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/common.sh"

need docker
load_lab_config
[[ -f "${COMPOSE_FILE}" && -f "${LAB_DIR}/.env" ]] || die "Hãy chạy 01-bootstrap.sh trước."
mkdir -p "${RUNTIME_DIR}/enrollments"
chmod 700 "${RUNTIME_DIR}/enrollments"

info "Xác định Docker network của quickstart"
container_id="$(compose ps -q "${ZITI_COMPOSE_SERVICE}")"
[[ -n "${container_id}" ]] || die "Không tìm thấy container ${ZITI_COMPOSE_SERVICE}."
network_name="$(docker inspect "${container_id}" --format '{{range $name, $_ := .NetworkSettings.Networks}}{{$name}}{{"\n"}}{{end}}' | head -n1)"
[[ -n "${network_name}" ]] || die "Không xác định được Docker network."

if ! docker container inspect zt-demo-web >/dev/null 2>&1; then
  info "Khởi động Nginx private, không publish host port"
  docker run -d --name zt-demo-web --network "${network_name}" --restart unless-stopped nginx:alpine >/dev/null
fi
[[ -z "$(docker port zt-demo-web)" ]] || die "zt-demo-web đang publish port; dừng để tránh làm sai mô hình."
docker run --rm --network "${network_name}" curlimages/curl:latest --fail --silent --show-error \
  --head http://zt-demo-web:80/ >/dev/null

create_identity() {
  local name="$1" role="$2" jwt_host="${RUNTIME_DIR}/enrollments/${name}.jwt"
  if entity_exists identities "${name}"; then
    info "Identity ${name} đã tồn tại; không sinh lại enrollment token."
    return
  fi
  info "Tạo identity ${name}"
  ziti create identity user "${name}" --role-attributes "${role}" --jwt-output-file "/tmp/${name}.jwt"
  docker cp "${container_id}:/tmp/${name}.jwt" "${jwt_host}"
  chmod 600 "${jwt_host}"
  compose exec -T "${ZITI_COMPOSE_SERVICE}" rm -f "/tmp/${name}.jwt"
}

create_identity alice-lab demo-allowed
create_identity bob-lab demo-denied

if ! entity_exists configs portal-host; then
  ziti create config portal-host host.v1 '{"protocol":"tcp","address":"zt-demo-web","port":80}'
fi
if ! entity_exists configs portal-intercept; then
  ziti create config portal-intercept intercept.v1 \
    '{"protocols":["tcp"],"addresses":["portal.ziti.internal"],"portRanges":[{"low":80,"high":80}]}'
fi
if ! entity_exists services portal-zt; then
  ziti create service portal-zt --configs portal-intercept,portal-host
fi

if ! entity_exists service-policies portal-dial; then
  ziti create service-policy portal-dial Dial --service-roles '@portal-zt' --identity-roles '#demo-allowed'
fi

info "Gắn role demo-host cho router tunneler"
if ! ziti update edge-router "${ZITI_ROUTER_NAME}" --role-attributes demo-host; then
  die "Không cập nhật được router ${ZITI_ROUTER_NAME}. Kiểm tra tên/router tunneler capability trước khi tiếp tục."
fi
if ! entity_exists service-policies portal-bind; then
  ziti create service-policy portal-bind Bind --service-roles '@portal-zt' --identity-roles '#demo-host'
fi

info "Policy advisor"
ziti policy-advisor services portal-zt
info "JWT one-time nằm trong ${RUNTIME_DIR}/enrollments (không commit)."

