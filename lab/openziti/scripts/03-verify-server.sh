#!/usr/bin/env bash
set -Eeuo pipefail
source "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/common.sh"

need docker
load_lab_config

info "Trạng thái OpenZiti"
compose ps
info "Backend health trong Docker network"
container_id="$(compose ps -q "${ZITI_COMPOSE_SERVICE}")"
network_name="$(docker inspect "${container_id}" --format '{{range $name, $_ := .NetworkSettings.Networks}}{{$name}}{{"\n"}}{{end}}' | head -n1)"
docker run --rm --network "${network_name}" curlimages/curl:latest --fail --silent --show-error --head http://zt-demo-web:80/

info "Xác minh backend không publish port"
published="$(docker port zt-demo-web)"
[[ -z "${published}" ]] || die "FAIL: backend đang publish port: ${published}"
bindings="$(docker inspect zt-demo-web --format '{{json .HostConfig.PortBindings}}')"
printf 'PortBindings=%s\n' "${bindings}"

info "Policy advisor"
advisor="$(ziti policy-advisor services portal-zt)"
printf '%s\n' "${advisor}"
grep -Fq 'alice-lab' <<<"${advisor}" || die "Không thấy Alice trong policy advisor."
grep -Fq 'bob-lab' <<<"${advisor}" || info "Bob có thể không hiện vì không có Dial; đối chiếu list identities/service policies."

info "Kiểm tra listener host (TCP/80 và 8080 phải không có listener do lab tạo)"
if command -v ss >/dev/null 2>&1; then ss -lntp | grep -E ':(80|8080)\b' || true; fi
info "Server-side checks hoàn tất; allow/deny vẫn cần kiểm thử từ client."

