# brain-cache

JohnTrunix's Brain Cache

## Development

Create virtual environment

```bash
virtualenv env --python=3.10
```

Activate virtual environment

```bash
source env/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

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
