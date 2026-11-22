from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Bao_cao_tien_do_do_an_Zero_Trust_OpenZiti.docx"

NAVY = "17365D"
BLUE = "D9EAF7"
PALE = "F3F7FA"
GRID = "D9D9D9"

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:fill'), fill); tcPr.append(shd)

def borders(table):
    tblPr = table._tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        el = OxmlElement(f'w:{edge}'); el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'6'); el.set(qn('w:color'),GRID); b.append(el)
    tblPr.append(b)

def set_cell(cell, text, bold=False, color=None, size=9.4):
    cell.text = ''
    p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(2); p.paragraph_format.space_before = Pt(2)
    r = p.add_run(text); r.bold = bold; r.font.size = Pt(size); r.font.name = 'Aptos'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), 'Aptos')
    if color: r.font.color.rgb = RGBColor.from_string(color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

def table(doc, headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers)); t.alignment = WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'; borders(t)
    # Repeat the header when a table continues on a following page.
    header_pr = t.rows[0]._tr.get_or_add_trPr()
    repeat = OxmlElement('w:tblHeader'); repeat.set(qn('w:val'), 'true'); header_pr.append(repeat)
    for i,h in enumerate(headers):
        set_cell(t.rows[0].cells[i], h, True, 'FFFFFF'); shade(t.rows[0].cells[i], NAVY)
        if widths: t.rows[0].cells[i].width = Inches(widths[i])
    for idx,row in enumerate(rows):
        new_row = t.add_row()
        # Keep each record intact when a table crosses a page boundary.
        row_pr = new_row._tr.get_or_add_trPr()
        cant_split = OxmlElement('w:cantSplit'); row_pr.append(cant_split)
        cells=new_row.cells
        for i,val in enumerate(row):
            set_cell(cells[i], str(val))
            if idx % 2 == 1: shade(cells[i], PALE)
            if widths: cells[i].width=Inches(widths[i])
    doc.add_paragraph().paragraph_format.space_after=Pt(2)
    return t

def add_bullet(doc, text, level=0):
    p=doc.add_paragraph(style='List Bullet' if level==0 else 'List Bullet 2')
    p.paragraph_format.space_after=Pt(2); p.add_run(text)
    return p

def heading(doc, text, level=1):
    p=doc.add_heading(text, level=level); p.paragraph_format.space_before=Pt(13 if level==1 else 8); p.paragraph_format.space_after=Pt(5)
    for r in p.runs:
        r.font.color.rgb=RGBColor(0,0,0); r.font.name='Aptos Display'
    return p

def para(doc, text, boldlead=None):
    p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(5); p.paragraph_format.line_spacing=1.15
    if boldlead and text.startswith(boldlead):
        p.add_run(boldlead).bold=True; p.add_run(text[len(boldlead):])
    else: p.add_run(text)
    return p

def add_page_number(paragraph):
    paragraph.alignment=WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run('Trang ')
    fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); paragraph._p.append(fld)

