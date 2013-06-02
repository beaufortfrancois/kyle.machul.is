#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kyle Machulis'
SITENAME = u'Nonpolynomial Labs'
SITEURL = 'http://nonpolynomial.com'

TIMEZONE = 'US/Pacific'

MARKUP = (('md', 'markdown'))

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = ('atom-fb.xml')
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
FEED_DOMAIN = SITEURL
TRANSLATION_FEED = None
FEED_MAX_ITEMS = 10

THEME = "themes/nonpolynomial"

# Relative to content dir
PAGE_DIR = 'pages'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_DIR = 'posts'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORY_SAVE_AS = False
TAG_URL = 'tag/{slug}/index.html'
TAG_SAVE_AS = 'tag/{slug}/index.html'
AUTHOR_SAVE_AS = False

DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATH = 'plugins'
PLUGINS = ['summary', 'neighbors', ]

SUMMARY_END_MARKER = "<!--more-->"
SUMMARY_MAX_LENGTH = None

FILES_TO_COPY = (('extras/htaccess', '.htaccess'),)

TEMPLATE_PAGES = {'about/about.html': "about/index.html",
                  'templates/404.html': "404/index.html"}

EXTRA_TEMPLATES_PATHS = (['content/about/about-templates'])

MD_EXTENSIONS = ['codehilite', 'extra', 'video']
