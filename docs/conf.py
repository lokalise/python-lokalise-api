# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/`master`/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from lokalise._version import __version__

# -- Project information -----------------------------------------------------
project = 'python-lokalise-api'
copyright = '2020, Lokalise team, Ilya Bodrov'
author = 'Lokalise team, Ilya Bodrov'

# The full version, including alpha/beta/rc tags
release = __version__
version = __version__

# -- General configuration ---------------------------------------------------
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = 'Python Lokalise API client'
html_short_title = 'Lokalise API client'

html_sidebars = {
    "index": [
        'about.html',
        "globaltoc.html",
        "links.html",
        "slim_searchbox.html",
    ],
    "**": [
        'about.html',
        "globaltoc.html",
        "relations.html",
        "links.html",
        "slim_searchbox.html",
    ],
}

html_theme_options = {
    'logo': 'lok_logo.png',
    #'description': 'Official Lokalise APIv2 Python interface',
    'github_user': 'lokalise',
    'github_repo': 'python-lokalise-api',
    'github_button': 'true',
    'show_powered_by': 'false'
}