def main():
    d=Document()
    sec=d.sections[0]; sec.top_margin=Inches(.7); sec.bottom_margin=Inches(.65); sec.left_margin=Inches(.78); sec.right_margin=Inches(.78)
    normal=d.styles['Normal']; normal.font.name='Aptos'; normal._element.rPr.rFonts.set(qn('w:eastAsia'),'Aptos'); normal.font.size=Pt(10.5)
    for n,size in [('Title',23),('Heading 1',15),('Heading 2',12)]:
        s=d.styles[n]; s.font.name='Aptos Display'; s._element.rPr.rFonts.set(qn('w:eastAsia'),'Aptos Display'); s.font.size=Pt(size); s.font.color.rgb=RGBColor(0,0,0)
    # Header/footer
    hp=sec.header.paragraphs[0]; hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT; r=hp.add_run('ĐỒ ÁN AN TOÀN MẠNG | ZERO TRUST VÀ OPENZITI'); r.font.size=Pt(8); r.font.color.rgb=RGBColor(89,89,89)
    add_page_number(sec.footer.paragraphs[0])
    # Cover
    for _ in range(5): d.add_paragraph()
    p=d.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run('BÁO CÁO TIẾN ĐỘ ĐỒ ÁN'); r.bold=True; r.font.size=Pt(16); r.font.color.rgb=RGBColor.from_string(NAVY)
    p=d.add_paragraph(style='Title'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run('Nghiên cứu kiến trúc Zero Trust và triển khai thử nghiệm Zero Trust Network Access bằng OpenZiti')
    p=d.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run('Môn học: An toàn mạng'); r.font.size=Pt(13)
    d.add_paragraph()
    table(d, ['Thông tin', 'Nội dung'], [
        ('Loại đồ án','Nghiên cứu kết hợp triển khai thực nghiệm'),
        ('Giải pháp demo','OpenZiti cho truy cập ứng dụng nội bộ theo mô hình ZTNA'),
        ('Quy mô nhóm','03 thành viên'),
        ('Môi trường dự kiến','03 máy ảo Ubuntu 22.04 LTS'),
        ('Thời lượng kế hoạch','06 tuần'),
        ('Ngày lập báo cáo','28/10/2026')], [1.75,4.65])
    d.add_paragraph()
    para(d,'Báo cáo này tổng hợp hiện trạng chuẩn bị của đồ án, thiết kế kỹ thuật, kế hoạch triển khai, tiêu chí kiểm chứng và các công việc tiếp theo. Các chỉ số thực nghiệm được ghi rõ là cần cập nhật sau khi nhóm chạy lab; báo cáo không thay thế kết quả đo thực tế.')
    d.add_page_break()

    heading(d,'Tóm tắt điều hành')
    para(d,'Đồ án hướng đến việc chứng minh rằng quyền truy cập vào ứng dụng nội bộ không nên được quyết định chỉ bởi vị trí mạng hoặc việc đã kết nối VPN. Thay vào đó, người dùng được xác thực bằng identity và chỉ được cấp quyền tới đúng service theo policy. OpenZiti được chọn để xây dựng lớp overlay bảo mật cho một web application nội bộ.')
    para(d,'Kế hoạch hiện đã xác định rõ đề tài, câu hỏi nghiên cứu, kiến trúc lab ba máy ảo, kịch bản baseline và kịch bản Zero Trust, WBS 42 đầu việc, tiêu chí nghiệm thu và phân công ba vai trò. Mốc kỹ thuật quan trọng nhất là hoàn tất chuỗi chứng minh: Alice truy cập thành công, Bob có identity nhưng không có quyền bị từ chối, truy cập trực tiếp theo IP thất bại và cổng 8080 không còn bị lộ ra mạng.')
    heading(d,'1. Thông tin và mục tiêu đồ án')
    heading(d,'1.1 Bối cảnh và vấn đề',2)
    para(d,'Mô hình bảo vệ biên truyền thống thường coi mạng nội bộ là vùng đáng tin cậy hơn mạng bên ngoài. Khi một tài khoản VPN hoặc thiết bị đã vào mạng, phạm vi nhìn thấy và khả năng di chuyển ngang có thể tăng đáng kể. Trong bối cảnh làm việc từ xa, BYOD, cloud và tấn công đánh cắp thông tin xác thực, giả định tin cậy dựa trên vị trí mạng trở nên không đủ.')
    heading(d,'1.2 Mục tiêu tổng quát',2)
    para(d,'Nghiên cứu kiến trúc Zero Trust theo định hướng NIST, phân tích các nguyên tắc và công nghệ liên quan, sau đó triển khai thử một mô hình Zero Trust Network Access cho web application nội bộ bằng OpenZiti để đánh giá truy cập dựa trên identity và policy.')
    heading(d,'1.3 Mục tiêu cụ thể',2)
    for x in ['Trình bày đúng khái niệm Zero Trust, các nguyên tắc verify explicitly, least privilege, assume breach và deny by default.','Phân tích kiến trúc NIST SP 800-207 với Policy Engine, Policy Administrator, Policy Enforcement Point, control plane và data plane.','So sánh perimeter security/VPN với ZTNA ở góc độ đối tượng cấp quyền, khả năng khám phá dịch vụ và rủi ro lateral movement.','Khảo sát các hệ sinh thái Microsoft, Zscaler, Cloudflare, Palo Alto Networks, Cisco, Fortinet và OpenZiti.','Triển khai controller, edge router, identities, service, bind policy và dial policy trong lab.','Thực hiện các kiểm thử truy cập hợp lệ, trái phép, direct IP, quét cổng, thay đổi policy, quan sát traffic và đo độ trễ.']:
        add_bullet(d,x)
    heading(d,'1.4 Câu hỏi nghiên cứu',2)
    table(d,['Mã','Câu hỏi'],[
        ('RQ1','Zero Trust Architecture là gì và vì sao cần thay đổi từ mô hình tin cậy dựa trên perimeter?'),
        ('RQ2','ZTA khác VPN/perimeter security như thế nào về đơn vị cấp quyền và bề mặt tấn công?'),
        ('RQ3','PE, PA, PEP, identity, resource và policy phối hợp như thế nào?'),
        ('RQ4','Các nhà cung cấp lớn hiện thực ZTNA/Zero Trust bằng những nhóm năng lực nào?'),
        ('RQ5','OpenZiti có đáp ứng được một lab ZTNA có thể kiểm chứng cho sinh viên không?'),
        ('RQ6','Việc chuyển web service từ public port sang overlay ảnh hưởng thế nào đến discoverability và quyền truy cập?')],[.55,5.85])
    heading(d,'2. Đối tượng, phạm vi và phương pháp')
    heading(d,'2.1 Đối tượng nghiên cứu',2)
    para(d,'Đối tượng nghiên cứu là kiến trúc Zero Trust và trường hợp áp dụng Zero Trust Network Access cho một dịch vụ web nội bộ. Đối tượng triển khai là OpenZiti Controller, Edge Router, identity của máy chủ và người dùng, service configuration, service policy và tunneler ở hai đầu kết nối.')
    table(d,['Trong phạm vi','Ngoài phạm vi'],[
        ('ZTA, ZTNA, identity-based access, PKI/certificate ứng dụng, policy dịch vụ, overlay network, port exposure, latency cơ bản và quan sát traffic.','SIEM/SOC hoàn chỉnh, EDR thương mại, DLP, Active Directory doanh nghiệp đầy đủ, HA production, Kubernetes, multi-cloud phức tạp, MFA và device posture nâng cao.')],[3.2,3.2])
    heading(d,'2.2 Phương pháp thực hiện',2)
    table(d,['Phương pháp','Cách áp dụng'],[
        ('Nghiên cứu tài liệu','Ưu tiên NIST, CISA, tài liệu chính thức của hãng và OpenZiti.'),
        ('Phân tích so sánh','So sánh network/perimeter, VPN và ZTNA theo access model, trust và exposure.'),
        ('Triển khai thực nghiệm','Dựng lab 03 VM; tạo service private và policy theo identity.'),
        ('Đánh giá','Thực hiện test case có tiêu chí pass/fail, thu thập log/screenshot/capture và số liệu latency.')],[1.45,4.95])
    heading(d,'3. Cơ sở kiến trúc và mô hình bảo mật')
    para(d,'Zero Trust không có nghĩa là không tin bất kỳ chủ thể nào. Ý nghĩa chính xác là không có implicit trust: một yêu cầu phải được xác lập, cấp phát và thực thi bằng identity, policy và ngữ cảnh. Authentication trả lời “ai đang yêu cầu”, còn authorization trả lời “identity đó được dùng service nào”.')
    table(d,['Tiêu chí','VPN/perimeter truyền thống','ZTNA theo đồ án'],[
        ('Đơn vị cấp quyền','Mạng hoặc subnet','Ứng dụng/dịch vụ cụ thể'),
        ('Cơ sở trust','Thường dựa nhiều vào kết nối vào mạng','Identity và policy'),
        ('Khả năng khám phá','Có thể thấy thêm tài nguyên nội bộ','Giảm discoverability của service không được cấp'),
        ('Least privilege','Khó duy trì khi cấp network access','Áp dụng ở mức service'),
        ('Rủi ro lateral movement','Cao hơn nếu phạm vi mạng rộng','Giảm nhờ giới hạn service và policy')],[1.2,2.55,2.65])
    heading(d,'3.1 Ánh xạ khái niệm NIST vào lab',2)
    table(d,['Thành phần','Vai trò trong lab'],[
        ('Policy Engine (PE)','Logic ra quyết định cho phép/từ chối dựa trên identity và service policy.'),
        ('Policy Administrator (PA)','Thiết lập, quản lý và thay đổi quyền truy cập; thực thi quyết định điều phối.'),
        ('Policy Enforcement Point (PEP)','Điểm thực thi lưu lượng được phép; trong lab là các thành phần OpenZiti/tunneler theo service.'),
        ('Identity','Alice, Bob và server-host có credential/identity riêng.'),
        ('Resource','Private web application đang lắng nghe trên localhost:8080.'),
        ('Policy Information','Thông tin identity, cấu hình service, bind policy và dial policy.')],[1.65,4.75])
    heading(d,'4. Kiến trúc đề xuất và thiết kế lab')
    heading(d,'4.1 Topology logic',2)
    para(d,'Lab dự kiến dùng ba máy ảo trong mạng host-only 192.168.56.0/24; mỗi máy có thêm NAT để cài đặt package. Lưu lượng ứng dụng đi qua OpenZiti overlay, không đi trực tiếp từ client đến cổng HTTP public của VM2.')
    table(d,['Máy','Địa chỉ mẫu','Thành phần chính','Vai trò'],[
        ('VM1: zt-controller','192.168.56.10','OpenZiti Controller, Edge Router, PKI, quản lý policy','Control plane và điểm trung chuyển overlay'),
        ('VM2: private-web','192.168.56.20','Web app 127.0.0.1:8080, server tunneler, server-host identity','Host service nội bộ'),
        ('VM3: zt-client','192.168.56.30','Client tunneler, Alice/Bob identities, curl, nmap, tcpdump','Thiết bị kiểm thử')],[1.3,1.2,2.4,1.5])
    heading(d,'4.2 Luồng truy cập kỳ vọng',2)
    for x in ['Alice enroll identity và kết nối tunneler tới OpenZiti overlay.','Alice yêu cầu private-web.ziti; service chỉ hiển thị khi Alice có Dial Policy phù hợp.','OpenZiti xác nhận server-host có Bind Policy để host private-web.','Tunneler phía server chuyển tiếp tới 127.0.0.1:8080; ứng dụng không cần mở cổng 8080 ra interface mạng.','Bob có identity hợp lệ nhưng không có Dial Policy; yêu cầu bị từ chối.']:
        add_bullet(d,x)
    heading(d,'4.3 Mô hình policy',2)
    table(d,['Identity','Xác thực','Quyền tới private-web','Kết quả kỳ vọng'],[
        ('server-host','Có','Bind Policy','Host service'),('Alice','Có','Dial Policy','Truy cập thành công'),('Bob','Có','Không có Dial Policy','Bị từ chối'),('Identity không hợp lệ','Không','Không','Không truy cập được')],[1.5,1.2,1.85,1.85])
    heading(d,'5. Kế hoạch triển khai và phân công')
    para(d,'Kế hoạch sáu tuần chia theo một chuỗi phụ thuộc: đề cương và lý thuyết → hạ tầng lab → baseline → dịch vụ Zero Trust → kiểm thử/bằng chứng → hoàn thiện báo cáo và bảo vệ. Một điểm kiểm soát bắt buộc là Integration Day, nơi cả ba thành viên phải chạy được luồng end-to-end.')
    table(d,['Tuần','Mục tiêu chính','Mốc đầu ra'],[
        ('1','Chốt đề tài, RQ, phạm vi, nghiên cứu nền tảng và OpenZiti concepts.','M1: hoàn thành đề cương.'),
        ('2','Hoàn thiện kiến trúc, khảo sát vendor, dựng 03 VM và IP plan.','M2: VM liên lạc được; lý thuyết khoảng 60%.'),
        ('3','Tạo web baseline public, cài controller/router, tạo identity.','M3: hạ tầng OpenZiti online và baseline hoàn tất.'),
        ('4','Tạo service/config/policy, enroll host và client tunnelers.','M4: Alice success, Bob fail, direct IP fail.'),
        ('5','Quét cổng, revoke policy, capture traffic, latency và phân tích.','M5: đủ bằng chứng thực nghiệm.'),
        ('6','Hợp nhất báo cáo, slide, demo script, backup video và rehearsal.','M6: sẵn sàng nộp/bảo vệ.')],[.55,3.8,2.05])
    table(d,['Vai trò','Trách nhiệm chính','Đầu ra'],[
        ('TV1','Điều phối kiến trúc NIST, controller/router, identity, policy và tích hợp.','NIST/ZTA, kiến trúc lab, controller/policy evidence.'),
        ('TV2','Khảo sát vendor/thị trường, web baseline, private service và host tunneler.','Vendor/market, web deployment, server evidence.'),
        ('TV3','OpenZiti client, security testing, nmap, traffic, latency, demo script.','Test cases, kết quả, screenshot/capture, demo.')],[.75,3.05,2.6])
    heading(d,'6. Tiến độ hiện tại')
    para(d,'Đánh giá dưới đây dựa trên tài liệu kế hoạch hiện có trong repository. Vì repository chưa có cấu hình triển khai, screenshot, logs, kết quả nmap, pcap hoặc dữ liệu latency, các đầu việc thực nghiệm chưa được xác nhận hoàn thành. Trạng thái “đã sẵn sàng” thể hiện đã có thiết kế/kế hoạch, không phải bằng chứng triển khai.')
    table(d,['Hạng mục','Trạng thái','Căn cứ / việc còn lại'],[
        ('Đề tài, mục tiêu, RQ và phạm vi','Đã sẵn sàng','Đã được xác định trong kế hoạch; cần chốt tên nhóm/giảng viên nếu trường yêu cầu.'),
        ('Cơ sở lý thuyết và outline report','Đã sẵn sàng','Có chương mục, chuẩn tham chiếu và nội dung cần nghiên cứu.'),
        ('Kiến trúc lab 03 VM và IP plan','Đã thiết kế','Cần dựng VM, kiểm tra ping/SSH và lưu minh chứng.'),
        ('Khảo sát vendor/thị trường','Đã lập kế hoạch','Cần thu thập nguồn chính thức, bảng so sánh và citation.'),
        ('Baseline public web','Chưa có minh chứng','Cần chạy 0.0.0.0:8080, nmap/curl và lưu kết quả.'),
        ('OpenZiti controller/router/service/policy','Chưa có minh chứng','Cần cài đặt, tạo identities/configs/service policies và export lệnh/kết quả.'),
        ('Kiểm thử Alice/Bob/direct IP/revoke','Chưa có minh chứng','Cần thực thi test case, capture terminal/screenshot và kết luận pass/fail.'),
        ('Traffic capture và latency','Chưa có minh chứng','Cần pcap/tcpdump và 20 mẫu mỗi trạng thái để tính min/max/average.'),
        ('Tài liệu, slide, rehearsal','Đang chuẩn bị','Báo cáo tiến độ này là một đầu ra; còn cần report cuối kỳ và rehearsal.')],[1.65,1.25,3.5])
    heading(d,'7. Kế hoạch kiểm thử và tiêu chí đánh giá')
    para(d,'Các thử nghiệm phải được tiến hành theo thứ tự baseline trước, Zero Trust sau để so sánh công bằng. Mỗi case cần ghi rõ thời gian, lệnh đã chạy, identity sử dụng, expected result, actual result và đường dẫn minh chứng.')
    table(d,['ID','Kịch bản','Kết quả mong đợi','Minh chứng cần lưu'],[
        ('TC01','Baseline direct curl tới 192.168.56.20:8080','Thành công khi web bind 0.0.0.0:8080.','Output curl và ss -lntp.'),
        ('TC02','Baseline nmap port 8080','Port 8080 open.','Output nmap -sV.'),
        ('TC03','Zero Trust direct IP','Thất bại sau khi web bind 127.0.0.1:8080.','curl và ss -lntp.'),
        ('TC04','Zero Trust nmap','8080 closed hoặc filtered.','Output nmap -sV.'),
        ('TC05','Alice truy cập private-web.ziti','Thành công khi có identity và Dial Policy.','Output curl, service/policy list.'),
        ('TC06','Bob truy cập private-web.ziti','Thất bại dù identity hợp lệ nhưng không có Dial Policy.','Output curl và policy advisor.'),
        ('TC07','Thu hồi quyền Alice','Alice mất quyền sau khi xóa Dial Policy; khôi phục policy thì truy cập lại.','Trước/sau policy, output curl.'),
        ('TC08','Quan sát traffic','Không có HTTP plaintext trực tiếp VM3 → VM2; thấy overlay encrypted.','pcap/tcpdump hoặc Wireshark screenshot.'),
        ('TC09','Latency','Có 20 mẫu baseline và 20 mẫu Ziti, báo cáo min/max/average.','Raw samples và bảng tổng hợp.')],[.45,1.55,2.35,2.05])
    heading(d,'8. Rủi ro, kiểm soát và chất lượng')
    table(d,['Rủi ro','Ảnh hưởng','Giảm thiểu'],[
        ('Controller/router không online hoặc advertised address sai','Cao','Snapshot VM, kiểm tra controller/router list và port reachability trước Integration Day.'),
        ('JWT enrollment hết hạn/đã dùng','Trung bình','Tạo identity mới theo quy trình chuẩn; không commit file identity hoặc khóa riêng.'),
        ('Web vẫn bind public','Cao','Xác nhận ss -lntp hiển thị 127.0.0.1:8080 trước khi demo ZTNA.'),
        ('DNS intercept/private-web.ziti lỗi','Cao','Kiểm tra tunneler, systemd-resolved và getent hosts.'),
        ('Demo live lỗi','Cao','Snapshot, export config an toàn, screenshot và video backup.'),
        ('Báo cáo chỉ thiên về lý thuyết','Cao','Mỗi nhận định kỹ thuật phải đi cùng test case và evidence thực nghiệm.'),
        ('Lộ secrets trong repo','Cao','Gitignore *.jwt, *.json, *.key, *.pem, *.crt, *.p12, *.pfx và thư mục credentials/identities.')],[1.65,1.0,3.75])
    heading(d,'9. Kế hoạch hành động tiếp theo')
    for x in ['Dựng ba VM, gán IP ổn định và kiểm tra ping/SSH; chụp lại topology thực tế.','Triển khai baseline web công khai tạm thời trên VM2, thực hiện TC01-TC02 và lưu evidence.','Cài OpenZiti Controller/Edge Router theo tài liệu phiên bản đã chốt; tạo server-host, Alice và Bob identities.','Chuyển web service về 127.0.0.1:8080; tạo host.v1/intercept.v1, service, bind policy và dial policy.','Chạy TC03-TC09, điền actual result, đính kèm hình/PCAP/latency raw data vào report cuối kỳ.','Hoàn thiện chương khảo sát vendor bằng nguồn chính thức và cập nhật tài liệu tham khảo nhất quán.','Tổ chức Integration Day và rehearsal; bảo đảm mỗi thành viên trình bày được luồng identity → policy → service.']:
        add_bullet(d,x)
    heading(d,'10. Kết luận')
    para(d,'Đồ án đã có một nền tảng kế hoạch vững chắc: vấn đề rõ ràng, kiến trúc lab khả thi, kịch bản kiểm chứng phân biệt authentication với authorization và tiêu chí nghiệm thu cụ thể. Giá trị cốt lõi cần chứng minh không phải chỉ là cài đặt OpenZiti, mà là dịch vụ web không còn phụ thuộc vào cổng public hoặc vị trí mạng để cấp quyền: Alice được phép theo policy, còn Bob bị chặn dù sở hữu identity hợp lệ.')
    para(d,'Giai đoạn tiếp theo cần ưu tiên triển khai và thu thập evidence thay vì mở rộng tính năng. Khi hoàn thành đầy đủ các test case, nhóm sẽ có đủ cơ sở để đánh giá trade-off giữa giảm attack surface, kiểm soát truy cập chi tiết và chi phí vận hành của mô hình Zero Trust.')
    heading(d,'Tài liệu tham khảo định hướng')
    for x in ['NIST SP 800-207, Zero Trust Architecture, National Institute of Standards and Technology. https://csrc.nist.gov/pubs/sp/800/207/final','NIST SP 800-207A, A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Cloud Environments. https://csrc.nist.gov/pubs/sp/800/207/a/final','CISA, Zero Trust Maturity Model. https://www.cisa.gov/zero-trust-maturity-model','OpenZiti Documentation. https://openziti.io/docs/','OpenZiti Service Policies. https://openziti.io/docs/learn/core-concepts/security/authorization/policies/creating-service-policies/']:
        add_bullet(d,x)
    # core properties
    d.core_properties.title='Báo cáo tiến độ đồ án Zero Trust và OpenZiti'; d.core_properties.subject='Báo cáo tiến độ đồ án môn An toàn mạng'; d.core_properties.author='Nhóm đồ án'; d.core_properties.comments='Tạo từ kế hoạch đồ án hiện có'
    d.save(OUT)
    print('Report created successfully')

if __name__ == '__main__': main()
