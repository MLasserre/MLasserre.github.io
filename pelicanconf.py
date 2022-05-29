#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marvin Lasserre'
SITENAME = 'Marvin Lasserre'
SITESUBTITLE = 'Ph.D. in computer science'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE = 'fs'

DEFAULT_DATE_FORMAT = '%d %b %Y'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/MLasserre'),)

# Pagination
DEFAULT_PAGINATION = 10
# PAGINATION_PATTERNS = (
    # (1, '{base_name}/', '{base_name}/index.html'),
    # (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )

# RELATIVE_URLS = True

STATIC_PATHS = ['images', 'assets', 'pdfs']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    #'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

ARTICLE_PATHS = ['articles']
ARTICLE_EXCLUDES = ['static', 'extra']
ARTICLE_ORDER_BY = 'reversed-date'

PAGE_PATHS = ['pages']

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'


### Plugins

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'neighbors', 'assets']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

THEME = 'attila'


DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

#MENUITEMS = 
#PUBLICATIONS_SRC = 'content/publication_list.bib'

HOME_COVER = 'images/pig.jpg'
#HEADER_COLOR = 'green'

AUTHORS_BIO = {
  "Marvin Lasserre": {
    "name": "Marvin Lasserre",
    "cover": "images/pig.jpeg",
    "image": "images/profile_picture.jpg",
    "linkedin": "marvin-lasserre",
    "github": "MLasserre",
    "location": "Paris",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/myblog.css']

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
    'extensions' :[
        'jinja2.ext.loopcontrols',
        'jinja2.ext.i18n',
        'jinja2.ext.do'
    ]
}

