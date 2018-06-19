# md2html

Generate beautiful CSS-flavoured HTML page from Markdown file

## Usage

### Basic

```bash
./md2html.py README.md > docs.html
```

or

```bash
./md2html.py README.md -o docs.html
```

### Change flavour

Add option `-f` or `--flavour`. See `flavours.yaml` or `./md2html.py --help` to list available flavours.

```bash
./md2html.py -f bootstrap README.md > docs.html
```

### Included stylesheets

Add option `-i` or `--include-stylesheet`. This might be useful if you need to browse generated documents offline.

```bash
./md2html.py -i README.md > docs.html
```

Output HTML will contain `<style>` with pre-downloaded stylesheet(s).

## Installation

Clone this repository

```bash
git clone https://github.com/MikeWent/md2html.git && cd md2html
```

Install dependencies

```bash
pip3 install --user --upgrade -r requirements.txt
```

## Upgrade

```bash
git pull
```

## License

> MIT
