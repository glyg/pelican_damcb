# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guillaume Gay'
SITENAME = u'Morphogénie Logiciels'
SITEURL = 'http://damcb.com'
#SITEURL = 'http://damcb.com/index.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PATH = 'content'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('M. Suzanne group', 'http://www-lbcmcp.ups-tlse.fr/Nouveau_site/modeles/EquipeSuzanne-Accueil.htm'),
    ('X. Wang group', 'http://www-lbcmcp.ups-tlse.fr/'),
    ('S. Tournier group', 'http://s.pombe.free.fr'),
    ('SciPy', 'http://scipy.org/'),
    ('Python.org', 'http://python.org/'),
    ('Graph-tool', 'http://graph-tool.skewed.de/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.org/DamCB'),
          ('Twitter', 'https://twitter.com/elagachado'),
          ('LinkedIn', 'https://www.linkedin.com/pub/guillaume-gay/27/a22/492'),)

GITHUB_USER = 'glyg'


DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('About Morphogénie', '/pages/aboutus.html'),
             ('Projects', '/pages/projects.html'),
             ('Services', '/pages/what-we-do.html'),
             ('Tools', '/pages/tools.html'),
             ('Contact', '/pages/contact.html'),)

### Those are displayed on the index page, with one image, a title and a link
DISPLAY_HEROITEMS = True
HEROITEMS = (('images/logo_modeling.png', 'Projects', '/pages/projects.html'),
             ('images/logo_python.png', 'Tools', '/pages/tools.html'),
             ('images/logo_data.png', 'Services', '/pages/what-we-do.html'),)

THEME = 'themes/glyg'#''notmyidea'
#BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_THEME = 'cosmo'

SITELOGO = 'images/logo_blackbg.png'
HIDE_SITENAME = True

DISPLAY_TAGS_ON_SIDEBAR = True

STATIC_PATHS = ['images']
TYPOGRIFY = True

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'


PLUGIN_PATHS = ['../Pelican/pelican-plugins/', ]
PLUGINS = ['summary',
           'liquid_tags.img',
           'liquid_tags.video',
           'liquid_tags.vimeo',
           'liquid_tags.youtube',
           'liquid_tags.include_code',
           'liquid_tags.notebook',
           'liquid_tags.literal',
           'render_math']

# CATEGORY_SAVE_AS = None
DEFAULT_PAGINATION = 10
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),)


ABOUT_ME = '''Data analysis and modeling for Cell Biology\n
We offer free and open source software services to help biologists get the most out of their experiments.'''

AVATAR=False#'images/logo_blackbg.png'

FAVICON = 'images/favicon.png'
#FAVICON_IE = 'images/favicon.png'


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

NEWEST_FIRST_ARCHIVES = True


SUMMARY_END_MARKER = "<!-- TEASER_END -->"


# Following items are often useful when publishing

DISQUS_SITENAME = "damcellbiology"

import os
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found. "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read()
