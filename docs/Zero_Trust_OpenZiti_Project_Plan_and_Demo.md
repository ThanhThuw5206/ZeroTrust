# ĐỒ ÁN MÔN AN TOÀN MẠNG
## NGHIÊN CỨU KIẾN TRÚC ZERO TRUST VÀ TRIỂN KHAI THỬ NGHIỆM BẰNG OPENZITI

> **Loại đồ án:** Nghiên cứu + triển khai thực nghiệm  
> **Số thành viên:** 03  
> **Giải pháp demo chính:** OpenZiti  
> **Mô hình demo:** Zero Trust Network Access cho một Web Application nội bộ  
> **Môi trường đề xuất:** 03 máy ảo Ubuntu 22.04 LTS  
> **Thời gian triển khai mẫu:** 06 tuần  
> **Chuẩn tham chiếu chính:** NIST SP 800-207, NIST SP 800-207A, CISA Zero Trust Maturity Model  

---

# MỤC LỤC

1. Thông tin chung của đồ án  
2. Lý do chọn đề tài  
3. Mục tiêu đồ án  
4. Câu hỏi nghiên cứu  
5. Phạm vi và giới hạn  
6. Phương pháp thực hiện  
7. Nội dung nghiên cứu lý thuyết  
8. Nội dung nghiên cứu công nghệ và thị trường  
9. Thiết kế hệ thống demo  
10. Kịch bản thực nghiệm và tiêu chí đánh giá  
11. Hướng dẫn demo OpenZiti step by step  
12. Kế hoạch thực hiện theo giai đoạn  
13. Phân chia công việc chi tiết cho 3 thành viên  
14. Work Breakdown Structure – WBS  
15. Timeline 6 tuần  
16. Cấu trúc báo cáo cuối kỳ  
17. Cấu trúc slide thuyết trình  
18. Kịch bản bảo vệ và demo  
19. Danh sách deliverable phải nộp  
20. Quản lý rủi ro  
21. Tiêu chí nghiệm thu đồ án  
22. Hướng phát triển  
23. Tài liệu tham khảo chính  

---

# 1. THÔNG TIN CHUNG CỦA ĐỒ ÁN

## 1.1. Tên đề tài đề xuất

**Nghiên cứu kiến trúc Zero Trust và triển khai thử nghiệm hệ thống Zero Trust Network Access bằng OpenZiti**

Tên tiếng Anh có thể dùng:

**Research on Zero Trust Architecture and Experimental Deployment of Zero Trust Network Access using OpenZiti**

## 1.2. Bài toán

Mô hình an toàn mạng truyền thống thường dựa nhiều vào khái niệm:

> Mạng bên ngoài là không tin cậy – mạng bên trong là tin cậy.

Sau khi người dùng hoặc thiết bị vượt qua firewall, VPN hoặc các cơ chế kiểm soát tại biên mạng, họ thường có khả năng nhìn thấy một phần tương đối lớn của hệ thống nội bộ.

Điều này làm tăng rủi ro:

- Tài khoản VPN bị đánh cắp.
- Credential theft.
- Insider threat.
- Lateral movement.
- Ransomware.
- Remote work.
- BYOD.
- Cloud và multi-cloud.
- Ứng dụng được đặt ngoài phạm vi mạng doanh nghiệp truyền thống.

Zero Trust thay đổi cách tiếp cận:

> Không cấp implicit trust chỉ dựa trên vị trí mạng. Quyền truy cập phải được xác định dựa trên identity, tài nguyên cần truy cập, chính sách và ngữ cảnh.

Đồ án nghiên cứu kiến trúc này và triển khai một mô hình nhỏ để chứng minh nguyên tắc:

**Deny by default + Identity-based access + Least privilege + Service-level authorization.**

---

# 2. LÝ DO CHỌN ĐỀ TÀI

Zero Trust phù hợp với môn An toàn mạng vì liên quan trực tiếp đến:

- Network security.
- Authentication.
- Authorization.
- Identity and Access Management.
- PKI.
- Digital certificate.
- Mutual TLS.
- Network segmentation.
- Policy enforcement.
- Secure remote access.
- Attack surface reduction.
- Defense in depth.

Đề tài đồng thời có cả:

1. **Nội dung học thuật**  
   Nghiên cứu NIST Zero Trust Architecture.

2. **Nội dung công nghệ**  
   Phân tích giải pháp từ Microsoft, Zscaler, Cloudflare, Cisco, Palo Alto Networks, Fortinet,...

3. **Nội dung thực hành**  
   Xây dựng hệ thống Zero Trust mã nguồn mở bằng OpenZiti.

4. **Nội dung đánh giá an toàn**  
   Thử truy cập trái phép, port scanning, policy enforcement, service hiding và latency.

---

# 3. MỤC TIÊU ĐỒ ÁN

## 3.1. Mục tiêu tổng quát

Nghiên cứu kiến trúc Zero Trust, phân tích các thành phần, nguyên tắc, công nghệ và thị trường liên quan; sau đó triển khai thử nghiệm một hệ thống Zero Trust đơn giản sử dụng OpenZiti để kiểm chứng cơ chế truy cập dựa trên identity và policy.

## 3.2. Mục tiêu cụ thể

Đồ án phải đạt được các mục tiêu sau:

### Mục tiêu 1 – Hiểu Zero Trust

Trình bày được:

- Zero Trust là gì.
- Vì sao cần Zero Trust.
- Zero Trust khác VPN và perimeter security như thế nào.
- Các nguyên tắc cốt lõi.
- Các thành phần của kiến trúc.

### Mục tiêu 2 – Phân tích kiến trúc chuẩn

Nghiên cứu:

- NIST SP 800-207.
- Policy Engine.
- Policy Administrator.
- Policy Enforcement Point.
- Identity.
- Device.
- Resource.
- Policy Information Point.
- Control plane và data plane.

### Mục tiêu 3 – Khảo sát công nghệ

Khảo sát ít nhất 6 hệ sinh thái:

- Microsoft.
- Zscaler.
- Cloudflare.
- Palo Alto Networks.
- Cisco.
- Fortinet.
- OpenZiti.

### Mục tiêu 4 – Khảo sát thị trường

Phân tích:

- Động lực tăng trưởng.
- Remote/hybrid work.
- Cloud adoption.
- Identity attack.
- Ransomware.
- Regulatory requirements.
- Xu hướng ZTNA/SASE/SSE.

### Mục tiêu 5 – Triển khai demo

Xây dựng:

- OpenZiti Controller.
- OpenZiti Edge Router.
- Private Web Application.
- Server Identity.
- Client Identity.
- Service.
- Bind Policy.
- Dial Policy.

### Mục tiêu 6 – Kiểm chứng an toàn

Chứng minh:

- Không có identity → không truy cập.
- Có identity nhưng không có policy → không truy cập.
- Identity được cấp đúng policy → truy cập thành công.
- Web service không cần public trực tiếp.
- Nmap không nhìn thấy private web service sau khi chuyển sang mô hình Zero Trust.
- Traffic overlay không hiển thị HTTP plaintext trên đường truyền mạng.

---

# 4. CÂU HỎI NGHIÊN CỨU

Đồ án nên trả lời các câu hỏi sau.

## RQ1

**Zero Trust Architecture là gì và vì sao nó xuất hiện?**

## RQ2

**Zero Trust khác kiến trúc mạng perimeter/VPN truyền thống như thế nào?**

## RQ3

**Các thành phần của một Zero Trust Architecture hoạt động và tương tác như thế nào?**

## RQ4

**Các nhà cung cấp lớn hiện thực Zero Trust bằng các sản phẩm và công nghệ nào?**

## RQ5

**Ưu điểm và hạn chế của Zero Trust trong triển khai thực tế là gì?**

## RQ6

**OpenZiti có thể được sử dụng để xây dựng một mô hình Zero Trust đơn giản cho sinh viên hay không?**

## RQ7

**Việc chuyển một Web Service từ mô hình public port sang OpenZiti ảnh hưởng như thế nào đến attack surface và quyền truy cập?**

---

# 5. PHẠM VI VÀ GIỚI HẠN

## 5.1. Trong phạm vi

Đồ án nghiên cứu:

- Zero Trust Architecture.
- Zero Trust Network Access – ZTNA.
- Identity-based access.
- PKI và certificate ở mức ứng dụng.
- Service policy.
- OpenZiti overlay network.
- Web application access.
- Port exposure.
- Basic performance comparison.
- Basic network traffic observation.

## 5.2. Ngoài phạm vi

Không bắt buộc triển khai:

- Enterprise SIEM hoàn chỉnh.
- SOC.
- EDR thương mại.
- DLP.
- Full Active Directory enterprise.
- Full multi-cloud.
- Production-grade HA cluster.
- Kubernetes.
- Complex MFA.
- Device posture nâng cao.

