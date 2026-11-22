# Nguồn upstream

- File: `compose.yml`
- URL: `https://get.openziti.io/dock/all-in-one/compose.yml`
- Ngày lấy: 22/11/2026 (Asia/Saigon)
- Chủ sở hữu: OpenZiti, theo giấy phép và điều khoản của dự án upstream.

Compose dùng image controller chính thức và tạo controller, edge router cùng persistent volume. Image mặc định là tag `latest`; vì vậy khi nghiệm thu phải lưu kết quả `docker image inspect`/digest và `ziti version` vào bằng chứng.

Để chủ động cập nhật, tải file vào vị trí tạm, review diff và chạy lại toàn bộ TC01–TC10 trước khi thay bản đang dùng.
