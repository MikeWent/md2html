# md2html

Create beautiful CSS-flavoured HTML page from Markdown file

## Usage

For example, you have a `document.md` file and want to convert it to HTML. Simply run:

```$ md2html.py document.md -o index.html```

Then copy `index.html` to a directory accessible by a web-server or just open in any web-browser.

## Installation

```bash
git clone https://github.com/MikeWent/md2html.git && cd md2html
pip3 install --user -r requirements.txt
sudo ln -s $PWD/md2html.py /usr/bin/local/md2html.py
```

## Upgrade

```bash
git pull
```

## License

MIT