# md2html

Generate beautiful CSS-flavoured HTML page from Markdown file

## How to use

```bash
md2html README.md > docs.html
```

Alternatively you can use option `-o` instead of `>` to specify output file.

### Change flavour

```bash
md2html -f mini README.md > docs.html
```

Available flavours:

- mini
- mini-dark
- skeleton
- bootstrap
- min
- milligram

You can also run `md2html --help` to see available flavours.

### Included stylesheets

```bash
md2html.py -i README.md > docs.html
```

Output HTML will contain `<style>` with pre-downloaded stylesheet(s) instead of just `<link>` tag. This might be useful if you need to browse generated documents offline.

## Installation

Clone this repository

```bash
git clone https://github.com/MikeWent/md2html.git && cd md2html
```

Install dependencies

```bash
pip3 install --user --upgrade -r requirements.txt
```

Create symlink

```bash
sudo ln -s $PWD/md2html.py /usr/local/bin/md2html
```

### Upgrade (run this once a week)

Fetch updates

```bash
git pull
```

Update dependencies

```bash
pip3 install --user --upgrade -r requirements.txt
```

## License

MIT
