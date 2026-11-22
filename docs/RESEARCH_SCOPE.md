# Phạm vi nghiên cứu và sản phẩm bàn giao

Tài liệu chính: `docs/Zero_Trust_OpenZiti_Project_Plan_and_Demo.md`.

| Yêu cầu | Nội dung cần trình bày | Vị trí trong tài liệu |
|---|---|---|
| Định nghĩa | Không có tin cậy ngầm; xác thực và phân quyền theo từng tài nguyên | 7.2–7.3 |
| Kiến trúc | NIST SP 800-207; PE, PA, PEP; control plane/data plane; nguồn tín hiệu | 7.4–7.6 |
| Giải pháp hãng | Microsoft, Zscaler, Cloudflare, Palo Alto, Cisco, Fortinet và OpenZiti | 8.1–8.2 |
| Thị trường | Động lực, rào cản, phạm vi số liệu và tránh trộn ZTA/ZTNA/SASE | 8.3 |
| Ưu/nhược điểm | Giảm bề mặt tấn công/lateral movement; đổi lại tăng độ phức tạp, chi phí và phụ thuộc telemetry | 8.4–8.5 |
| Triển khai mã nguồn mở | OpenZiti controller/router/tunneler, Nginx private, Alice allow, Bob deny, revoke | 9–11 và repo `lab/` |

## Luận điểm demo phải chứng minh

1. Backend không được publish TCP/80 ra host/LAN.
2. Hai người dùng cùng mạng nhưng kết quả khác nhau vì identity/policy.
3. Alice có `Dial`; Bob có identity hợp lệ nhưng không có `Dial`.
4. Thu hồi policy làm request mới của Alice bị từ chối; khôi phục policy cho phép lại.
5. Log, policy advisor, client status và kiểm tra port được lưu làm bằng chứng.

Demo chỉ chứng minh identity-based connectivity của OpenZiti. Không tuyên bố nó tự động chứng minh MFA, endpoint posture, DLP, SIEM hoặc toàn bộ chương trình Zero Trust cấp doanh nghiệp.

