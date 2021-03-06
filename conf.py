# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import datetime
sys.path.insert(0, os.path.abspath('.'))
today_date = datetime.date.today()


# -- Project information -----------------------------------------------------

project = "Carpentries Internationalisation Handbook"
author = "The Carpentrie's i18n team"
copyright = f"2019-{today_date:%Y}, {author}. Creative Commons Attribution 4.0 International license."



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'LICENSE.rst', 'README.rst',]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

extlinks = {'project': ('https://github.com/orgs/carpentries-i18n/projects/%s',
                        'project '),
            'org-repo': ('https://github.com/carpentries-i18n/%s', ''),
            'issue-p4g': ('https://github.com/carpentries-i18n/po4gitbook/issues/%s', 'po4gitbook#'),
            'commit-png': ('https://github.com/carpentries-i18n/python-novice-gapminder/commit/%s', 'commit '),
            }

todo_include_todos = True
todo_link_only = True