Các nội dung trên chỉ được xem là **hướng mở rộng** nếu còn thời gian.

---

# 6. PHƯƠNG PHÁP THỰC HIỆN

Đồ án sử dụng 4 phương pháp.

## 6.1. Nghiên cứu tài liệu

Nguồn ưu tiên:

1. NIST.
2. CISA.
3. Tài liệu chính thức của hãng.
4. OpenZiti Documentation.
5. Whitepaper.
6. Báo cáo thị trường uy tín.

## 6.2. Phân tích so sánh

So sánh:

- Traditional network security.
- VPN.
- ZTNA.
- Zero Trust Architecture.

## 6.3. Triển khai thực nghiệm

Xây dựng lab 3 VM và triển khai OpenZiti.

## 6.4. Đánh giá thực nghiệm

Đánh giá:

- Authorized access.
- Unauthorized access.
- Service exposure.
- Policy enforcement.
- Revocation/change policy.
- Network visibility.
- Latency.
- Resource usage.

---

# 7. NỘI DUNG NGHIÊN CỨU LÝ THUYẾT

# 7.1. Mô hình bảo mật truyền thống

Mô hình:

```text
Internet
   |
Firewall
   |
VPN
   |
-----------------------
    Internal Network
-----------------------
 |        |        |
Web      DB       File
Server   Server    Server
```

Đặc trưng:

- Trust dựa nhiều vào network location.
- Sau khi vào mạng nội bộ, user có thể nhìn thấy nhiều tài nguyên.
- Security boundary tập trung ở perimeter.
- VPN thường cấp network-level connectivity.

## Hạn chế

- Credential bị đánh cắp.
- VPN account bị compromise.
- Lateral movement.
- Flat network.
- Misconfigured firewall.
- Insider threat.

---

# 7.2. Định nghĩa Zero Trust

Theo tinh thần của NIST SP 800-207:

Zero Trust chuyển trọng tâm bảo vệ từ network perimeter sang:

- User.
- Device.
- Asset.
- Application.
- Service.
- Resource.

Không cấp trust chỉ vì:

- User đang ở LAN.
- User dùng máy công ty.
- User kết nối VPN.
- Resource nằm trong datacenter.

---

# 7.3. Nguyên tắc cốt lõi

## Verify Explicitly

Xác minh dựa trên:

- Identity.
- Credential.
- Device.
- Context.
- Policy.

## Least Privilege

Người dùng chỉ được:

- Đúng tài nguyên.
- Đúng dịch vụ.
- Đúng thời điểm.
- Đúng quyền cần thiết.

## Assume Breach

Thiết kế hệ thống với giả định attacker có thể đã có mặt trong hệ thống.

## Deny by Default

Không có rule cho phép → từ chối.

---

# 7.4. Kiến trúc logic theo NIST

```text
             +------------------------+
             |     Policy Engine      |
             |          PE            |
             +-----------+------------+
                         |
                  Decision: Allow/Deny
                         |
             +-----------v------------+
             | Policy Administrator   |
             |          PA            |
             +-----------+------------+
                         |
                  Control Channel
                         |
Client --------> +-------v-------+ --------> Resource
                 |      PEP      |
                 +---------------+
```

## Policy Engine – PE

Quyết định:

- Cho phép.
- Từ chối.
- Thu hồi session.

## Policy Administrator – PA

Thực hiện quyết định:

- Thiết lập session.
- Cấp credential/session information.
- Ngắt session.

## Policy Enforcement Point – PEP

Thực thi:

- Cho traffic đi qua.
- Chặn traffic.
- Ngắt kết nối.

---

# 7.5. Các nguồn dữ liệu cho Policy Engine

Một hệ thống thực tế có thể sử dụng:

- IAM.
- Device inventory.
- EDR.
- Threat intelligence.
- SIEM.
- User behavior.
- Geo-location.
- Risk score.
- Resource sensitivity.

---

# 7.6. Zero Trust Pillars

Phân tích theo các nhóm:

1. Identity.
2. Device.
3. Network.
4. Application.
5. Data.
6. Infrastructure.
7. Visibility/Analytics.

---

# 7.7. Traditional VPN và ZTNA

| Tiêu chí | VPN truyền thống | ZTNA |
|---|---|---|
| Đối tượng cấp quyền | Network | Application/Service |
| Trust | Sau khi VPN thành công thường có network access | Không implicit trust |
| Discoverability | Có thể thấy tài nguyên khác | Giảm khả năng discover |
| Least privilege | Khó hơn | Tốt hơn |
| Identity | Có | Là trung tâm |
| Segmentation | VLAN/subnet/firewall | Identity/service policy |
| Remote access | Có | Có |
| Lateral movement | Rủi ro cao hơn | Giảm |

---

# 8. NGHIÊN CỨU CÔNG NGHỆ VÀ THỊ TRƯỜNG

# 8.1. Các giải pháp cần khảo sát

## Microsoft

Nghiên cứu:

- Microsoft Entra ID.
- Conditional Access.
- Microsoft Intune.
- Microsoft Defender.
- Identity-driven security.

## Zscaler

Nghiên cứu:

- Zero Trust Exchange.
- Zscaler Private Access – ZPA.
- Zscaler Internet Access – ZIA.

## Cloudflare

Nghiên cứu:

- Cloudflare One.
- Cloudflare Access.
- Identity-aware application access.

## Palo Alto Networks

Nghiên cứu:

- Prisma Access.
- ZTNA.
- SASE.

## Cisco

Nghiên cứu:

- Cisco Secure Access.
- Identity.
- Device posture.
- SSE/SASE.

## Fortinet

Nghiên cứu:

- FortiGate.
- FortiClient.
- FortiClient EMS.
- ZTNA tags.

## OpenZiti

Nghiên cứu:

- Controller.
- Router.
- Identity.
- Service.
- Service policy.
- Overlay networking.
- mTLS.

---

# 8.2. Khung so sánh hãng

Không chỉ liệt kê sản phẩm.

Mỗi hãng phải so sánh theo:

| Tiêu chí | Nội dung |
|---|---|
| Identity | Cách xác minh user/device |
| Access model | Network hay application |
| ZTNA | Có/không |
| Device posture | Có/không |
| Cloud integration | Mức độ |
| On-premises | Mức độ |
| SASE/SSE | Có/không |
| Policy | Kiểu policy |
| Logging | Khả năng |
| Strength | Điểm mạnh |
| Weakness | Hạn chế |
| Target | Đối tượng doanh nghiệp |

---

# 8.3. Phân tích thị trường

Phần báo cáo cần trả lời:

- Vì sao thị trường Zero Trust tăng trưởng?
- Doanh nghiệp nào cần Zero Trust?
- Zero Trust có liên quan gì tới SASE/SSE?
- Cloud ảnh hưởng như thế nào?
- Remote work ảnh hưởng như thế nào?

## Động lực thị trường

```text
Cloud Adoption
       +
Hybrid Work
       +
Identity Attack
       +
Ransomware
       +
BYOD
       +
Multi-cloud
       +
Compliance
       |
       v
Zero Trust Adoption
```

Khi dùng số liệu thị trường phải:

- Ghi năm.
- Ghi nguồn.
- Không trộn số liệu từ nhiều báo cáo như thể cùng phương pháp thống kê.
- Ghi rõ đây là forecast/estimate.

---

# 8.4. Ưu điểm

- Least privilege.
- Identity-centric.
- Giảm lateral movement.
- Hạn chế service exposure.
- Microsegmentation.
- Remote access phù hợp cloud.
- Granular policy.
- Better visibility.
- Có thể revoke quyền nhanh.
- Không phụ thuộc hoàn toàn vào network location.

---

# 8.5. Nhược điểm

- Triển khai phức tạp.
- Chi phí migration.
- Legacy application khó tích hợp.
- Policy có thể rất phức tạp.
- IAM trở thành thành phần cực kỳ quan trọng.
- PKI/certificate management khó.
- Có thể tăng latency.
- Phụ thuộc vào availability của control infrastructure.
- Có thể xảy ra vendor lock-in với giải pháp thương mại.
- Yêu cầu thay đổi tư duy vận hành.

---

# 9. THIẾT KẾ HỆ THỐNG DEMO

# 9.1. Mục tiêu demo

Chứng minh 4 tính chất:

1. **Identity-based authentication.**
2. **Service-level authorization.**
3. **Deny by default.**
4. **Service không cần expose trực tiếp ra mạng.**

---

# 9.2. Topology

