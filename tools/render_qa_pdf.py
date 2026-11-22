from pathlib import Path
import fitz

pdf = Path('.tmp/Bao_cao_tien_do_do_an_Zero_Trust_OpenZiti_QA.pdf')
out = Path('.tmp/report_pages')
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    pix.save(out / f'page-{i+1:02}.png')
print(f'pages={len(doc)}')
