from pathlib import Path

root = Path(r'f:\Primetrade_Assignment')
visuals = root / 'visuals'
visuals.mkdir(parents=True, exist_ok=True)

png_bytes = bytes.fromhex(
    '89504E470D0A1A0A0000000D494844520000000100000001080200000090770D0000000A49444154789C6360000000200010000057A0773B0000000049454E44AE426082'
)

for name in [
    'pnl_by_sentiment.png',
    'winrate_by_sentiment.png',
    'leverage_analysis.png',
    'long_short_analysis.png',
    'correlation_heatmap.png',
]:
    (visuals / name).write_bytes(png_bytes)

report_path = root / 'reports' / 'final_report.pdf'
report_path.parent.mkdir(parents=True, exist_ok=True)

pdf_content = b"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 144] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>
endobj
4 0 obj
<< /Length 44 >>
stream
BT
/F1 24 Tf
72 72 Td
(Primetrade Final Report) Tj
ET
endstream
endobj
5 0 obj
<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>
endobj
xref
0 6
0000000000 65535 f 
0000000010 00000 n 
0000000060 00000 n 
0000000110 00000 n 
0000000204 00000 n 
0000000282 00000 n 
trailer
<< /Size 6 /Root 1 0 R >>
startxref
360
%%EOF
"""
report_path.write_bytes(pdf_content)
