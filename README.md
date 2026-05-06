# 📊 Relatório Financeiro: Visibilidade e Governança Pessoal

Como economista e analista de governança, minha rotina envolve criar visibilidade para indicadores de custos corporativos, CAPEX/OPEX e *forecast*. Este projeto nasce da aplicação direta desses princípios de controladoria na **gestão financeira pessoal**.

O **Dashboard Financeiro** é uma ferramenta *single-page* e autocontida que consolida o fluxo de caixa (cartões, utilities, salário) e o balanço patrimonial (ativos, fundos, dívidas) em uma visão executiva clara, rápida e focada em tomada de decisão.

> 🎭 [Acesse o Dashboard Interativo](https://paulohscp.github.io/relatoriofinanceiro/) para ver o projeto em funcionamento direto no navegador.

---

### 🧠 A Regra de Negócio (Por que foi criado?)
A maior dor da gestão financeira não é a falta de dados, é a **fragmentação**. Bancos, corretoras e contas de consumo vivem em silos. Este dashboard resolve isso aplicando conceitos de governança:
1. **Consolidação de Passivos (Fluxo de Caixa):** Visão clara do "déficit oculto", mapeando gastos recorrentes, faturas de cartão de crédito e contas de consumo (energia, água).
2. **Auditoria de Ativos (Patrimônio e Dívidas):** Acompanhamento da curva de amortização de empréstimos contra a evolução de ativos (FGTS, Previdência, Fundos).
3. **Plano de Ação Executivo:** Geração automática de decisões priorizadas com base no impacto financeiro projetado.

---

### ⚙️ Arquitetura e Engenharia da Solução

Para garantir eficiência, segurança e facilidade de manutenção, o projeto foi construído com duas frentes:

**1. Frontend: Alta Performance e Zero Dependências**
- **Single-file Architecture:** Construído inteiramente em HTML5, CSS3 e JavaScript Vanilla. Sem frameworks, sem *bundlers*.
- **Visualização de Dados:** Gráficos (barras, linhas, *gauges*) renderizados via SVG *inline* de forma nativa, garantindo leveza.
- **Segurança da Informação:** Botão de **Modo Privacidade** integrado, que aplica filtros para borrar valores numéricos imediatamente em casos de compartilhamento de tela.

**2. Backend/Automação: Extração de Dados via IA (OCR)**
Para evitar trabalho manual, o projeto conta com um script em Python (`ocr_itau.py`) que atua como um robô de extração de faturas.
- Utiliza **PyMuPDF** para processamento de imagens e **Tesseract OCR** para reconhecimento ótico de caracteres.
- Extrai automaticamente métricas-chave (total da fatura, vencimento e pagamento mínimo) direto dos PDFs bancários.

---

### 🚀 Como Utilizar

A filosofia do projeto é "plug and play". Não há necessidade de servidores ou comandos complexos como `npm install`.

**Para visualizar o dashboard:**
```bash
# Execute no seu terminal ou apenas dê um duplo clique no arquivo:
start demo.html      # Windows
open demo.html       # macOS
xdg-open demo.html   # Linux
