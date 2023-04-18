# :rocket: brain-cache

![](https://img.shields.io/github/actions/workflow/status/JohnTrunix/brain-cache/ci.yml)
![](https://img.shields.io/github/last-commit/JohnTrunix/brain-cache)
![](https://img.shields.io/badge/mkdocs--material-v9.1.6-blue)
![](https://img.shields.io/github/repo-size/JohnTrunix/brain-cache)

## Development

Create virtual environment

```bash
virtualenv env --python=3.10
```

Activate virtual environment

```bash
env/Scripts/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

### Social Cards Requirements

-   [Documentation Social Cards](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/)
-   [GTK Release](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)

### Serving

```bash
mkdocs serve
```

Only rebuild current page (faster, useful for big sites)

```bash
mkdocs serve --dirtyreload
```

### Building & Deploying

```bash
mkdocs build
```

Manually deploy to GitHub Pages (instead of GitHub Actions):

```bash
mkdocs gh-deploy --force
```
