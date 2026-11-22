#!/usr/bin/env bash
set -Eeuo pipefail
source "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/common.sh"

need docker
need curl
load_lab_config
docker compose version >/dev/null
docker info >/dev/null 2>&1 || die "Docker daemon chưa chạy hoặc user chưa có quyền truy cập."

if ss -lnt 2>/dev/null | grep -Eq ":(${ZITI_CTRL_PORT}|${ZITI_ROUTER_PORT})[[:space:]]"; then
  die "Port ${ZITI_CTRL_PORT} hoặc ${ZITI_ROUTER_PORT} đang được sử dụng."
fi

if [[ -z "${ZITI_PWD:-}" ]]; then
  read -r -s -p "OpenZiti admin password cho lab: " ZITI_PWD
  printf '\n'
fi
[[ ${#ZITI_PWD} -ge 16 ]] || die "Password lab phải có ít nhất 16 ký tự."
[[ "${ZITI_PWD}" =~ ^[A-Za-z0-9_@%+=:,.-]+$ ]] \
  || die "Password chỉ dùng chữ, số và các ký tự _@%+=:,.- để ghi an toàn vào Compose .env."

mkdir -p "${RUNTIME_DIR}/enrollments"
chmod 700 "${RUNTIME_DIR}" "${RUNTIME_DIR}/enrollments"

if [[ ! -f "${COMPOSE_FILE}" ]]; then
  info "Tải Docker Compose all-in-one chính thức"
  curl --fail --location --proto '=https' --tlsv1.2 \
    https://get.openziti.io/dock/all-in-one/compose.yml \
    --output "${COMPOSE_FILE}"
fi

cat > "${LAB_DIR}/.env" <<ENV
ZITI_CTRL_ADVERTISED_ADDRESS=${ZITI_ADVERTISED_ADDRESS}
ZITI_ROUTER_ADVERTISED_ADDRESS=${ZITI_ADVERTISED_ADDRESS}
ZITI_CTRL_ADVERTISED_PORT=${ZITI_CTRL_PORT}
ZITI_ROUTER_PORT=${ZITI_ROUTER_PORT}
ZITI_INTERFACE=0.0.0.0
ZITI_PWD=${ZITI_PWD}
ENV
chmod 600 "${LAB_DIR}/.env"

info "Kiểm tra cấu hình Compose đã render"
compose config --quiet
info "Kéo image và khởi động OpenZiti"
compose pull
compose up -d
compose ps

info "Chờ controller sẵn sàng"
ready=0
for _ in $(seq 1 60); do
  if ziti list identities >/dev/null 2>&1; then ready=1; break; fi
  sleep 2
done
[[ "${ready}" == 1 ]] || { compose logs --tail=120; die "Controller chưa sẵn sàng sau 120 giây."; }

info "Bootstrap xong. ZAC: https://${ZITI_ADVERTISED_ADDRESS}:${ZITI_CTRL_PORT}/zac/"

