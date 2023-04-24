# CSS Selectors

## Element Selector

```css
div {
    color: green;
    font-size: 2em;
}
```

## Class Selector

```css
.class {
    color: red;
    font-size: 2em;
}
```

## ID Selector

```css
#id {
    color: blue;
    font-size: 1em;
}
```

## Universal Selector

```css
* {
    color: green;
    font-size: 2em;
}
```

!!! note

    The universal selector selects all HTML elements.

## Advanced Selectors

Note: All Selector Patterns can be found at [w3schools.com](https://www.w3schools.com/cssref/css_selectors.php){target=\_blank}.

### Grouping Selector

```css
div,
p {
    color: green;
    font-size: 2em;
}
```

### Descendant Selector

```css
div p {
    color: green;
    font-size: 2em;
}
```

!!! note

    Styles are only applied to the last element which are in the hierarchy.
