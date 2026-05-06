"""OCR de faturas de cartão de crédito em PDF (imagem) — extrai valores-chave.

Pipeline:
  PDF  →  PyMuPDF (render 300 DPI)  →  PNG  →  Tesseract OCR  →  texto + regex

Uso:
  1. Edite as constantes PDF_DIR / OUT_DIR / TESS abaixo
  2. python ocr_itau.py

Saída:
  - <stem>_pageN.png          imagens renderizadas
  - <stem>_pageN.txt          texto OCR por página
  - <stem>_FULL.txt           texto combinado de todas as páginas
  - console: total, limite, vencimento, pagamento mínimo extraídos via regex
"""
import fitz, subprocess, re
from pathlib import Path

# ─── CONFIG (edite estes caminhos) ───────────────────────────────────────────
PDF_DIR = Path("./pdfs")           # pasta com os PDFs das faturas
OUT_DIR = Path("./ocr_output")     # pasta de saída (criada automaticamente)
TESS    = "tesseract"              # caminho do executável Tesseract
DPI     = 300                      # qualidade de renderização (200-400)
LANG    = "eng"                    # idioma OCR (números são universais)
# ─────────────────────────────────────────────────────────────────────────────

OUT_DIR.mkdir(exist_ok=True)
results = {}

for pdf_path in sorted(PDF_DIR.glob("*.pdf")):
    print(f"\n{'='*70}\n[PDF] {pdf_path.name}\n{'='*70}")
    doc = fitz.open(pdf_path)
    full_text = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=DPI)
        img_path = OUT_DIR / f"{pdf_path.stem}_page{i+1}.png"
        pix.save(img_path)
        txt_path = OUT_DIR / f"{pdf_path.stem}_page{i+1}"
        cmd = [TESS, str(img_path), str(txt_path), "-l", LANG, "--psm", "6"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        text_file = txt_path.with_suffix(".txt")
        if text_file.exists():
            t = text_file.read_text(encoding="utf-8", errors="ignore")
            full_text.append(f"--- PAGE {i+1} ---\n{t}")
            print(f"  page {i+1}: {len(t)} chars")
        else:
            print(f"  page {i+1}: FAILED — {r.stderr[:200]}")
    doc.close()
    combined = "\n\n".join(full_text)
    (OUT_DIR / f"{pdf_path.stem}_FULL.txt").write_text(combined, encoding="utf-8")
    results[pdf_path.name] = combined

# ─── Extração via regex ─────────────────────────────────────────────────────
print(f"\n{'='*70}\nVALORES EXTRAÍDOS\n{'='*70}")
patterns = {
    "total_fatura":      [r"total[^0-9]{0,30}da\s+fatura[^0-9]{0,15}(?:R\$\s*)?([\d\.]+,\d{2})",
                          r"total\s+a\s+pagar[^0-9]{0,15}(?:R\$\s*)?([\d\.]+,\d{2})"],
    "limite_total":      [r"limite[^0-9]{0,30}total[^0-9]{0,15}(?:R\$\s*)?([\d\.]+,\d{2})",
                          r"limite\s+do\s+cart[aã]o[^0-9]{0,15}([\d\.]+,\d{2})"],
    "limite_disponivel": [r"limite\s+dispon[ií]vel[^0-9]{0,15}([\d\.]+,\d{2})"],
    "vencimento":        [r"vencimento[^0-9]{0,15}(\d{2}/\d{2}/\d{4})"],
    "pagamento_minimo":  [r"pagamento\s+m[ií]nimo[^0-9]{0,15}([\d\.]+,\d{2})"],
}
for name, txt in results.items():
    print(f"\n[{name}]")
    txt_low = txt.lower()
    for key, pats in patterns.items():
        found = None
        for pat in pats:
            m = re.search(pat, txt_low, re.I)
            if m:
                found = m.group(1)
                break
        print(f"   {key:22s} = {found or '???'}")

print(f"\nArquivos salvos em: {OUT_DIR.resolve()}")
