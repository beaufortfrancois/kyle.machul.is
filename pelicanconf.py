#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kyle Machulis'
SITENAME = u'Kyle Machulis'
SITEURL = 'http://kyle.machul.is'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

THEME = "themes/kyle.machul.is"

# Feed generation is usually not desired when developing
FEED_ATOM = ('atom-fb.xml')
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
FEED_DOMAIN = SITEURL
TRANSLATION_FEED = None
FEED_MAX_ITEMS = 10

# Relative to content dir
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_PATHS = ['posts']
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

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['summary', 'neighbors', ]

SUMMARY_END_MARKER = "<!--more-->"
SUMMARY_MAX_LENGTH = None

STATIC_PATHS = ['extras/htaccess',
                'extras/robots.txt']

EXTRA_PATH_METADATA = {
    'extras/htaccess': {'path': '.htaccess'},
    'extras/robots.txt': {'path': 'robots.txt'}
}

TEMPLATE_PAGES = {'about/about.html': "about/index.html",
                  'config/config.html': "config/index.html",
                  'templates/404.html': "404/index.html"}

EXTRA_TEMPLATES_PATHS = ['content/about/about-templates',
                         'content/config/config-templates']

MENUITEMS = (('bio', '/about'),
             ('blog', '/'),
             ('portfolio', '/portfolio'),
             ('config', '/config'))

SITELOGO = "theme/images/qdotlogo.png"
SITELOGOSVG = "theme/images/qdot.logo.svg"
SITELOGO_SIZE = "35px"
HIDE_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_CATEGORY = False

MD_EXTENSIONS = ['codehilite', 'extra', 'video']
