---
icon: material/math-integral
---

# LaTeX Math

Ressources:

-   [Mathematical expressions](https://www.overleaf.com/learn/latex/Mathematical_expressions){target=\_blank}
-   [List of mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols){target=\_blank}
-   [List of Greek letters and math symbols](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols){target=\_blank}

Often following packages are used:

```latex
\usepackage{amsmath}
\usepackage{amssymb}
```

## Inline Mode

```latex
Inline math: $x^2 + y^2 = z^2$.\\
Inline math with Greek letters: $\alpha + \beta = \gamma$.
```

> Inline math: $x^2 + y^2 = z^2$.
>
> Inline math with Greek letters: $\alpha + \beta = \gamma$.

## Display Mode

### Unnumbered equations

```latex
\[
    x^2 + y^2 = z^2
\]

\begin{equation*}
    x^2 + y^2 = z^2
\end{equation*}
```

> $$
>    x^2 + y^2 = z^2
> $$

### Numbered equations

```latex
\begin{equation}
    x^2 + y^2 = z^2
    \label{eq:<label_name>}
\end{equation}
```

> $$
> \begin{equation}
>    x^2 + y^2 = z^2 \qquad (1)
>    \label{eq:<label_name>}
> \end{equation}
> $$

!!! info

    Referencing an equation:

    ```latex
    Equation \ref{eq:<label_name>}
    ```

## Aligning Equations

### Long equations

```latex
\begin{multline*}
    p(x) = 3x^6 + 14x^5y + 590x^4y^2 + 19x^3y^3\\
    - 12x^2y^4 - 12xy^5 + 2y^6 - a^3b^3
\end{multline*}
```

> $$
> \begin{multline*}
>    p(x) = 3x^6 + 14x^5y + 590x^4y^2 + 19x^3y^3\\
>    - 12x^2y^4 - 12xy^5 + 2y^6 - a^3b^3
> \end{multline*}
> $$

### Aligning vertically

```latex
\begin{align*}
    x^2 + y^2 &= z^2\\
    x^2 &= z^2 - y^2\\
    x &= \sqrt{z^2 - y^2}
\end{align*}
```

> $$
> \begin{align*}
>    x^2 + y^2 &= z^2\\
>    x^2 &= z^2 - y^2\\
>    x &= \sqrt{z^2 - y^2}
> \end{align*}
> $$

### Centering equations

```latex
\begin{gather*}
    x^2 + y^2 = z^2\\
    x^2 = z^2 - y^2\\
    x = \sqrt{z^2 - y^2}
\end{gather*}
```

> $$
> \begin{gather*}
>    x^2 + y^2 = z^2\\
>    x^2 = z^2 - y^2\\
>    x = \sqrt{z^2 - y^2}
> \end{gather*}
> $$

## General Math Symbols

| Symbol              | LaTeX Code          | Symbol                       | LaTeX Code                   |
| ------------------- | ------------------- | ---------------------------- | ---------------------------- |
| $\infty$            | `\infty`            | $\binom{n}{k}$               | `\binom{n}{k}`               |
| $\pi$               | `\pi`               | $\lim_{x \to \infty} f(x)$   | `\lim_{x \to \infty} f(x)`   |
| $\sum_{i=1}^{n} i$  | `\sum_{i=1}^{n} i`  | $\log_{b} a$                 | `\log_{b} a`                 |
| $\prod_{i=1}^{n} i$ | `\prod_{i=1}^{n} i` | $\ln a$                      | `\ln a`                      |
| $\int_{a}^{b} x$    | `\int_{a}^{b} x`    | $\sin x$                     | `\sin x`                     |
| $\frac{a}{b}$       | `\frac{a}{b}`       | $\arcsin x$                  | `\arcsin x`                  |
| $\sqrt{a}$          | `\sqrt{a}`          | $\mathbb{R}$                 | `\mathbb{R}`                 |
| $\sqrt[n]{a}$       | `\sqrt[n]{a}`       | $\left[ \frac{a}{b} \right]$ | `\left[ \frac{a}{b} \right]` |

## Matrices

```latex
\begin{equation*}
    \begin{bmatrix}
        1 & 2 & 3\\
        4 & 5 & 6\\
        7 & 8 & 9
    \end{bmatrix}
\end{equation*}
```

> $$
> \begin{equation*}
>   \begin{bmatrix}
>    1 & 2 & 3\\
>    4 & 5 & 6\\
>    7 & 8 & 9
>   \end{bmatrix}
> \end{equation*}
> $$

## Cases

```latex
\begin{equation*}
    f(n) =
    \begin{cases}
        n/2 & \text{if $n$ is even}\\
        -(n+1)/2 & \text{if $n$ is odd}
    \end{cases}
\end{equation*}
```

> $$
> \begin{equation*}
>   f(n) =
>  \begin{cases}
>  n/2 & \text{if $n$ is even}\\
> -(n+1)/2 & \text{if $n$ is odd}
> \end{cases}
> \end{equation*}
> $$
