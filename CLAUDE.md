# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX academic thesis (TCC) for a Computer Engineering Bachelor's degree at IPRJ/UERJ. The thesis proposes an IoT-based alert system for tailings dams: soil saturation (hygrometer) + 72 h rainfall (48 h observed from BNDMET + 24 h forecast from OpenWeatherMap), three alert levels, ESP8266 prototype and ESP32 Wokwi simulation with battery backup. Software: [tcc-iprj-2025-sistema](https://github.com/ramosth/tcc-iprj-2025-sistema), branch v3-simples.

- **Language**: Portuguese (pt-BR) — all document content must be written in Portuguese
- **Standard**: ABNT formatting via the `abnTeX2` LaTeX class
- **Author**: Thamires Ramos dos Santos | **Advisor**: Prof. Dr. Edgard Poiate Junior

## Build Commands

**Full compilation (required for cross-references and bibliography):**
```bash
pdflatex principal.tex
bibtex principal
pdflatex principal.tex
pdflatex principal.tex
```

**Using latexmk (handles multiple passes automatically):**
```bash
latexmk -pdf principal.tex
```

**Using VS Code + LaTeX Workshop:** open `principal.tex` and press `Ctrl+Alt+B`.

Output is `principal.pdf`. Build artifacts (`*.aux`, `*.log`, `*.toc`, etc.) are git-ignored.

## Document Architecture

**Entry point**: [principal.tex](principal.tex) — includes all other files in order and sets the `abntex2` document class options.

**Configuration**: [config.tex](config.tex) — all package imports, font settings, page styles, section formatting, image path (`figures/`), and author/advisor metadata. Edit here when changing document-wide formatting.

**Bibliography**: [tcc.bib](tcc.bib) — ABNT-style BibTeX entries. The style file [abntex2-alf.bst](abntex2-alf.bst) must stay in the root directory.

**Chapter files** (o que o principal.tex inclui de fato; numeração real no PDF):
- [introducao.tex](introducao.tex) — Introdução (sem número; 6 parágrafos)
- [cap1.tex](cap1.tex) — Cap. 1 Revisão Bibliográfica (1.1–1.5, estrutura do orientador)
- [cap3.tex](cap3.tex) — Cap. 2 Objetivos
- [cap4.tex](cap4.tex) — Cap. 3 Material e Métodos (modelo de alerta, BNDMET/OWM, software, hardware, energia, Wokwi, testes)
- [cap5.tex](cap5.tex) — Cap. 4 Resultados (C00–C09, X01–X09, E01–E04, F01–F08, plataforma web)
- [cap6.tex](cap6.tex) — Cap. 5 Discussões
- [conclusao.tex](conclusao.tex) — Conclusões (sem número)
- NÃO compilados: cap2.tex (saiu; conteúdo útil foi para o cap1) e cap1_antigo.tex (backup).

## Estado em 05/10/2026 (varredura P15 — detalhes em Downloads/P15_varredura.txt)

- Modelo novo (limiar hidrometeorológico S x P72; S1/S2 = 0,64/0,86, Mirus 2018; P1/P2 = 60/100 mm, Mendes 2020) aplicado em todos os capítulos. Sem rastro do modelo antigo no PDF (R10).
- Energia: 3 x NCR18650B em paralelo (7816 mAh necessários; 9600 mAh), T_carga = 19,5 h; bateria só na simulação.
- Buzzer: tone 2300 Hz na simulação; TMB-12A03 ativo no físico.
- Equações (7) com origem, \label e "Cada variável..."; contas conferidas.
- Refs/labels/cites: nenhum quebrado; 132 entradas, todas citadas.
- Firmwares: projeto_tcc_wokwi/sketch_v3/sketch_v3.ino (ESP32) e Downloads/tcc_versao_21/tcc_versao_21.ino (ESP8266), constantes iguais ao texto.

## Pendências abertas (05/10/2026, depois de aplicar o P15 — IDs do Downloads/P15_varredura.txt)

Aplicados em 05/10: A1–A4, A6, A8, A10–A12, B1–B5, B7, B8, B10, B11, B13, B14, B16–B18, B21, B23, B25, B27, C1, C2 ("Autora, 2026."), C6–C9.
Compilação completa (4 passes) sem erro e sem referência indefinida; o documento passou a 158 folhas.

- A5: trocar no Google Drive o arquivo das requisições BNDMET (tem o texto "V_ch.30d / 300 mm" do modelo antigo).
- A7: firmware — branch v3-simples com o tcc_versao_21 está commitada em D:/Users/thami/Documents/github/tcc-iprj-2025-firmware, falta `git push origin v3-simples` e tornar v3-simples a branch padrão no GitHub.
- A9: buzzer 35 mA direto no GPIO (limite 12 mA) — não aplicado.
- B6 (domínio do BNDMET no .bib), B9 (fontes fracas), B12 (fonte da figura do buzzer), B15 (horários X05 x F07), B19 (parágrafos > 5 linhas), B20 (overfull), B22 (ficha catalográfica: gerar de novo com 158 f. e "Poiate Júnior, Edgard"), B24, B26 (página da Taklite), C3–C5.
- Energizer 522: conferir se a menor corrente do gráfico é 25 mA (o PDF parece começar em 10 mA).
- Orientador: diagrama de classes, palavras-chave, numeração dos capítulos, SMS/Defesa Civil.
- BNDMET como iniciativa INMET + DECEA: não confirmado.
- C8: arquivos antigos tirados do índice do git (git rm --cached) e postos no .gitignore; falta o commit.
- Downloads ainda tem temporários antigos: _teste_cap1.tgz, _teste_figs.txt, _prev_componentes/.

**Front matter files**: `capa.tex`, `folhaderosto.tex`, `folhaaprovacao.tex`, `catalogacao.tex`, `dedicatoria.tex`, `agradecimentos.tex`, `epigrafe.tex`, `resumo.tex`, `abstract.tex`, `siglas.tex`, `simbolos.tex`

**Figures**: all images go in the [figures/](figures/) directory. The image path is pre-configured in `config.tex`, so use just the filename in `\includegraphics{}`.

## Key Conventions

- **Citations**: use `\cite{}` with keys from `tcc.bib`; non-cited references go in [nocite.tex](nocite.tex)
- **Cross-references**: always run a full 3-pass compilation after adding `\label{}` or `\ref{}`
- **Figures**: reference with `\autoref{fig:name}` (abnTeX2 standard)
- **ABNT formatting rules** are enforced by the `abntex2` class and `config.tex` — avoid overriding them with manual spacing or font changes
