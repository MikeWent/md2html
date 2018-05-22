#!/usr/bin/env python3
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# read long description from README.md
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='md2html',
    version='0.0.1',
    description='Create beautiful CSS-flavoured HTML page from Markdown file',
    keywords='markdown html',
    long_description=long_description,
    url='https://github.com/MikeWent/md2html',
    author='Mike_Went',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup :: HTML',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    py_modules=['md2html'],
    scripts=['md2html.py'],
    install_requires=['jinja2', 'markdown2', 'pyyaml'],
    
    project_urls={
        'Bug Reports': 'https://github.com/MikeWent/md2html/issues',
        'Funding': 'https://meew.me/#donate',
        'Source': 'https://github.com/MikeWent/md2html',
    },
)
