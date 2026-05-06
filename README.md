# 💰 Dashboard Financeiro Pessoal — Template Open Source

Dashboard interativo single-page para análise financeira pessoal — consolida cartões de crédito, contas de utilities (energia, água), salário, patrimônio (FGTS, previdência, fundos) e empréstimos em uma única página HTML autocontida.

> 🎭 **[Abra `demo.html`](demo.html) para ver o dashboard funcionando** — sem build, sem instalação, basta um navegador.

---

## ✨ Destaques

- 📊 **Single-file** — HTML + CSS + JS vanilla; sem framework, sem bundler, sem CDN além de Google Fonts
- 🗂️ **2 abas:** Fluxo de Caixa (8 capítulos com storytelling) + Patrimônio & Dívidas (6 capítulos)
- 🎨 **Estética cyber:** grid de fundo, neon glow nos KPIs, gauges SVG semicirculares, sparklines inline
- 🔒 **Modo privacidade:** botão que borra todos os valores numéricos antes de compartilhar tela
- 🤖 **OCR opcional** via Tesseract + PyMuPDF para faturas em PDF baseado em imagem
- 📐 **Responsivo** (1100/900/700/600px breakpoints) + `@media print` para PDF

---

## 🚀 Como abrir

```bash
# Apenas abra no navegador:
start demo.html      # Windows
open demo.html       # macOS
xdg-open demo.html   # Linux
```

Sem build. Sem servidor. Sem `npm install`.

---

## 📁 Estrutura do projeto

```
.
├── demo.html         # 🎭 Dashboard com dados fictícios (este é o template)
├── ocr_itau.py       # Script opcional de OCR para faturas em PDF imagem
├── README.md
└── .gitignore
```

---

## 📊 O que tem dentro do dashboard

### Tab 1 — Fluxo de Caixa (8 capítulos com arco narrativo)

| # | Capítulo | Conteúdo |
|---|---|---|
| 01 | **Perfil Financeiro** | Salário bruto/líquido + acordeão de deduções |
| 02 | **O Déficit Oculto** | KPIs e bal-cards mostrando o vermelho mensal |
| 03 | **Faturas do Cartão** | Gráfico SVG de barras animado com tooltip |
| 04 | **Onde Vai o Dinheiro** | Composição por categoria + recorrentes + utilities |
| 05 | **Parcelamentos** | Lista com barra de progresso de cada parcela |
| 06 | **Projeção até Dez** | Gráfico de linha SVG + tabela mês a mês |
| 07 | **Plano de Ação** | 3 decisões priorizadas com badges de impacto |
| 08 | **Resumo Executivo** | 4 KPIs finais com sparklines |

### Tab 2 — Patrimônio & Dívidas (6 capítulos)

| # | Capítulo | Conteúdo |
|---|---|---|
| 01 | **Visão Geral** | KPIs: bruto, dívida, líquido + barra de comprometimento |
| 02 | **Composição dos Ativos** | Horizontal bars: FGTS · Previdência · Fundos |
| 03 | **Empréstimo Consignado** | Curva de amortização SVG mês a mês |
| 04 | **Limite dos Cartões** | Gauges SVG semicirculares animados |
| 05 | **Análise de Eficiência** | Tabela retorno × custo (rendimento vs juros) |
| 06 | **Projeção Patrimonial** | Linha do patrimônio líquido até dez |

---

## ✨ Tecnologias

- **HTML5 + CSS3 puro** (CSS custom properties, Grid, Flexbox)
- **JavaScript vanilla** — sem frameworks, sem bundler
- **SVG inline** para todos os gráficos (barras, linhas, gauges, sparklines)
- **IntersectionObserver** para scroll-reveal animations
- **requestAnimationFrame** para easing de números/barras
- **Google Fonts** (Inter + JetBrains Mono) — única dependência externa

### Recursos visuais

- 🎨 Tema dark com paleta neon (verde-limão · vermelho · amarelo · roxo)
- 📐 Grid de fundo sutil estilo cyberpunk (CSS `linear-gradient` em `body::before`)
- ✨ Box-shadows com neon glow nos KPI cards
- 🔒 **Modo privacidade** — toggle de classe `body.privacy-mode` aplica `filter:blur(7px)` em valores
- 📱 Totalmente responsivo
- 🖨️ `@media print` configurado para exportação em PDF (fundo branco, sombras off)

---

## 🤖 OCR de faturas (opcional)

O script `ocr_itau.py` extrai dados de faturas em PDF baseado em imagem (scans), usando:

- **PyMuPDF** (`fitz`) para renderizar PDF em PNG a 300 DPI
- **Tesseract OCR** com idioma inglês (números são universais)
- **Regex** para extrair total da fatura, limite, vencimento e pagamento mínimo

### Como usar

1. **Instale as dependências:**
   ```bash
   # Windows
   winget install --id UB-Mannheim.TesseractOCR
   pip install pymupdf

   # macOS
   brew install tesseract
   pip install pymupdf

   # Linux
   sudo apt install tesseract-ocr
   pip install pymupdf
   ```

2. **Configure os caminhos** no topo do `ocr_itau.py`:
   ```python
   PDF_DIR = Path("/caminho/para/suas/faturas")
   OUT_DIR = Path("/caminho/para/saida")
   TESS = "/caminho/para/tesseract.exe"
   ```

3. **Execute:**
   ```bash
   python ocr_itau.py
   ```

4. **Saída:** texto OCR completo + valores-chave extraídos no console

---

## 🎨 Como personalizar para os seus dados

Toda a lógica de dados está em **constantes JavaScript** no fim do `demo.html`:

```javascript
// Fluxo de caixa
const SANTANDER = [null, 7250, 7180, 6920, 4380, /* ... */];  // gastos cartão por mês
const ITAU      = [420, 380, 425, 510, 395, /* ... */];
const ENEL      = [215, 195, 142, 188, /* ... */];            // energia
const SABESP    = [100, 100, /* ... */];                      // água
const INCOME    = [11420, 28940, 6840, 6760, 6800, /* ... */];// renda mensal
const INCOME_REG = 6800;                                       // renda regular

// Patrimônio
const FGTS              = 48200.00;
const PREVIDENCIA       = 28500.00;
const FUNDOS            =  5800.00;
const PATRIMONIO_BRUTO  = 82500.00;
const LOAN_BALANCE      = 38700.00;
const LOAN_MONTHLY      =  1345.00;
const LOAN_RATE         =     0.0215;  // 2,15% ao mês
const PATRIMONIO_LIQUIDO= 43800.00;
```

Customize **cores/fontes** via CSS custom properties em `:root`:

```css
:root {
  --bg:      #09090f;
  --accent:  #c8f135;  /* verde-limão */
  --danger:  #ff5566;
  --warn:    #ffaa33;
  --ok:      #33d97b;
  --info:    #5599ff;
  --purple:  #aa77ff;
}
```

Os textos narrativos (headlines, sub-textos, plano de ação) ficam direto no HTML — basta editar o markup das `<section class="chapter">`.

---

## 🔐 Privacidade

- **Mantenha seus dados reais fora do GitHub público** — use `.gitignore` para excluir
- O botão **🔒 Privacidade** dentro do dashboard borra valores numéricos para screensharing
- Se for usar com seus dados, considere **repositório privado** ou um fork local sem push

---

## 📜 Licença

MIT — código livre para reutilização e modificação.
Consulte `LICENSE` (se ausente, assuma MIT).
