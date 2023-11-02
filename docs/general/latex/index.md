---
icon: material/text
---

# LaTeX

General notes about LaTeX and its usage with a focus for a thesis.

**Where to write `LaTeX`?**

-   [Overleaf](https://www.overleaf.com/): Online LaTeX editor
-   [TeX Live](https://www.tug.org/texlive/): LaTeX distribution for Linux, Mac OS X, Windows (preferred)

## Folder structure

The following folder structure is recommended:

```text
thesis
├── chapters
│   ├── 01_<name>.tex
│   ├── ...
│   └── nn_<name>.tex
│── figures
├── appendix.tex
├── bibliography.bib
│── main.tex
└── ...
```

## `main.tex` Structure

```latex
\documentclass[twoside]{report}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage[skip=10pt, indent=0pt]{parskip}
\usepackage{graphicx}
\usepackage{minted}

\newgeometry{
    a4paper,
    top=2.5cm,
    bottom=2.5cm,
    inner=2.5cm,
    outer=2.5cm
}


\title{
    Thesis title\\
    {\large Thesis subtitle}
}
\author{Author name}
\date{Month Year}

\begin{document}

\maketitle

\chapter*{Abstract}

Abstract text

\chapter*{Acknowledgements}

Acknowledgements text

\tableofcontents
\listoffigures

\include{chapters/01_<name>}
\include{chapters/...}
\include{chapters/nn_<name>}

\appendix
\include{appendix}

\bibliographystyle{IEEEtrans}
\bibliography{bibliography}

\end{document}
```

-   `\documentclass[twoside]{report}`: Document class with two-sided printing (this switches margins on odd and even pages)
-   `\usepackage[utf8]{inputenc}`: UTF-8 encoding
-   `\usepackage{geometry}`: Geometry package for page layout
-   `\usepackage[skip=20pt, indent=0pt]{parskip}`: Paragraph package for paragraph spacing
    -   `skip=10pt`: Vertical space between paragraphs
    -   `indent=0pt`: Indentation of paragraphs
-   `\usepackage{graphicx}`: Graphics package for figures

## `chapter.tex` Structure

```latex
\chapter{Chapter title}

\section{Section title}
\subsection{Subsection title}
```
