# Ma trận nghiệm thu

Không đổi `NOT RUN` thành `PASS` nếu chưa chạy và lưu bằng chứng thực tế.

| ID | Bài kiểm thử | Kỳ vọng | Trạng thái | Bằng chứng |
|---|---|---|---|---|
| TC01 | `docker compose ps` | Controller/router Up | NOT RUN | |
| TC02 | Mở ZAC | Trang quản trị hiển thị | NOT RUN | |
| TC03 | `docker port zt-demo-web` | Không có published port | NOT RUN | |
| TC04 | Policy advisor | Alice Dial Y, Bob Dial N, host Bind Y | NOT RUN | |
| TC05 | Chỉ Alice active | HTTP success qua overlay | NOT RUN | |
| TC06 | Chỉ Bob active | Không thiết lập service session | NOT RUN | |
| TC07 | Revoke Alice | Request mới bị từ chối | NOT RUN | |
| TC08 | Direct TCP/80 từ client | Không kết nối được | NOT RUN | |
| TC09 | Thu thập log | Log đã review và redact | NOT RUN | |
| TC10 | Restore policy | Alice truy cập lại | NOT RUN | |

## Mẫu ghi nhận

```text
Test ID:
Ngày/giờ và timezone:
Docker/OpenZiti version + image digest:
Topology:
Identity active:
Policy:
Thao tác:
Kết quả kỳ vọng:
Kết quả thực tế:
PASS / FAIL / BLOCKED:
Đường dẫn ảnh/log:
Nhận xét:
```