```text
                     ZERO TRUST INFRASTRUCTURE

               +-------------------------------+
               | VM1 - ZT-CONTROLLER           |
               | 192.168.56.10                 |
               |                               |
               | OpenZiti Controller           |
               | OpenZiti Edge Router          |
               | PKI                           |
               | Policy Management             |
               +---------------+---------------+
                               |
                        OpenZiti Overlay
                     Encrypted / Identity-based
                               |
                +--------------+--------------+
                |                             |
                |                             |
+---------------v-------------+   +-----------v------------+
| VM2 - PRIVATE-WEB           |   | VM3 - CLIENT           |
| 192.168.56.20               |   | 192.168.56.30          |
|                             |   |                        |
| Python HTTP / Nginx         |   | Alice Identity         |
| 127.0.0.1:8080              |   | Bob Identity           |
|                             |   | OpenZiti Tunneler      |
| OpenZiti Tunneler           |   | curl / nmap / tcpdump  |
| server-host Identity        |   |                        |
+-----------------------------+   +------------------------+
```

---

# 9.3. IP Plan

> Đây là IP mẫu. Nhóm có thể thay đổi theo VMware/VirtualBox.

| Máy | Hostname | IP |
|---|---|---|
| VM1 | zt-controller | 192.168.56.10 |
| VM2 | private-web | 192.168.56.20 |
| VM3 | zt-client | 192.168.56.30 |

## Network đề xuất

Mỗi VM có:

- Adapter 1: NAT – để tải package.
- Adapter 2: Host-only Network – để lab giao tiếp.

Ví dụ:

```text
192.168.56.0/24
```

---

# 9.4. Tài nguyên máy

| VM | CPU | RAM | Disk |
|---|---:|---:|---:|
| VM1 | 2 vCPU | 4 GB | 25 GB |
| VM2 | 1–2 vCPU | 2 GB | 20 GB |
| VM3 | 2 vCPU | 2–4 GB | 20 GB |

Tổng đề xuất:

- CPU: 5–6 vCPU.
- RAM: khoảng 8 GB.
- Disk: khoảng 65 GB.

Nếu laptop hạn chế:

- VM1: 2 GB RAM.
- VM2: 1 GB RAM.
- VM3: 2 GB RAM.

---

# 10. KỊCH BẢN THỰC NGHIỆM

Phải có **baseline** và **Zero Trust state**.

---

# 10.1. Scenario A – Mô hình truyền thống

VM2 chạy:

```text
Web service = 0.0.0.0:8080
```

VM3:

```bash
nmap -sV -p 8080 192.168.56.20
curl http://192.168.56.20:8080
```

Kỳ vọng:

```text
Port 8080 OPEN
HTTP request SUCCESS
```

Ý nghĩa:

- Client biết server IP.
- Client discover được service.
- Service expose trực tiếp vào network.

---

# 10.2. Scenario B – Zero Trust

VM2 chuyển thành:

```text
Web service = 127.0.0.1:8080
```

VM3:

```bash
curl http://192.168.56.20:8080
```

Kỳ vọng:

```text
FAIL
```

Nmap:

```bash
nmap -sV -p 8080 192.168.56.20
```

Kỳ vọng:

```text
8080 closed hoặc filtered
```

Nhưng Alice:

```bash
curl http://private-web.ziti
```

Kỳ vọng:

```text
SUCCESS
```

---

# 10.3. Scenario C – Unauthorized Identity

Bob có identity hợp lệ nhưng **không có Dial Policy**.

Bob:

```bash
curl http://private-web.ziti
```

Kỳ vọng:

```text
Không truy cập được service
```

Đây là một test rất quan trọng:

> Authentication thành công không đồng nghĩa Authorization thành công.

---

# 10.4. Scenario D – Policy Change

Ban đầu:

```text
Alice -> private-web = ALLOW
Bob   -> private-web = DENY
```

Sau đó xóa Dial Policy của Alice.

Kỳ vọng:

```text
Alice mất quyền truy cập service.
```

Có thể tạo lại policy sau khi demo.

---

# 10.5. Scenario E – Network Traffic Observation

Capture traffic trên VM3:

```bash
sudo tcpdump -i any -nn
```

hoặc Wireshark.

Kiểm tra:

- Không thấy HTTP GET plaintext chạy trực tiếp từ VM3 tới VM2.
- Client giao tiếp với OpenZiti Router qua encrypted overlay.

---

# 10.6. Scenario F – Latency

Thực hiện:

### Traditional

```bash
curl -s -o /dev/null -w "%{time_total}\n" http://192.168.56.20:8080
```

### OpenZiti

```bash
curl -s -o /dev/null -w "%{time_total}\n" http://private-web.ziti
```

Mỗi loại chạy 20 lần.

Tính:

- Average.
- Min.
- Max.

Không cần chứng minh OpenZiti nhanh hơn.

Mục tiêu là:

> Đánh giá security/performance trade-off.

---

# 11. HƯỚNG DẪN DEMO OPENZITI STEP BY STEP

> **Khuyến nghị:** thực hiện trước trên snapshot VM để dễ rollback.  
> Các lệnh dưới đây dùng cho lab học tập và được xây dựng theo luồng quickstart chính thức của OpenZiti.  
> Nếu phiên bản OpenZiti mới thay đổi package/CLI, ưu tiên đối chiếu OpenZiti Documentation trước khi demo chính thức.

---

# PHASE 0 – CHUẨN BỊ 3 VM

## Bước 0.1 – Tạo VM

Tạo:

```text
VM1: zt-controller
VM2: private-web
VM3: zt-client
```

OS:

```text
Ubuntu 22.04 LTS
```

## Bước 0.2 – Cài công cụ cơ bản trên cả 3 VM

```bash
sudo apt update
sudo apt install -y curl wget git vim net-tools iproute2 openssh-server
sudo systemctl enable --now ssh
```

VM3 cài thêm:

```bash
sudo apt install -y nmap tcpdump
```

Kiểm tra:

```bash
ip a
```

Ghi lại IP của từng máy.

---

# PHASE 1 – KIỂM TRA KẾT NỐI LAB

Trên VM3:

```bash
ping -c 4 192.168.56.10
ping -c 4 192.168.56.20
```

Trên VM2:

```bash
ping -c 4 192.168.56.10
```

Nếu không ping được:

- Kiểm tra Host-only adapter.
- Kiểm tra IP.
- Kiểm tra firewall.
- Kiểm tra VMware/VirtualBox network.

---

# PHASE 2 – BASELINE TRADITIONAL WEB

## Bước 2.1 – Tạo web app trên VM2

```bash
mkdir -p ~/private-web
cat > ~/private-web/index.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Zero Trust Demo</title>
</head>
<body>
    <h1>Private Web Service</h1>
    <p>Zero Trust OpenZiti Demo</p>
</body>
</html>
EOF
```

## Bước 2.2 – Chạy public web service

VM2:

```bash
python3 -m http.server 8080 \
  --bind 0.0.0.0 \
  --directory ~/private-web
```

Giữ terminal này mở.

## Bước 2.3 – Scan từ VM3

```bash
nmap -sV -p 8080 192.168.56.20
```

Kỳ vọng:

```text
8080/tcp open
```

## Bước 2.4 – Truy cập trực tiếp

```bash
curl http://192.168.56.20:8080
```

Kỳ vọng thấy:

```html
<h1>Private Web Service</h1>
```

## Bước 2.5 – Lưu bằng chứng

Chụp:

```text
01-baseline-nmap.png
02-baseline-curl.png
```

Đây là bằng chứng cho:

> Trước Zero Trust, service được expose trực tiếp.

---

# PHASE 3 – CÀI OPENZITI TRÊN VM1

## Bước 3.1 – Xác định IP VM1

```bash
ip -4 addr
```

Trong tài liệu này giả sử:

```text
VM1 = 192.168.56.10
```

## Bước 3.2 – Cấu hình biến môi trường

VM1:

```bash
export EXTERNAL_IP="192.168.56.10"

export ZITI_CTRL_EDGE_IP_OVERRIDE="${EXTERNAL_IP}"

export ZITI_CTRL_ADVERTISED_ADDRESS="${EXTERNAL_IP}"
export ZITI_CTRL_ADVERTISED_PORT=8440

export ZITI_CTRL_EDGE_ADVERTISED_ADDRESS="${EXTERNAL_IP}"
export ZITI_CTRL_EDGE_ADVERTISED_PORT=8441

export ZITI_ROUTER_ADVERTISED_ADDRESS="${EXTERNAL_IP}"
export ZITI_ROUTER_IP_OVERRIDE="${EXTERNAL_IP}"
export ZITI_ROUTER_PORT=8442
```

## Bước 3.3 – Chạy OpenZiti Express Install

```bash
source /dev/stdin <<< "$(wget -qO- https://get.openziti.io/ziti-cli-functions.sh)"
expressInstall
```

Quickstart sẽ thực hiện các bước chính:

