#!/usr/bin/env python3
import argparse
import sys
from hashlib import md5
from os import mkdir, path
from time import strftime

import yaml
from jinja2 import Template
from markdown2 import markdown
from requests import get as requests_get

SIGNATURE = strftime("""
---
Generated via [md2html](https://github.com/MikeWent/md2html) on %Y.%m.%d %H:%M:%S %z""")

CACHE_DIR = "/tmp/md2html_cache" # no trailing slash

# Determine absolute system path to directory with md2html.py
# to use it instead of relative path
SCRIPT_DIR = sys.path[0]

# Load flavours
with open(SCRIPT_DIR+"/flavours.yaml", "r") as f:
    FLAVOURS = yaml.load(f)

args = argparse.ArgumentParser()
args.add_argument("input", help="Markdown file")
args.add_argument("-o", "--output", metavar="FILENAME", help="output HTML filename")
args.add_argument("-f", "--flavour", help="preferred CSS flavour to use (see flavours.yaml)", default="mini", choices=FLAVOURS.keys())
args.add_argument("-t", "--title", help="HTML title tag", default=None)
args.add_argument("-g", "--signature", help="add signature to output file", action="store_true", default=False)
args.add_argument("-i", "--include-stylesheet", help="include CSS stylesheet into output HTML file to make styles available offline", action="store_true")
args.add_argument("-e", "--allow-html", help="don't escape HTML tags found in Markdown document", action="store_true")
options = args.parse_args()

def http_cached_get(resource_url):
    """Simple HTTP resource fetcher with caching mechanism""" 
    cached_resource_filename = CACHE_DIR+"/"+md5(resource_url.encode("utf-8")).hexdigest()
    # Create cache dir if doesn't exist
    if not path.isdir(CACHE_DIR):
        mkdir(CACHE_DIR)
    # Get file from cache
    if path.isfile(cached_resource_filename):
        with open(cached_resource_filename, "r") as f:
            return f.read()
    else:
        # Save file to cache
        r = requests_get(resource_url)
        content = r.text.strip()
        with open(cached_resource_filename, "w") as f:
            f.write(content)
        return content

if options.output:
    def stdout(anything):
        # Save to file (append mode)
        with open(options.output, "w") as f:
            f.write(anything)
else:
    def stdout(anything):
        # Just print to stdout
        print(anything)

# Read markdown file
with open(options.input, "r") as f:
    markdown_source = f.read()

# Add signature (if -g/--signature) passed
if options.signature:
    markdown_source = markdown_source.join(("\n", SIGNATURE))

extras = [
    "fenced-code-blocks",
    "header-ids",
    "footnotes",
    "tables"
]

if options.allow_html:
    extras.append("markdown-in-html")

# Convert markdown to basic HTML here
converted_markdown = markdown(markdown_source, extras=extras)

with open(SCRIPT_DIR+"/template.html", "r") as f:
    HTML_PAGE_TEMPLATE = Template(f.read())
SELECTED_FLAVOUR = FLAVOURS.get(options.flavour, None)

# If container template doesn't exist for current
# flavour, simply replace it with placeholder
main_container_template = SELECTED_FLAVOUR.get("container", "{{ content }}")
MAIN_CONTAINER = Template(main_container_template)

# Generate a list of CSS stylesheet URLs for jinja2 template
u = SELECTED_FLAVOUR.get("url", None)
if isinstance(u, str):
    stylesheet_urls = [u]
else:
    stylesheet_urls = u

# Download stylesheets if -i/--include-stylesheet is specified
included_stylesheets = []
if options.include_stylesheet:
    for stylesheet_url in stylesheet_urls:
        included_stylesheets.append(
            http_cached_get(stylesheet_url)
        )

# Favour-specified document structure:
#
#   html (HTML_PAGE_TEMPLATE)
#   └─ container (MAIN_CONTAINER, optional)
#      ├─ p
#      ├─ img
#      ├─ pre
#      └─ ...

final_html_output = HTML_PAGE_TEMPLATE.render(
    body=MAIN_CONTAINER.render(
        content=converted_markdown
    ),
    included_stylesheets=included_stylesheets,
    stylesheet_urls=stylesheet_urls,
    custom_css=SELECTED_FLAVOUR.get("css-hack", None),
    title=options.title
)

stdout(final_html_output)
