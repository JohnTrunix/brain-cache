---
icon: material/code-brackets
---

# LaTeX Elements

## Citations and Bibliography

The `bibliography.bib` file contains all the references used in the thesis. The references can be added manually or using a reference manager like. See [BibTeX](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex){target=\_blank} for more information.

```bib
@article{<label_name>,
    author  = {Author name},
    title   = {Title},
    journal = {Journal},
    year    = {Year},
    volume  = {Volume},
    number  = {Number},
    pages   = {Pages},
    doi     = {DOI}
}
```

**Citation:**

```latex
Text to cite \cite{<label_name>}.
```

## Footnotes

```latex
Text with footnote\footnote{Footnote text}.

Text with a long footnote\footnotemark. More text ...

\footnotetext{Footnote text}
```

## Figures

```latex
\usepackage{graphicx}

\begin{figure}[ht]
    \centering
    \includegraphics[width=0.5\textwidth]{figures/<name>.png}
    \caption{Caption text}
    \label{fig:<label_name>}
\end{figure}
```

**Referencing a figure:**

```latex
Figure \ref{fig:<label_name>}
```

## Tables

!!! tip

    [Online table generator](https://www.tablesgenerator.com/){target=\_blank}

```latex
\begin{table}[ht]
    \centering
    \begin{tabular}{|l|l|l|}
        \hline
        \textbf{Column 1} & \textbf{Column 2} & \textbf{Column 3} \\ \hline
        Row 1             & Row 1             & Row 1             \\ \hline
        Row 2             & Row 2             & Row 2             \\ \hline
        Row 3             & Row 3             & Row 3             \\ \hline
    \end{tabular}
    \caption{Caption text}
    \label{tab:<label_name>}
\end{table}
```

**Referencing a table:**

```latex
Table \ref{tab:<label_name>}
```

## Code

```latex
\usepackage{minted}

\begin{minted}{python}
    def function():
        print("Hello World!")
\end{minted}
```

```python
def function():
    print("Hello World!")
```