- Download Ziti CLI.
- Tạo PKI.
- Tạo Controller config.
- Khởi tạo Controller.
- Tạo Router.
- Enroll Router.
- Tạo các router policies mặc định.

## Bước 3.4 – Source environment sau khi login lại

Nếu mở terminal mới:

```bash
source ~/.ziti/quickstart/$(hostname -s)/$(hostname -s).env
```

## Bước 3.5 – Login Ziti CLI

```bash
zitiLogin
```

## Bước 3.6 – Kiểm tra Controller

```bash
ziti edge list controllers
```

## Bước 3.7 – Kiểm tra Edge Router

```bash
ziti edge list edge-routers
```

Router phải ở trạng thái online.

## Bước 3.8 – Kiểm tra policy nền

```bash
ziti edge list edge-router-policies
ziti edge list service-edge-router-policies
```

Nếu quickstart đã tạo default policy thì không cần tạo lại.

Nếu chưa có, tạo lab policy:

```bash
ziti edge create edge-router-policy lab-all-identities \
  --edge-router-roles '#all' \
  --identity-roles '#all'

ziti edge create service-edge-router-policy lab-all-services \
  --edge-router-roles '#all' \
  --service-roles '#all'
```

## Bước 3.9 – Firewall VM1

Nếu UFW đang bật:

```bash
sudo ufw allow 8440/tcp
sudo ufw allow 8441/tcp
sudo ufw allow 8442/tcp
```

Kiểm tra:

```bash
sudo ufw status
```

---

# PHASE 4 – TẠO IDENTITIES

Trên VM1:

```bash
zitiLogin
```

## Bước 4.1 – Server identity

```bash
ziti edge create identity server-host \
  --role-attributes web-host \
  -o server-host.jwt
```

## Bước 4.2 – Alice identity

```bash
ziti edge create identity alice-client \
  --role-attributes web-client \
  -o alice-client.jwt
```

## Bước 4.3 – Bob identity

```bash
ziti edge create identity bob-client \
  --role-attributes unauthorized-client \
  -o bob-client.jwt
```

## Bước 4.4 – Kiểm tra

```bash
ziti edge list identities
```

Phải thấy:

```text
server-host
alice-client
bob-client
```

---

# PHASE 5 – TẠO OPENZITI SERVICE

Trên VM1.

## Bước 5.1 – Tạo intercept config

Client sẽ gọi:

```text
http://private-web.ziti
```

Tạo config:

```bash
ziti edge create config private-web-intercept intercept.v1 \
'{
  "protocols":["tcp"],
  "addresses":["private-web.ziti"],
  "portRanges":[
    {"low":80,"high":80}
  ]
}'
```

## Bước 5.2 – Tạo host config

Web server thực nằm tại:

```text
127.0.0.1:8080
```

trên VM2.

```bash
ziti edge create config private-web-host host.v1 \
'{
  "protocol":"tcp",
  "address":"127.0.0.1",
  "port":8080
}'
```

## Bước 5.3 – Tạo service

```bash
ziti edge create service private-web \
  --configs private-web-intercept,private-web-host
```

## Bước 5.4 – Kiểm tra

```bash
ziti edge list services
ziti edge list configs
```

---

# PHASE 6 – TẠO SERVICE POLICIES

## Bước 6.1 – Bind Policy

Cho phép `server-host` cung cấp service.

```bash
ziti edge create service-policy private-web-bind Bind \
  --service-roles '@private-web' \
  --identity-roles '@server-host'
```

## Bước 6.2 – Dial Policy

Chỉ Alice được truy cập.

```bash
ziti edge create service-policy private-web-dial Dial \
  --service-roles '@private-web' \
  --identity-roles '@alice-client'
```

## Không tạo Dial Policy cho Bob

Đây là chủ ý của test.

## Bước 6.3 – Kiểm tra policy

```bash
ziti edge list service-policies
```

## Bước 6.4 – Policy Advisor

```bash
ziti edge policy-advisor services private-web -q
```

Kỳ vọng logic:

```text
server-host  -> Bind = YES
alice-client -> Dial = YES
bob-client   -> Dial = NO
```

Chụp màn hình:

```text
03-policy-advisor.png
```

---

# PHASE 7 – CÀI ZITI-EDGE-TUNNEL TRÊN VM2

## Bước 7.1 – Cài repository key

```bash
curl -sSLf https://get.openziti.io/tun/package-repos.gpg \
| sudo gpg --dearmor --yes \
  --output /usr/share/keyrings/openziti.gpg
```

```bash
sudo chmod a+r /usr/share/keyrings/openziti.gpg
```

## Bước 7.2 – Thêm stable repository

```bash
echo "deb [signed-by=/usr/share/keyrings/openziti.gpg] https://packages.openziti.org/zitipax-openziti-deb-stable debian main" \
| sudo tee /etc/apt/sources.list.d/openziti-release.list
```

## Bước 7.3 – Install

```bash
sudo apt update
sudo apt install -y ziti-edge-tunnel
```

Kiểm tra:

```bash
ziti-edge-tunnel version
```

## Nếu package repository thay đổi

Dùng manual installation theo OpenZiti Documentation:

1. Download latest stable `ziti-edge-tunnel`.
2. Copy binary:

```bash
sudo install -o root -g root ./ziti-edge-tunnel /usr/local/bin/
```

3. Tạo thư mục identities:

```bash
sudo groupadd --system ziti 2>/dev/null || true
sudo mkdir -p /opt/openziti/etc/identities
sudo chown -R :ziti /opt/openziti/etc/identities
sudo chmod -R ug=rwX,o-rwx /opt/openziti/etc/identities
```

---

# PHASE 8 – CHUYỂN SERVER JWT TỚI VM2

Từ VM1:

```bash
scp server-host.jwt \
  <USERNAME_VM2>@192.168.56.20:/home/<USERNAME_VM2>/
```

Ví dụ nếu username là `student`:

```bash
scp server-host.jwt student@192.168.56.20:/home/student/
```

**Không đưa JWT và identity JSON lên GitHub.**

---

# PHASE 9 – ENROLL SERVER IDENTITY

VM2:

```bash
cd ~
```

## Cách A – Add trực tiếp vào tunneler service

```bash
sudo systemctl enable --now ziti-edge-tunnel
```

```bash
sudo ziti-edge-tunnel add \
  --jwt "$(< ./server-host.jwt)" \
  --identity server-host
```

Kiểm tra:

```bash
sudo systemctl status ziti-edge-tunnel
```

Sau enrollment thành công, JWT là one-time token và không nên tái sử dụng.

---

# PHASE 10 – CHUYỂN WEB APP THÀNH PRIVATE SERVICE

Dừng web server baseline bằng:

```text
Ctrl + C
```

Chạy lại chỉ trên localhost:

```bash
python3 -m http.server 8080 \
  --bind 127.0.0.1 \
  --directory ~/private-web
```

VM2 tự kiểm tra:

```bash
curl http://127.0.0.1:8080
```

Phải SUCCESS.

Kiểm tra:

```bash
ss -lntp | grep 8080
```

Kỳ vọng:

```text
127.0.0.1:8080
```

Không phải:

```text
0.0.0.0:8080
```

---

# PHASE 11 – KIỂM TRA SERVICE ĐÃ BỊ ẨN KHỎI NETWORK

VM3:

```bash
nmap -sV -p 8080 192.168.56.20
```

Kỳ vọng:

```text
closed
```

Thử:

```bash
curl --connect-timeout 3 http://192.168.56.20:8080
```

Kỳ vọng:

```text
FAIL
```

Chụp:

```text
04-after-zero-trust-nmap.png
05-direct-access-fail.png
```

---

# PHASE 12 – CÀI TUNNELER TRÊN VM3

Lặp lại cài đặt package như VM2.

```bash
curl -sSLf https://get.openziti.io/tun/package-repos.gpg \
| sudo gpg --dearmor --yes \
  --output /usr/share/keyrings/openziti.gpg

sudo chmod a+r /usr/share/keyrings/openziti.gpg

echo "deb [signed-by=/usr/share/keyrings/openziti.gpg] https://packages.openziti.org/zitipax-openziti-deb-stable debian main" \
| sudo tee /etc/apt/sources.list.d/openziti-release.list

sudo apt update
sudo apt install -y ziti-edge-tunnel
```

---

# PHASE 13 – CHUYỂN ALICE/BOB JWT TỚI VM3

VM1:

```bash
scp alice-client.jwt bob-client.jwt \
  <USERNAME_VM3>@192.168.56.30:/home/<USERNAME_VM3>/
```

---

# PHASE 14 – ENROLL ALICE VÀ BOB RIÊNG

Trên VM3:

```bash
cd ~
```

Enroll Alice:

