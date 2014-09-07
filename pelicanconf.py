#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guillaume Gay'
SITENAME = u'DamCB'
SITEURL = 'http://damcb.com'
#SITEURL = 'http://damcb.com/index.html'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('SciPy', 'http://scipy.org/'),
         ('Python.org', 'http://python.org/'),
         ('Graph-tool', 'http://graph-tool.skewed.de/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.org/DamCB'),
          ('Twitter', 'https://twiter.com/elagachado'),)

THEME = 'themes/glyg'#''notmyidea'
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_THEME = 'cosmo'

SITELOGO = 'images/logo_blackbg.png'
HIDE_SITENAME = True

STATIC_PATHS = ['images']
TYPOGRIFY = True

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'


PLUGIN_PATHS = ['../Pelican/pelican-plugins/', ]
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
'liquid_tags.youtube', 'render_math',
'liquid_tags.include_code', 'liquid_tags.notebook',
'liquid_tags.literal']

# CATEGORY_SAVE_AS = None
DEFAULT_PAGINATION = 10
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),)


ABOUT_ME = '''We offer free and open source software services to help biologists get the most out of their experiments.'''

AVATAR=False#'images/logo_blackbg.png'

FAVICON = 'images/favicon.png'
#FAVICON_IE = 'images/favicon.png'


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

NEWEST_FIRST_ARCHIVES = True

# Following items are often useful when publishing

DISQUS_SITENAME = "damcellbiology"
#GOOGLE_ANALYTICS = ""

EXTRA_HEADER = open('_nb_header_minimal.html').read().decode('utf-8')