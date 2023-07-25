# CSS :simple-css3:

!!! note

    CSS is a language for describing the presentation of a Webpage. It can handle:
    - Fonts
    - Colors
    - Layout
    - Style
    - Animations
    - etc.

## Add CSS to HTML

```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <div></div>
    </body>
</html>
```

**Other Methods:**

-   Internal CSS - CSS in the `<head>` tag with `<style>` tags
-   Inline CSS - CSS in the HTML element with the `style` attribute

## CSS Selectors

```css
div {
    color: green;
    font-size: 2em;
}

.class {
    color: red;
    font-size: 2em;
}

#id {
    color: blue;
    font-size: 1em;
}
```

!!! note

    CSS Styles can applied to HTML elements, classes, IDs, and more.
    It can also be applied to a specific element in a specific hierarchy.
