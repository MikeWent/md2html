#!/usr/bin/env python3
import argparse
from os import path

import yaml
from jinja2 import Template
from markdown2 import markdown_path

# Determine absolute system path to directory with md2html.py
# to use it instead of relative path
SCRIPT_DIR = path.dirname(path.abspath(__file__))+"/"

# Load flavours
with open(SCRIPT_DIR+"flavours.yaml", "r") as f:
    FLAVOURS = yaml.load(f)

args = argparse.ArgumentParser()
args.add_argument("input", help="Markdown file")
args.add_argument("-o", "--output", metavar="FILENAME", help="output HTML filename")
args.add_argument("-f", "--flavour", help="prefered CSS flavour to use (see flavours.yaml)", default="minicss", choices=FLAVOURS.keys())
args.add_argument("-t", "--title", help="HTML title tag", default=None)
options = args.parse_args()

if options.output:
    def stdout(anything):
        # save to file (append mode)
        with open(options.output, "w") as f:
            f.write(anything)
else:
    def stdout(anything):
        # just print to stdout
        print(anything)

# Convert markdown to basic HTML here
converted_markdown = markdown_path(options.input, extras=(
        "fenced-code-blocks",
        "header-ids",
        "footnotes",
        "tables",
        "markdown-in-html"
    ))

with open(SCRIPT_DIR+"template.html", "r") as f:
    HTML_PAGE_TEMPLATE = Template(f.read())
SELECTED_FLAVOUR = FLAVOURS.get(options.flavour, None)

# If some templates doesn't exist for current
# flavour, simply replace them with placeholder
block_template = SELECTED_FLAVOUR.get("block", "{{ text }}")
main_container_template = SELECTED_FLAVOUR.get("container", "{{ content }}")
BLOCK = Template(block_template)
MAIN_CONTAINER = Template(main_container_template)

# Favour-specified document structure:
#
#   html (HTML_PAGE_TEMPLATE)
#   └─ container (MAIN_CONTAINER, optionally)
#      └─ block (BLOCK, optionally)
#         ├─ p
#         ├─ img
#         ├─ pre
#         └─ ...

final_html_output = HTML_PAGE_TEMPLATE.render(
    body=MAIN_CONTAINER.render(
        content=BLOCK.render(
            text=converted_markdown
        )
    ),
    stylesheet_url=SELECTED_FLAVOUR.get("url", None),
    custom_css=SELECTED_FLAVOUR.get("css", None),
    title=options.title
)

stdout(final_html_output)