```bash
ziti-edge-tunnel enroll \
  --jwt ./alice-client.jwt \
  --identity ./alice-client.json
```

Enroll Bob:

```bash
ziti-edge-tunnel enroll \
  --jwt ./bob-client.jwt \
  --identity ./bob-client.json
```

> File JSON sau enrollment chứa private key/certificate identity.  
> Không upload lên GitHub.

---

# PHASE 15 – TEST ALICE

Để test từng identity riêng biệt, dừng system service trước:

```bash
sudo systemctl stop ziti-edge-tunnel
```

Chạy Alice:

```bash
sudo ziti-edge-tunnel run -i ./alice-client.json
```

Giữ terminal này mở.

Mở terminal khác trên VM3.

## Kiểm tra DNS

```bash
getent hosts private-web.ziti
```

## Truy cập

```bash
curl http://private-web.ziti
```

Kỳ vọng:

```html
<h1>Private Web Service</h1>
```

Chụp:

```text
06-alice-access-success.png
```

---

# PHASE 16 – TEST BOB

Dừng Alice tunneler:

```text
Ctrl + C
```

Chạy Bob:

```bash
sudo ziti-edge-tunnel run -i ./bob-client.json
```

Terminal khác:

```bash
curl --connect-timeout 5 http://private-web.ziti
```

Bob không có Dial Policy.

Kỳ vọng:

```text
Không truy cập được private-web.
```

Chụp:

```text
07-bob-access-denied.png
```

---

# PHASE 17 – TEST POLICY THAY ĐỔI

Trên VM1:

```bash
zitiLogin
```

Xóa policy của Alice:

```bash
ziti edge delete service-policy private-web-dial
```

Chạy lại Alice trên VM3:

```bash
sudo ziti-edge-tunnel run -i ./alice-client.json
```

Thử:

```bash
curl --connect-timeout 5 http://private-web.ziti
```

Kỳ vọng:

```text
FAIL
```

Tạo lại policy:

```bash
ziti edge create service-policy private-web-dial Dial \
  --service-roles '@private-web' \
  --identity-roles '@alice-client'
```

Test lại:

```bash
curl http://private-web.ziti
```

Kỳ vọng:

```text
SUCCESS
```

Điểm cần trình bày:

> Quyền truy cập nằm ở policy; không cần thay đổi firewall rule trên VM2 để cấp quyền từng user.

---

# PHASE 18 – CAPTURE TRAFFIC

Trên VM3:

```bash
sudo tcpdump -i any -nn -A
```

Sau đó:

```bash
curl http://private-web.ziti
```

Quan sát:

- Không có HTTP GET plaintext gửi trực tiếp tới `192.168.56.20:8080`.
- Network traffic được chuyển qua OpenZiti overlay.

Nếu dùng Wireshark:

Filter thử:

```text
tcp.port == 8442
```

hoặc tìm traffic giữa VM3 và VM1.

Không cần giải mã traffic.

Mục tiêu:

> Chứng minh HTTP application không được gửi dưới dạng kết nối trực tiếp Client → VM2:8080.

---

# PHASE 19 – PERFORMANCE TEST

## Traditional baseline

Tạm chạy web:

```bash
python3 -m http.server 8080 \
  --bind 0.0.0.0 \
  --directory ~/private-web
```

VM3:

```bash
for i in {1..20}; do
  curl -s -o /dev/null \
  -w "%{time_total}\n" \
  http://192.168.56.20:8080
done | tee traditional-latency.txt
```

## OpenZiti

Chuyển VM2 về:

```bash
python3 -m http.server 8080 \
  --bind 127.0.0.1 \
  --directory ~/private-web
```

Chạy Alice tunneler.

VM3:

```bash
for i in {1..20}; do
  curl -s -o /dev/null \
  -w "%{time_total}\n" \
  http://private-web.ziti
done | tee openziti-latency.txt
```

Tính trung bình:

```bash
awk '{sum+=$1} END {print "Average =", sum/NR}' \
traditional-latency.txt

awk '{sum+=$1} END {print "Average =", sum/NR}' \
openziti-latency.txt
```

Lưu file vào:

```text
results/
```

---

# PHASE 20 – ĐO RESOURCE USAGE

VM1:

```bash
free -h
top
ps aux | grep ziti
```

VM2:

```bash
ps aux | grep ziti-edge-tunnel
```

Ghi:

- CPU.
- RAM.
- Số process.

Không cần benchmark production.

---

# 12. KẾ HOẠCH THỰC HIỆN THEO GIAI ĐOẠN

# Giai đoạn 1 – Xây dựng đề cương và phạm vi

Kết quả phải có:

- Tên đề tài.
- Mục tiêu.
- RQ1–RQ7.
- Scope.
- Sơ đồ lab.
- Danh sách tài liệu chuẩn.
- Repository nhóm.

Không được bắt đầu demo khi chưa thống nhất topology và IP plan.

---

# Giai đoạn 2 – Nghiên cứu lý thuyết

Kết quả:

- Zero Trust definition.
- NIST Architecture.
- Principles.
- VPN vs ZTNA.
- PE/PA/PEP.
- Zero Trust pillars.

---

# Giai đoạn 3 – Khảo sát công nghệ và thị trường

Kết quả:

- Bảng 6 hãng.
- Market trend.
- Advantages/disadvantages.
- Vì sao chọn OpenZiti.

---

# Giai đoạn 4 – Xây dựng lab

Kết quả:

- 3 VM hoạt động.
- Ping.
- SSH.
- Controller online.
- Router online.
- Web baseline hoạt động.

---

# Giai đoạn 5 – Xây dựng Zero Trust Service

Kết quả:

- 3 identities.
- Intercept config.
- Host config.
- Service.
- Bind policy.
- Dial policy.
- Server tunneler.
- Client tunneler.

---

# Giai đoạn 6 – Security Testing

Kết quả:

- Baseline nmap.
- Zero Trust nmap.
- Alice success.
- Bob deny.
- Policy removal test.
- Traffic capture.
- Latency results.

---

# Giai đoạn 7 – Viết báo cáo và thuyết trình

Kết quả:

- Báo cáo.
- Slide.
- Demo script.
- Screenshot.
- Backup video.
- Source/config.

---

# 13. PHÂN CHIA CÔNG VIỆC CHI TIẾT CHO 3 THÀNH VIÊN

Đặt tên tạm:

- **TV1 – Thành viên 1**
- **TV2 – Thành viên 2**
- **TV3 – Thành viên 3**

Thay bằng tên thật khi nhóm sử dụng file.

---

# 13.1. TV1 – ZERO TRUST ARCHITECTURE + OPENZITI INFRASTRUCTURE LEAD

## Trách nhiệm chính

TV1 chịu trách nhiệm:

1. Nền tảng lý thuyết Zero Trust.
2. NIST SP 800-207.
3. Kiến trúc logic.
4. OpenZiti Controller.
5. Edge Router.
6. Integration giữa 3 VM.
7. Tổng hợp technical architecture.

## Công việc cụ thể

### Research

TV1 phải đọc và viết:

- Định nghĩa Zero Trust.
- Lý do xuất hiện.
- Seven tenets của NIST.
- PE.
- PA.
- PEP.
- Control plane.
- Data plane.
- Trust algorithm.
- Identity/resource relationship.
- Traditional vs Zero Trust.
- VPN vs ZTNA.

### Lab

TV1 thực hiện:

- Tạo VM1.
- Cấu hình Host-only IP VM1.
- Install OpenZiti quickstart.
- Kiểm tra Controller.
- Kiểm tra Router.
- Firewall port.
- Tạo identities:
  - server-host.
  - alice-client.
  - bob-client.
- Tạo service configs.
- Tạo service.
- Tạo Bind Policy.
- Tạo Dial Policy.
- Chạy Policy Advisor.

### Deliverables TV1

```text
docs/01-introduction.md
docs/02-zero-trust-fundamentals.md
docs/03-nist-architecture.md

architecture/zero-trust-nist.drawio
architecture/openziti-lab.drawio

openziti/controller/
openziti/policies/
openziti/services/

screenshots/controller/
```

### Điều kiện nghiệm thu TV1

TV1 chỉ được xem là hoàn thành khi:

- Controller online.
- Router online.
- 3 identities xuất hiện.
- private-web service xuất hiện.
- Bind/Dial policy đúng.
- `policy-advisor` thể hiện Alice có Dial và server có Bind.
- Bob không được Dial.

---

# 13.2. TV2 – TECHNOLOGY/MARKET + PRIVATE APPLICATION LEAD

## Trách nhiệm chính

TV2 chịu trách nhiệm:

1. Khảo sát vendor.
2. Market analysis.
3. Ưu/nhược điểm.
4. VM2 Private Application.
5. Server tunneler.
6. Baseline Traditional vs Zero Trust.

