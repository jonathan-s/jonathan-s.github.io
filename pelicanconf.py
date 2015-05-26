#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jonathan Sundqvist'
SITENAME = 'argpar.se'
SITEURL = ''
SLUGIFY_SOURCE = 'title'
IGNORE_FILES = ['template.md']
THEME = 'pelican-sundown'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
WITH_FUTURE_DATES = True
DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# URL structure on site
ARTICLE_URL = 'posts/{category}/{slug}'
ARTICLE_SAVE_AS = 'posts/{category}/{slug}.html'

DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = ''

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

AUTHOR_URL = 'author/{slug}'
# won't be generated
AUTHOR_SAVE_AS = ''

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME',
    'extra/.gitignore'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/.gitignore': {'path': '.gitignore'},
    'content/pages/404.md': {'path': '404.html'}  # not sure this will work
}

SITEMAP_SAVE_AS = 'sitemap.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
TWITTER_USERNAME = 'argparse'


# Pagination and stuff
DEFAULT_METADATA = {
    'status': 'draft',
}
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 1
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
