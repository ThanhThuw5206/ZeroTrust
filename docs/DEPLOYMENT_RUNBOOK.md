# Runbook triển khai demo OpenZiti

## 1. Phạm vi

Runbook này triển khai đúng phần thực nghiệm: identity-based service access, private backend, allow/deny và revoke. Nó không tuyên bố demo bao phủ MFA, device posture, DLP, SIEM hoặc toàn bộ Zero Trust Architecture.

## 2. Chuẩn bị VM

- Ubuntu 22.04/24.04 hoặc Kali cập nhật; 2 vCPU, tối thiểu 4 GB RAM, 20 GB trống.
- Docker Engine và Docker Compose plugin từ tài liệu Docker chính thức.
- VM dùng bridged hoặc NAT có port/reachability phù hợp. Windows phải tới được TCP 1280 và 3022 trên địa chỉ quảng bá.
- Không mở các cổng lab ra Internet.

Kiểm tra:

```bash
docker --version
docker compose version
docker info
ip -4 addr
ss -lntp | grep -E ':(1280|3022)\b' || true
```

## 3. Control plane và private app

Sửa `lab/openziti/lab.env`, sau đó chạy lần lượt:

```bash
bash lab/openziti/scripts/01-bootstrap.sh
bash lab/openziti/scripts/02-configure-demo.sh
bash lab/openziti/scripts/03-verify-server.sh
```

Repo đã giữ một bản `compose.yml` lấy từ endpoint chính thức `get.openziti.io/dock/all-in-one/compose.yml` ngày 22/11/2026. Nếu file bị thiếu, `01-bootstrap.sh` sẽ tải lại. Phải ghi image digest/version sau khi pull vì tag image mặc định của upstream là `latest`.

## 4. Client Alice và Bob

1. Cài Ziti Desktop Edge từ release chính thức.
2. Chép riêng `.runtime/enrollments/alice-lab.jwt`, enroll Alice và xóa JWT sau khi dùng.
3. Chỉ bật Alice, mở `http://portal.ziti.internal/`, lưu ảnh HTTP thành công và client status.
4. Tắt Alice hoàn toàn.
5. Enroll và chỉ bật Bob, mở cùng URL. Lỗi DNS/timeout/service unavailable là hợp lệ ở lớp overlay; không bắt buộc có HTTP 403.
6. Chỉ đánh dấu Bob PASS nếu Alice đã PASS trên cùng hệ thống và policy advisor chứng minh khác biệt quyền.

Không thêm hosts entry cho `portal.ziti.internal`, vì làm vậy sẽ bỏ qua DNS interception cần chứng minh.

## 5. Revoke

```bash
bash lab/openziti/scripts/04-policy-toggle.sh revoke
# Từ Alice, đóng kết nối/cache cũ và tạo request mới
bash lab/openziti/scripts/04-policy-toggle.sh restore
```

Ghi rõ phiên bản OpenZiti. Các bản mới có thể đóng circuit hiện hữu khi mất Dial; vẫn kiểm tra cả request mới và không suy diễn nếu chưa quan sát.

## 6. Bằng chứng

```bash
bash lab/openziti/scripts/05-collect-evidence.sh
```

Bổ sung thủ công:

- ảnh ZAC, Alice allow, Bob deny, revoke;
- `Test-NetConnection <VM_IP> -Port 80` từ Windows;
- phiên bản Docker/OpenZiti và image digest;
- packet capture lọc TCP 3022/1280 nếu thực hiện;
- thời điểm, topology và kết quả quan sát thực tế.

Review/redact mọi log trước khi nộp. Không đưa JWT, identity JSON, password, private key hoặc certificate private material vào repo/báo cáo.

## 7. Dừng lab

Giữ dữ liệu:

```bash
docker rm -f zt-demo-web
docker compose --project-directory lab/openziti --env-file lab/openziti/.env -f lab/openziti/compose.yml down
```

Không dùng `down -v` hoặc `docker volume prune` trừ khi chủ động muốn hủy dữ liệu lab.

