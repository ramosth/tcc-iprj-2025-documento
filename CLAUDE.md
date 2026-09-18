# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX academic thesis (TCC) for a Computer Engineering Bachelor's degree at IPRJ/UERJ. The thesis proposes an IoT-based tailings dam monitoring system using ESP8266 sensors integrated with a web application and meteorological data (BNDMET/INMET). The companion software system lives in a separate repository: [sistema-bndmet](https://github.com/ramosth/sistema-bndmet).

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

**Chapter files** (edit content here):
- [introducao.tex](introducao.tex) — Introduction
- [cap1.tex](cap1.tex) — Revisão Bibliográfica (literature review, ~1200 lines)
- [cap2.tex](cap2.tex) — Fundamentação Teórica
- [cap3.tex](cap3.tex) — Material e Métodos (hardware + software implementation)
- [cap4.tex](cap4.tex) — Resultados e Discussão *(stub — in development)*
- [cap5.tex](cap5.tex) — Conclusão *(stub — in development)*

**Front matter files**: `capa.tex`, `folhaderosto.tex`, `folhaaprovacao.tex`, `catalogacao.tex`, `dedicatoria.tex`, `agradecimentos.tex`, `epigrafe.tex`, `resumo.tex`, `abstract.tex`, `siglas.tex`, `simbolos.tex`

**Figures**: all images go in the [figures/](figures/) directory. The image path is pre-configured in `config.tex`, so use just the filename in `\includegraphics{}`.

## Key Conventions

- **Citations**: use `\cite{}` with keys from `tcc.bib`; non-cited references go in [nocite.tex](nocite.tex)
- **Cross-references**: always run a full 3-pass compilation after adding `\label{}` or `\ref{}`
- **Figures**: reference with `\autoref{fig:name}` (abnTeX2 standard)
- **ABNT formatting rules** are enforced by the `abntex2` class and `config.tex` — avoid overriding them with manual spacing or font changes
