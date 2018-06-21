# md2html

Generate beautiful CSS-flavoured HTML page from Markdown file

## How to use

```bash
md2html.py README.md > docs.html
```

Alternatively you can use option `-o` instead of `>` to specify output file.

### Change flavour

Add option `-f` or `--flavour`. Run `md2html.py --help` to see available flavours.

### Included stylesheets

Add option `-i` or `--include-stylesheet`. Output HTML will contain `<style>` with pre-downloaded stylesheet(s) instead of just `<link>` tag. This might be useful if you need to browse generated documents offline.

## Installation

Clone this repository

```bash
git clone https://github.com/MikeWent/md2html.git && cd md2html
```

Install dependencies

```bash
pip3 install --user --upgrade -r requirements.txt
```

### Upgrade (run this once a week)

Fetch updates

```bash
git pull
```

Update dependencies

```
pip3 install --user --upgrade -r requirements.txt
```

## License

MIT
