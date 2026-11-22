#!/usr/bin/env bash
set -Eeuo pipefail
source "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/common.sh"
load_lab_config

stamp="$(date -u +'%Y%m%dT%H%M%SZ')"
out="${REPO_DIR}/evidence/raw/${stamp}"
mkdir -p "${out}"

compose ps > "${out}/compose-ps.txt"
compose logs --tail=200 2>&1 \
  | sed -E 's/(token|password|secret|jwt)[=:][^[:space:]]+/\1=[REDACTED]/Ig' \
  > "${out}/openziti-logs-redacted.txt"
docker logs --tail=100 zt-demo-web > "${out}/nginx-logs.txt" 2>&1
docker inspect zt-demo-web --format '{{json .HostConfig.PortBindings}}' > "${out}/backend-port-bindings.json"
docker port zt-demo-web > "${out}/backend-docker-port.txt"
ziti list identities > "${out}/identities.txt"
ziti list services > "${out}/services.txt"
ziti list service-policies > "${out}/service-policies.txt"
ziti policy-advisor services portal-zt > "${out}/policy-advisor.txt"

cat > "${out}/README.txt" <<TXT
Thu thập UTC: ${stamp}
Chưa bao gồm ảnh client, kết quả Alice/Bob, Test-NetConnection hoặc packet capture.
Kiểm tra thủ công file log trước khi chia sẻ; bộ lọc tự động không đảm bảo loại bỏ mọi bí mật.
TXT
info "Đã thu thập bằng chứng tại ${out}"