## Research

TV2 phải nghiên cứu:

### Microsoft

- Entra.
- Conditional Access.
- Endpoint.
- Defender.

### Zscaler

- ZPA.
- Zero Trust Exchange.

### Cloudflare

- Cloudflare Access.
- Cloudflare One.

### Palo Alto Networks

- Prisma Access.

### Cisco

- Secure Access.

### Fortinet

- FortiGate/FortiClient/EMS.

TV2 tạo bảng so sánh ít nhất:

```text
Vendor
Architecture
Identity
ZTNA
Device posture
Cloud
On-prem
Strength
Weakness
Target
```

### Market

TV2:

- Tìm tối thiểu 2 báo cáo thị trường.
- Ghi năm xuất bản.
- Ghi market size.
- Ghi CAGR.
- Không trộn số liệu.
- Phân tích lý do thị trường tăng.

### Lab

TV2:

- Tạo VM2.
- Đặt IP.
- Cài SSH.
- Tạo private-web.
- Chạy baseline port 8080.
- Cung cấp bằng chứng Nmap trước Zero Trust.
- Chuyển app sang 127.0.0.1:8080.
- Cài ziti-edge-tunnel.
- Enroll server-host.
- Xác nhận server-host bind được service.
- Đảm bảo port 8080 không còn public.

### Deliverables TV2

```text
docs/04-vendor-comparison.md
docs/05-market-analysis.md
docs/06-advantages-disadvantages.md

web/index.html
server/server-setup.md

screenshots/server/
results/baseline/
```

### Điều kiện nghiệm thu TV2

- Web chạy thành công ở baseline.
- VM3 direct curl được baseline.
- Nmap thấy 8080 ở baseline.
- Sau Zero Trust app chỉ listen 127.0.0.1.
- Nmap không thấy 8080 open.
- Server tunneler hoạt động.
- Alice vẫn truy cập app thông qua OpenZiti.

---

# 13.3. TV3 – OPENZITI CLIENT + SECURITY TESTING & EVALUATION LEAD

## Trách nhiệm chính

TV3 chịu trách nhiệm:

1. OpenZiti mechanism.
2. Client identities.
3. Security test.
4. Nmap.
5. Traffic capture.
6. Latency.
7. Kết quả thực nghiệm.
8. Demo script.

## Research

TV3 viết:

- OpenZiti architecture.
- Overlay network.
- Identity.
- Certificate.
- Enrollment.
- Service.
- intercept.v1.
- host.v1.
- Dial Policy.
- Bind Policy.
- mTLS.
- Service hiding.

### Lab

TV3:

- Tạo VM3.
- Cấu hình IP.
- Install nmap.
- Install tcpdump.
- Install ziti-edge-tunnel.
- Enroll Alice.
- Enroll Bob.
- Test Alice.
- Test Bob.
- Test direct access.
- Test Nmap.
- Test policy delete/recreate.
- Capture traffic.
- Đo latency 20 lần.
- Tổng hợp bảng kết quả.

### Deliverables TV3

```text
docs/07-openziti.md
docs/08-experiment-methodology.md
docs/09-results.md
docs/10-discussion.md

test/test-cases.md
test/commands.md

results/nmap/
results/latency/
results/traffic/

screenshots/client/
demo/demo-script.md
```

### Điều kiện nghiệm thu TV3

Phải có đủ bằng chứng:

1. Baseline Nmap.
2. Zero Trust Nmap.
3. Alice success.
4. Bob fail.
5. Direct IP fail.
6. Policy removed → Alice fail.
7. Policy restored → Alice success.
8. Latency result.
9. Traffic capture.

---

# 13.4. Phần bắt buộc làm chung

Không được chia kiểu:

> “TV1 viết report, TV2 làm demo, TV3 làm slide”.

Cả 3 phải hiểu demo.

## Integration Day

Cả nhóm phải cùng thực hiện một buổi:

```text
VM1 + VM2 + VM3
```

Test từ đầu đến cuối.

## Report Review

- TV1 review chương của TV2.
- TV2 review chương của TV3.
- TV3 review chương của TV1.

## Demo

Cả 3 phải tự thực hiện được:

```text
ziti edge list identities
ziti edge list services
ziti edge list service-policies
nmap
curl
```

---

# 14. WORK BREAKDOWN STRUCTURE – WBS

| ID | Task | Owner | Support | Output | Acceptance |
|---|---|---|---|---|---|
| W01 | Chốt tên đề tài | TV1 | TV2,TV3 | proposal | Cả nhóm đồng ý |
| W02 | Xác định RQ | TV1 | TV3 | RQ1-RQ7 | Có 7 RQ |
| W03 | Xác định scope | TV1 | TV2 | scope | Không quá rộng |
| W04 | Tạo Git repo | TV3 | TV1 | repo | Cả nhóm clone được |
| W05 | NIST research | TV1 | TV3 | chapter 2-3 | Có citation |
| W06 | VPN vs ZTNA | TV1 | TV2 | comparison | Có bảng |
| W07 | Vendor Microsoft | TV2 | - | notes | Có official source |
| W08 | Vendor Zscaler | TV2 | - | notes | Có official source |
| W09 | Vendor Cloudflare | TV2 | - | notes | Có official source |
| W10 | Vendor Cisco | TV2 | - | notes | Có official source |
| W11 | Vendor Palo Alto | TV2 | - | notes | Có official source |
| W12 | Vendor Fortinet | TV2 | - | notes | Có official source |
| W13 | Market research | TV2 | TV1 | market table | >=2 sources |
| W14 | OpenZiti architecture | TV3 | TV1 | chapter 7 | Có diagram |
| W15 | Tạo 3 VM | TV1 | TV2,TV3 | VM | Ping được |
| W16 | IP plan | TV1 | TV3 | table | IP ổn định |
| W17 | Baseline web | TV2 | TV3 | web server | Curl success |
| W18 | Baseline nmap | TV3 | TV2 | screenshot | 8080 open |
| W19 | OpenZiti install | TV1 | TV3 | controller/router | Online |
| W20 | Create identities | TV1 | TV3 | 3 identities | List OK |
| W21 | Create configs | TV1 | TV2 | configs | List OK |
| W22 | Create service | TV1 | TV2 | private-web | List OK |
| W23 | Create Bind Policy | TV1 | TV2 | policy | server-host bind |
| W24 | Create Dial Policy | TV1 | TV3 | policy | Alice dial |
| W25 | Server tunneler | TV2 | TV1 | enrolled host | Active |
| W26 | Private localhost web | TV2 | TV3 | 127.0.0.1 | No public port |
| W27 | Client tunneler | TV3 | TV1 | enrolled clients | Alice/Bob ready |
| W28 | Alice test | TV3 | TV1 | screenshot | Success |
| W29 | Bob test | TV3 | TV1 | screenshot | Denied |
| W30 | Direct IP test | TV3 | TV2 | screenshot | Fail |
| W31 | Zero Trust nmap | TV3 | TV2 | screenshot | 8080 not open |
| W32 | Policy revoke test | TV3 | TV1 | result | Access removed |
| W33 | Traffic capture | TV3 | TV1 | pcap/screenshot | No direct HTTP |
| W34 | Latency baseline | TV3 | TV2 | txt | 20 samples |
| W35 | Latency Ziti | TV3 | TV1 | txt | 20 samples |
| W36 | Result analysis | TV3 | TV1,TV2 | table | Có discussion |
| W37 | Architecture diagram | TV1 | TV3 | drawio/png | Final |
| W38 | Report merge | TV1 | TV2,TV3 | report | No duplicate |
| W39 | Slide | TV2 | TV1,TV3 | ppt outline | 18–22 slide |
| W40 | Demo script | TV3 | TV1,TV2 | script | <=8 phút |
| W41 | Backup video | TV3 | TV2 | mp4 | Demo đầy đủ |
| W42 | Final rehearsal | TV1 | TV2,TV3 | checklist | 3 người trả lời được |

---

# 15. TIMELINE 6 TUẦN

# Tuần 1 – Proposal và Research Foundation

## TV1

- Chốt đề tài.
- Viết mục tiêu.
- Viết RQ.
- NIST SP 800-207.
- Traditional vs Zero Trust.

## TV2

- Microsoft.
- Zscaler.
- Cloudflare.
- Thu thập market sources.

## TV3

- OpenZiti concepts.
- Tạo Git repo.
- Nghiên cứu identity/service/policy.

## Milestone cuối tuần

```text
M1: Đề cương được hoàn thành.
```

Deliverable:

```text
proposal.md
research-notes/
```

---

# Tuần 2 – Architecture + Technology Survey + Lab Preparation

## TV1

- PE/PA/PEP.
- NIST diagram.
- Tạo VM1.

