# CSS Common Properties

## Units

```css
div {
    font-size: 1rem;
    width: 100px;
    height: 100vh;
}
```

### Absolute Lengths

-   `cm` - centimeters
-   `mm` - millimeters
-   `in` - inches
-   `px` - pixels

### Relative Lengths

-   `em` - relative to the font-size of the element (2em means 2 times the size of the current font)
-   `rem` - relative to font-size of the root element
-   `vw` - relative to 1% of the width of the viewport
-   `vh` - relative to 1% of the height of the viewport
-   `%` - relative to the parent element
-   `ch` - relative to the width of the "0" (zero)

## Psuedo-classes[^1]

!!! note

    Psuedo-classes are used to define a special state of an element.

```css
div:hover {
    background-color: red;
}
```

## Psuedo-elements[^2]

!!! note

    Psuedo-elements are used to style specified parts of an element.

```css
tr:nth-child(even) {
    background-color: #f2f2f2;
}
```

-   `:first-child` - selects the first child element of a parent element
-   `(even|odd|n)` - selects even, odd or every n-th elements

## Colors

```css
div {
    color: green;
    color: #00ff00;
    color: rgb(0, 255, 0);
    color: rgba(0, 255, 0, 0.5);
    color: hsl(120, 100%, 50%);
    color: hsla(120, 100%, 50%, 0.5);
    color: transparent;
}
```

-   `green` - named colors
-   `#00ff00` - hex colors
-   `rgb(0, 255, 0)` - rgb colors
-   `rgba(0, 255, 0, 0.5)` - rgba colors with alpha (transparency)
-   `hsl(120, 100%, 50%)` - hsl colors
-   `hsla(120, 100%, 50%, 0.5)` - hsla colors with alpha (transparency)

## Background

```css
div {
    background-color: blue;
    background-image: url("image.jpg");
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    background: blue url("image.jpg") no-repeat fixed center; /* shorthand */
}
```

## Fonts & Text Properties

```css
div {
    font-family: "Times New Roman", Times, serif;
    font-size: 16px;
    font-style: italic;
    font-weight: bold;
}
```

-   `font-family` - font family, fallbacks and specification
    -   `serif` - serif fonts
    -   `sans-serif` - sans-serif fonts
    -   `monospace` - monospace fonts

### Alignment

```css
div {
    text-align: left;
}
```

**Options:**

-   `left`
-   `right`
-   `center`
-   `justify`

### Other Properties

```css
div {
    text-transform: uppercase;
    text-decoration: underline;
    text-indent: 50px;
    text-shadow: 2px 2px 5px black;
    letter-spacing: 2px;
    word-spacing: 2px;
    line-height: 2;
    white-space: nowrap;
}
```

[^1]: [Psuedo-classes](https://www.w3schools.com/css/css_pseudo_classes.asp){target=\_blank}
[^2]: [Psuedo-elements](https://www.w3schools.com/css/css_pseudo_elements.asp){target=\_blank}
