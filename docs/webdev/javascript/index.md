# JavaScript

!!! info

    JavaScript is a programming language that adds interactivity to your website. This happens in the browser, and it is the main language for the web.

Embed JavaScript in HTML using the `<script>` tag.

```html
<script type="text/javascript" src="./main.js">
    // code or in imported file
    console.log("test")
</script>
```

!!! note

    Embed Script:

    - `<head>` tag to load before DOM content
    - `<body>`-end tag to load after DOM content (if it needs to access DOM elements)

## Installation

-   [Node.js](https://nodejs.org/en/)

**New Project/Packages init:**

```bash
npm init
```

**Package Installation:**

```bash
npm install <package-name>
```

## package.json

```json
{
    "name": "new-project",
    "version": "1.0.0",
    "description": "This is a new-project",
    "main": "index.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "dev": "parcel index.html",
        "build": "parcel build index.html"
    },
    "repository": {
        "type": "git",
        "url": "www.github.com/user/repository"
    },
    "keywords": ["keyword1", "keyword2"],
    "author": "author",
    "license": "GPL-3.0",
    "dependencies": {
        "chart.js": "^4.2.1",
        "express": "^4.18.2"
    },
    "devDependencies": {
        "parcel": "^2.8.3"
    }
}
```

### run scripts

```bash
npm run <script-name>
```

### run js in terminal

```bash
node <file-name>
```
