#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if [[ ! -f "${SCRIPT_DIR}/lab.env" ]]; then
  cp "${SCRIPT_DIR}/lab.env.example" "${SCRIPT_DIR}/lab.env"
  printf 'Đã tạo %s/lab.env. Hãy sửa ZITI_ADVERTISED_ADDRESS rồi chạy lại.\n' "${SCRIPT_DIR}"
  exit 2
fi

bash "${SCRIPT_DIR}/scripts/01-bootstrap.sh"
bash "${SCRIPT_DIR}/scripts/02-configure-demo.sh"
bash "${SCRIPT_DIR}/scripts/03-verify-server.sh"

cat <<'TXT'

SERVER DEMO READY

Việc còn lại trên Windows client:
1. Enroll .runtime/enrollments/alice-lab.jwt vào Ziti Desktop Edge.
2. Chỉ bật Alice và mở http://portal.ziti.internal/ (phải thành công).
3. Tắt Alice, enroll/bật Bob và mở cùng URL (phải bị từ chối).
4. Dùng scripts/04-policy-toggle.sh revoke|restore để demo thu hồi quyền.

Không commit các JWT/identity/private key. Chưa đánh dấu PASS trước khi chạy client tests.
TXT