## TV2

- Cisco.
- Palo Alto.
- Fortinet.
- Market comparison.
- Tạo VM2.

## TV3

- OpenZiti architecture.
- Test methodology.
- Tạo VM3.

## Công việc chung

- Host-only network.
- IP plan.
- Ping.
- SSH.

## Milestone

```text
M2: 3 VM kết nối được + hoàn thành khoảng 60% lý thuyết.
```

---

# Tuần 3 – Traditional Baseline + OpenZiti Infrastructure

## TV1

- Install OpenZiti.
- Controller.
- Router.
- Identities.

## TV2

- Tạo web app.
- Baseline public 8080.
- Screenshot.

## TV3

- Nmap baseline.
- Test direct curl.
- Chuẩn bị tunneler.

## Milestone

```text
M3: Controller/Router online + Baseline experiment hoàn thành.
```

---

# Tuần 4 – Zero Trust Service

## TV1

- intercept.v1.
- host.v1.
- Service.
- Bind/Dial policy.

## TV2

- Install server tunneler.
- Enroll server-host.
- Bind app về localhost.

## TV3

- Install client tunneler.
- Enroll Alice.
- Enroll Bob.

## Integration

- Alice success.
- Bob fail.
- Direct IP fail.

## Milestone

```text
M4: Demo Zero Trust cơ bản chạy end-to-end.
```

---

# Tuần 5 – Security Testing & Evaluation

## TV1

- Policy advisor.
- Review logs.
- Architecture update.

## TV2

- Review server exposure.
- So sánh attack surface.
- Hoàn thiện vendor/market chapter.

## TV3

- Nmap.
- Policy revoke.
- Tcpdump/Wireshark.
- Latency.
- Result table.

## Milestone

```text
M5: Có toàn bộ bằng chứng thực nghiệm.
```

---

# Tuần 6 – Report, Slide, Demo Rehearsal

## TV1

- Merge report.
- Review terminology.
- Architecture slides.

## TV2

- Vendor slides.
- Market slides.
- Advantages/disadvantages slides.

## TV3

- Experiment slides.
- Result slides.
- Demo script.
- Backup video.

## Cả nhóm

- Rehearsal.
- Test VM snapshots.
- Backup configs.
- Q&A.

## Milestone

```text
M6: Sẵn sàng nộp và bảo vệ.
```

---

# 16. CẤU TRÚC BÁO CÁO CUỐI KỲ

# Chương 1 – Giới thiệu

- Bối cảnh.
- Vấn đề.
- Lý do chọn đề tài.
- Mục tiêu.
- RQ.
- Scope.
- Phương pháp.

# Chương 2 – Cơ sở lý thuyết

- Traditional network security.
- Zero Trust.
- Principles.
- NIST tenets.
- VPN vs ZTNA.

# Chương 3 – Kiến trúc Zero Trust

- PE.
- PA.
- PEP.
- Control plane.
- Data plane.
- Identity.
- Resource.
- Policy.

# Chương 4 – Công nghệ Zero Trust

- Microsoft.
- Zscaler.
- Cloudflare.
- Palo Alto.
- Cisco.
- Fortinet.

# Chương 5 – Thị trường, ưu điểm và hạn chế

- Market.
- Drivers.
- Advantages.
- Challenges.
- Use cases.

# Chương 6 – OpenZiti

- Architecture.
- Controller.
- Router.
- Identity.
- Service.
- Bind.
- Dial.
- Certificate.
- Overlay.

# Chương 7 – Thiết kế thực nghiệm

- Topology.
- VM.
- IP.
- Test cases.
- Metrics.

# Chương 8 – Triển khai

- Baseline.
- Controller.
- Identity.
- Service.
- Policy.
- Tunneler.

# Chương 9 – Kết quả

- Alice.
- Bob.
- Nmap.
- Direct access.
- Policy change.
- Traffic.
- Latency.

# Chương 10 – Thảo luận

- Zero Trust có đạt mục tiêu không?
- Trade-off.
- Hạn chế lab.
- Khả năng áp dụng thực tế.

# Chương 11 – Kết luận

- Kết quả.
- Bài học.
- Hướng phát triển.

---

# 17. CẤU TRÚC SLIDE

Khoảng 18–22 slide.

| Slide | Nội dung | Người trình bày |
|---:|---|---|
| 1 | Tên đề tài | TV1 |
| 2 | Bối cảnh | TV1 |
| 3 | Vấn đề perimeter/VPN | TV1 |
| 4 | Zero Trust definition | TV1 |
| 5 | Principles | TV1 |
| 6 | NIST architecture | TV1 |
| 7 | PE/PA/PEP | TV1 |
| 8 | Traditional vs ZTNA | TV1 |
| 9 | Vendor landscape | TV2 |
| 10 | Vendor comparison | TV2 |
| 11 | Market | TV2 |
| 12 | Advantages | TV2 |
| 13 | Limitations | TV2 |
| 14 | Why OpenZiti | TV3 |
| 15 | OpenZiti architecture | TV3 |
| 16 | Lab topology | TV3 |
| 17 | Policy model | TV3 |
| 18 | Experiment | TV3 |
| 19 | Results | TV3 |
| 20 | Discussion | TV1 |
| 21 | Conclusion | TV1 |
| 22 | Q&A | Cả nhóm |

---

# 18. KỊCH BẢN BẢO VỆ VÀ DEMO

Demo không nên kéo dài quá lâu.

## Demo 1 – Baseline evidence

Show screenshot:

```text
8080 OPEN
curl direct SUCCESS
```

Không cần chạy lại baseline live nếu sợ mất thời gian.

## Demo 2 – Server hiện tại

VM2:

```bash
ss -lntp | grep 8080
```

Show:

```text
127.0.0.1:8080
```

## Demo 3 – Nmap

VM3:

```bash
nmap -sV -p 8080 192.168.56.20
```

Show:

```text
Not open
```

## Demo 4 – Alice

```bash
sudo ziti-edge-tunnel run -i ./alice-client.json
```

Terminal khác:

```bash
curl http://private-web.ziti
```

Show SUCCESS.

## Demo 5 – Bob

Stop Alice.

```bash
sudo ziti-edge-tunnel run -i ./bob-client.json
```

```bash
curl http://private-web.ziti
```

Show FAIL.

## Demo 6 – Policy

VM1:

```bash
ziti edge policy-advisor services private-web -q
```

Giải thích:

```text
Alice = Dial
Server = Bind
Bob = không Dial
```

## Câu kết demo

> Private Web không mở port trực tiếp cho client. Việc Alice truy cập được không dựa vào vị trí mạng hoặc IP của Alice, mà dựa vào OpenZiti identity và Dial Policy. Bob có identity hợp lệ nhưng không được policy cho phép nên vẫn không truy cập được.

---

# 19. DELIVERABLE CUỐI CÙNG

Nhóm phải có:

```text
01_Report.pdf
02_Report.docx hoặc .md
03_Slides.pptx
04_Demo_Guide.md
05_Source_Config.zip
06_Screenshots.zip
07_Results.zip
08_Backup_Demo.mp4
```

Repository:

```text
zero-trust-openziti/
│
├── README.md
│
├── docs/
│   ├── 01-introduction.md
│   ├── 02-zero-trust-fundamentals.md
│   ├── 03-nist-architecture.md
│   ├── 04-vendor-comparison.md
│   ├── 05-market-analysis.md
│   ├── 06-advantages-disadvantages.md
│   ├── 07-openziti.md
│   ├── 08-experiment-methodology.md
│   ├── 09-results.md
│   └── 10-discussion.md
│
├── architecture/
│   ├── nist-zta.drawio
│   ├── openziti-lab.drawio
│   └── exported/
│
├── openziti/
│   ├── controller/
│   ├── services/
│   └── policies/
│
├── web/
│   └── index.html
│
├── test/
│   ├── test-cases.md
│   └── commands.md
│
├── results/
│   ├── nmap/
│   ├── latency/
│   └── traffic/
│
├── screenshots/
│
├── demo/
│   └── demo-script.md
│
└── slides/
```

---

# 20. LƯU Ý BẢO MẬT REPOSITORY

`.gitignore` bắt buộc có:

```gitignore
*.jwt
*.json
*.key
*.pem
*.crt
*.p12
*.pfx

.env
credentials/
secrets/
identities/
```

Lý do:

Identity JSON có thể chứa:

- Private key.
- Certificate.
- Enrollment information.

Không commit các file đó.

---

# 21. QUẢN LÝ RỦI RO

