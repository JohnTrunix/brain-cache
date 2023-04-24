# HTML Meta Tags

!!! info

    Meta Tags are used to provide information about the document to the browser (data about the data).

## Meta Tags

```html
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" />
    <meta name="description" content="Website Description" />
    <meta name="keywords" content="HTML, CSS, JavaScript" />
    <meta name="author" content="John Doe" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>
```

-   `charset` - defines the character encoding for the HTML document
-   `http-equiv` - provides an HTTP header for the information/value of the content attribute (advanced!)
    -   `refresh` - refreshes the page after a specified time
-   `description` - provides a description of the page
-   `keywords` - provides keywords for search engines
-   `author` - provides the name of the author of the document
-   `viewport` - specifies the width and scaling of the viewport

## Other Elements in the Header

```
<head>
    <title>Page Title</title>
    <link rel="icon" type="image/x-icon" href="./favicon.ico" />
</head>
```

-   `title` - defines the title of the document (displayed in the browser tab)
-   `favicon` - defines a small icon for the document (displayed in the browser tab)
