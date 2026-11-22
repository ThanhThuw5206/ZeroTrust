# Zero Trust với OpenZiti — reproducible demo

Repo này triển khai demo trong tài liệu nghiên cứu theo mô hình:

- OpenZiti Controller + Edge Router + ZAC chạy trên một Linux VM bằng Docker Compose.
- Nginx `zt-demo-web` chỉ nằm trong Docker network, không publish TCP/80 ra host.
- `alice-lab` có quyền `Dial` tới `portal-zt`; `bob-lab` có identity hợp lệ nhưng không có quyền.
- Có bài test thu hồi/khôi phục policy và bộ thu thập bằng chứng.

## Trạng thái hiện tại

Bộ triển khai và bản Compose chính thức tải ngày 22/11/2026 đã được đặt sẵn trong repo, nhưng **chưa được đánh dấu chạy thành công** trên máy này: Docker chưa có trong `PATH` và WSL đang trả về `Wsl/E_ACCESSDENIED`. Kết quả kỳ vọng trong tài liệu không được coi là kết quả thực nghiệm.

## Topology

```text
Windows client (Alice hoặc Bob)
        | TCP 1280/3022
        v
Linux VM: OpenZiti Controller + Router + ZAC
        | Docker private network, không host port
        v
Nginx zt-demo-web:80
```

## Chạy nhanh trên Linux VM

Yêu cầu: Ubuntu 22.04/24.04 hoặc Kali, Docker Engine, Compose plugin, `curl`, và IP/DNS của VM phải truy cập được từ Windows client.

```bash
git clone https://github.com/ThanhThuw5206/ZeroTrust.git
cd ZeroTrust
bash lab/openziti/demo.sh   # lần đầu tạo lab.env rồi dừng
nano lab/openziti/lab.env   # sửa IP/DNS của VM
bash lab/openziti/demo.sh   # tự tải, dựng và config toàn bộ server demo
```

Sau đó lấy hai JWT trong `.runtime/enrollments/` qua kênh riêng, enroll lần lượt vào Ziti Desktop Edge. Không commit hoặc gửi công khai các file này.

```powershell
# Alice đang bật, Bob tắt
powershell -ExecutionPolicy Bypass -File .\lab\client\Test-ZitiAccess.ps1 -Mode Alice

# Alice tắt, Bob đang bật
powershell -ExecutionPolicy Bypass -File .\lab\client\Test-ZitiAccess.ps1 -Mode Bob
```

Thu hồi và khôi phục quyền Alice:

```bash
bash lab/openziti/scripts/04-policy-toggle.sh revoke
# tạo request mới từ client Alice và ghi nhận bị từ chối
bash lab/openziti/scripts/04-policy-toggle.sh restore
```

Thu thập log đã lọc về `evidence/raw/<timestamp>/`:

```bash
bash lab/openziti/scripts/05-collect-evidence.sh
```

## Tài liệu vận hành

- [Runbook triển khai](docs/DEPLOYMENT_RUNBOOK.md)
- [Ánh xạ phạm vi nghiên cứu](docs/RESEARCH_SCOPE.md)
- [Ma trận nghiệm thu](evidence/TEST_MATRIX.md)
- Tài liệu nghiên cứu gốc do nhóm cung cấp không được tự động sao chép vào repo.

## Cổng lab

| Cổng | Thành phần | Phạm vi |
|---:|---|---|
| 1280/TCP | Controller/ZAC | Chỉ mạng lab |
| 3022/TCP | Edge Router | Chỉ mạng lab |
| 80/TCP | Nginx backend | Chỉ Docker network, không publish |

Không dùng credentials lab, CA tự ký hoặc policy `#all` của quickstart cho production.

