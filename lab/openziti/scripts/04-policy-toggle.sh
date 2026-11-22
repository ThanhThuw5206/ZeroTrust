#!/usr/bin/env bash
set -Eeuo pipefail
source "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/common.sh"
load_lab_config

action="${1:-}"
case "${action}" in
  revoke)
    if entity_exists service-policies portal-dial; then
      ziti delete service-policy portal-dial
      info "Đã thu hồi portal-dial. Hãy tạo request mới từ Alice."
    else
      info "portal-dial đã không tồn tại."
    fi
    ;;
  restore)
    if entity_exists service-policies portal-dial; then
      info "portal-dial đã tồn tại."
    else
      ziti create service-policy portal-dial Dial --service-roles '@portal-zt' --identity-roles '#demo-allowed'
      info "Đã khôi phục portal-dial."
    fi
    ;;
  *) die "Cách dùng: $0 revoke|restore" ;;
esac
ziti policy-advisor services portal-zt

