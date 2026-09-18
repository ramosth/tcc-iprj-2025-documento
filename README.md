# A Engenharia da Computação na Prevenção de Acidentes em Barragens de Rejeitos

Trabalho de Conclusão de Curso (TCC) apresentado ao Instituto Politécnico do Rio de Janeiro (IPRJ) da Universidade do Estado do Rio de Janeiro (UERJ), como requisito para obtenção do grau de Bacharel em Engenharia da Computação.

**Autora:** Thamires Ramos dos Santos  
**Orientador:** Prof. Dr. Edgard Poiate Junior  
**Período:** 2026/1  

---

## Sobre o Trabalho

Este trabalho propõe o desenvolvimento de um sistema de monitoramento de barragens de rejeitos utilizando tecnologias de IoT (Internet das Coisas) e integração com dados meteorológicos. O sistema combina sensores de umidade do solo (ESP8266 + higrômetro resistivo) com uma aplicação web completa para visualização de dados em tempo real, análise de risco e envio de alertas.

O projeto foi motivado pelos desastres de Mariana (2015) e Brumadinho (2019), que evidenciaram a necessidade de sistemas de monitoramento mais acessíveis e automatizados para barragens de rejeitos no Brasil.

## Estrutura do Repositório

```
tcc_thamires_iprj_2025/
├── principal.tex          # Arquivo principal (compilar este)
├── config.tex             # Configurações de pacotes e formatação
├── tcc.bib                # Referências bibliográficas (ABNT)
├── capa.tex               # Capa
├── folhaderosto.tex       # Folha de rosto
├── dedicatoria.tex        # Dedicatória
├── agradecimentos.tex     # Agradecimentos
├── epigrafe.tex           # Epígrafe
├── resumo.tex             # Resumo (PT-BR)
├── abstract.tex           # Abstract (EN)
├── siglas.tex             # Lista de siglas
├── simbolos.tex           # Lista de símbolos
├── introducao.tex         # Introdução
├── cap1.tex               # Cap.1 - Revisão Bibliográfica
├── cap2.tex               # Cap.2 - Fundamentação Teórica
├── cap3.tex               # Cap.3 - Material e Métodos
├── cap4.tex               # Cap.4 - Resultados e Discussão
├── cap5.tex               # Cap.5 - Conclusão
├── apendices.tex          # Apêndices
├── catalogacao.tex        # Ficha catalográfica
├── nocite.tex             # Referências não citadas
├── figures/               # Figuras e imagens do trabalho
└── abntex2-alf.bst        # Estilo bibliográfico ABNT
```

## Tecnologias Utilizadas

**Documento:**
- LaTeX (abnTeX2) com formatação ABNT
- MiKTeX para compilação
- VS Code + LaTeX Workshop

**Sistema de Monitoramento (repositório separado: [sistema-bndmet](https://github.com/ramosth/sistema-bndmet)):**
- Hardware: ESP8266 (NodeMCU) + Sensor de umidade do solo
- Backend: Node.js, TypeScript, Express, Prisma ORM
- Frontend: Next.js, React
- Banco de dados: PostgreSQL + TimescaleDB
- Serviços: integração BNDMET/INMET, alertas por email

## Como Compilar

### Pré-requisitos
- [MiKTeX](https://miktex.org/download) (com instalação automática de pacotes habilitada)
- [VS Code](https://code.visualstudio.com/) + extensão [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

### Compilação
1. Abra a pasta do projeto no VS Code
2. Abra o arquivo `principal.tex`
3. Pressione `Ctrl+Alt+B` para compilar
4. O PDF gerado estará em `principal.pdf`

Alternativamente, via terminal:
```bash
pdflatex principal.tex
bibtex principal
pdflatex principal.tex
pdflatex principal.tex
```
(São necessárias múltiplas execuções para resolver referências cruzadas e bibliográficas.)

## Licença

Este trabalho é de uso acadêmico. Todos os direitos reservados à autora.