| Rủi ro | Khả năng | Ảnh hưởng | Cách xử lý |
|---|---|---|---|
| Controller không start | Trung bình | Cao | Snapshot VM |
| Router offline | Trung bình | Cao | Check advertised IP/port |
| JWT hết hạn/đã dùng | Trung bình | Trung bình | Tạo identity mới |
| DNS private-web.ziti lỗi | Trung bình | Cao | Check systemd-resolved/tunneler |
| VM mất network | Trung bình | Cao | Static IP/Host-only |
| Port 8080 vẫn public | Trung bình | Cao | Bind 127.0.0.1 |
| Demo live lỗi | Trung bình | Cao | Backup video |
| Package command thay đổi | Thấp/Trung bình | Trung bình | Dùng official docs/manual binary |
| Thành viên không hiểu phần khác | Cao | Cao | Cross-review + rehearsal |
| Báo cáo quá thiên lý thuyết | Trung bình | Cao | Có test results |
| Demo chỉ cho thấy VPN-like behavior | Trung bình | Cao | Alice/Bob policy test |

---

# 22. CHECKLIST TROUBLESHOOTING

# Controller

```bash
ziti edge list controllers
```

# Router

```bash
ziti edge list edge-routers
```

# Identity

```bash
ziti edge list identities
```

# Service

```bash
ziti edge list services
```

# Policy

```bash
ziti edge list service-policies
```

# Policy Advisor

```bash
ziti edge policy-advisor services private-web -q
```

# Server listener

```bash
ss -lntp | grep 8080
```

Phải là:

```text
127.0.0.1:8080
```

# Tunneler service

```bash
systemctl status ziti-edge-tunnel
```

# DNS

```bash
systemctl status systemd-resolved
```

Client authorized:

```bash
getent hosts private-web.ziti
```

# Network reachability

```bash
ping 192.168.56.10
```

# Router ports

```bash
nc -vz 192.168.56.10 8441
nc -vz 192.168.56.10 8442
```

Cài nc nếu thiếu:

```bash
sudo apt install -y netcat-openbsd
```

---

# 23. BẢNG KẾT QUẢ THỰC NGHIỆM MẪU

Sau khi chạy thật, thay `TBD` bằng kết quả.

| Test | Traditional | Zero Trust | Kết quả |
|---|---|---|---|
| Direct IP access | SUCCESS | FAIL | TBD |
| Port 8080 discoverable | YES | NO | TBD |
| Alice access | N/A | SUCCESS | TBD |
| Bob access | N/A | FAIL | TBD |
| Identity required | NO | YES | TBD |
| Policy required | NO | YES | TBD |
| Service hidden | NO | YES | TBD |
| Avg latency | TBD ms | TBD ms | TBD |
| Plain HTTP on client-server path | YES | NO direct path | TBD |

---

# 24. TIÊU CHÍ NGHIỆM THU ĐỒ ÁN

## Mức bắt buộc

- [ ] Định nghĩa Zero Trust chính xác.
- [ ] Có NIST architecture.
- [ ] Có PE/PA/PEP.
- [ ] Có Traditional vs Zero Trust.
- [ ] Có VPN vs ZTNA.
- [ ] Có ít nhất 6 vendor.
- [ ] Có market analysis.
- [ ] Có ưu/nhược điểm.
- [ ] OpenZiti Controller chạy.
- [ ] Router online.
- [ ] Private service chạy.
- [ ] Alice được truy cập.
- [ ] Bob bị từ chối.
- [ ] Direct IP không truy cập được.
- [ ] Có Nmap evidence.
- [ ] Có test result.
- [ ] Có report.
- [ ] Có slide.

## Mức khá

- [ ] Policy change/revoke test.
- [ ] Traffic capture.
- [ ] Latency comparison.
- [ ] Resource usage.
- [ ] Diagram đẹp.
- [ ] Demo backup.

## Mức mở rộng

- [ ] MFA.
- [ ] Keycloak/OIDC.
- [ ] Device posture.
- [ ] Additional service.
- [ ] Multi-router.
- [ ] Container/Kubernetes.

---

# 25. HƯỚNG MỞ RỘNG NẾU CÒN THỜI GIAN

## Extension 1 – Role-based access

Tạo:

```text
Alice -> web
Bob -> database
```

Mỗi identity chỉ nhìn thấy service của mình.

## Extension 2 – Nhiều service

```text
web.ziti
ssh.ziti
api.ziti
```

Policy riêng.

## Extension 3 – External Identity Provider

Có thể nghiên cứu:

```text
Keycloak
OIDC
MFA
```

Không nên làm trước khi demo core hoàn thành.

## Extension 4 – Device posture

Policy phụ thuộc:

- OS.
- Process.
- Endpoint posture.

## Extension 5 – Docker/Kubernetes

Đưa private service vào container.

---

# 26. CÂU HỎI GIẢNG VIÊN CÓ THỂ HỎI

## Zero Trust có phải sản phẩm không?

Không.

Đây là:

> Kiến trúc/chiến lược bảo mật.

OpenZiti chỉ là một công nghệ để triển khai một phần nguyên tắc Zero Trust.

## Zero Trust có nghĩa là không trust bất kỳ ai không?

Không hoàn toàn.

Ý nghĩa đúng là:

> Không có implicit trust. Trust phải được xác lập và đánh giá dựa trên chính sách.

## Zero Trust có thay firewall không?

Không.

Zero Trust có thể làm việc cùng:

- Firewall.
- IDS/IPS.
- EDR.
- IAM.
- SIEM.

## OpenZiti khác VPN thế nào?

VPN thường:

```text
User -> Network
```

Demo OpenZiti:

```text
Identity -> Specific Service
```

## Bob có certificate sao vẫn bị chặn?

Vì:

```text
Authentication != Authorization
```

Bob được xác thực là Bob nhưng không có Dial Policy tới `private-web`.

## Vì sao private-web.ziti không cần DNS thật?

OpenZiti tunneler intercept DNS/service name cho identity đã được cấp quyền.

## Vì sao bind web vào 127.0.0.1?

Để service không expose trực tiếp trên network interface.

OpenZiti host tunneler là thành phần kết nối tới service local.

---

# 27. KẾT LUẬN HƯỚNG LÀM

Đồ án không nên dừng ở:

```text
Zero Trust là gì?
Có hãng nào?
OpenZiti cài được.
```

Một đồ án hoàn chỉnh nên chứng minh:

```text
          BASELINE
Client -----------> Server:8080
          DIRECT
          OPEN PORT


              ↓


        ZERO TRUST MODEL

             Identity
                |
                v
          Authentication
                |
                v
             Policy
                |
          +-----+-----+
          |           |
       Alice         Bob
       ALLOW         DENY
          |
          v
    OpenZiti Overlay
          |
          v
 private-web.ziti
          |
          v
  127.0.0.1:8080
```

Kết quả mong muốn:

1. Service không còn public port.
2. Network location không quyết định quyền.
3. Identity hợp lệ là chưa đủ.
4. Policy quyết định service nào được sử dụng.
5. Attack surface giảm.
6. Quyền truy cập granular hơn VPN/network access truyền thống.

Đó là câu chuyện kỹ thuật xuyên suốt báo cáo, slide và demo.

---

# 28. TÀI LIỆU THAM KHẢO CHÍNH

## NIST

### NIST SP 800-207 – Zero Trust Architecture

https://csrc.nist.gov/pubs/sp/800/207/final

### NIST SP 800-207A

https://csrc.nist.gov/pubs/sp/800/207/a/final

### Planning for a Zero Trust Architecture

https://csrc.nist.gov/pubs/cswp/20/planning-for-a-zero-trust-architecture/final

---

## OpenZiti

### OpenZiti Documentation

https://openziti.io/docs/

### Local – No Docker Quickstart

https://openziti.io/docs/learn/quickstarts/network/local-no-docker

### Host OpenZiti Anywhere

https://openziti.io/docs/learn/quickstarts/network/hosted

### Quickstart Walkthrough

https://openziti.io/docs/learn/quickstarts/network/help/quickstart-walkthrough/

### Your First Service

https://openziti.io/docs/learn/quickstarts/services/ztha/

### Service Policy

https://openziti.io/docs/learn/core-concepts/security/authorization/policies/creating-service-policies/

### Identity Enrollment

https://openziti.io/docs/learn/core-concepts/identities/enrolling/

### Linux Tunneler

https://openziti.io/docs/reference/tunnelers/linux/

---

# 29. GHI CHÚ TRIỂN KHAI

OpenZiti là một dự án đang được phát triển.

Trước ngày demo chính thức:

1. Kiểm tra lại official documentation.
2. Không update version vào phút cuối.
3. Snapshot tất cả VM.
4. Export report/screenshots.
5. Quay backup video.
6. Lưu lệnh demo vào `demo-script.md`.
7. Test toàn bộ demo ít nhất 2 lần từ snapshot sạch.

---

# END OF PROJECT PLAN
