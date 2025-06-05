# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information
project = 'HDVAE Tutorials'
copyright = '2025, JunHua Yu'
author = 'JunHua Yu'
release = '1.0'

# -- General configuration
extensions = [
   'nbsphinx',  # Render .ipynb files
   'sphinx.ext.autodoc',
   'sphinx.ext.doctest',
   'sphinx.ext.intersphinx',
   'sphinx_rtd_theme',  # Read the Docs theme
]

# Support for file suffixes
source_suffix = {
   '.rst': 'restructuredtext',
   '.ipynb': 'nbsphinx',
}

# nbsphinx configuration
nbsphinx_allow_errors = True
nbsphinx_execute = 'never'  # Skip executing notebooks to speed up builds

# HTML output configuration
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
templates_path = ['_templates']

# Language setting
language = 'en'  # English

# Workaround for nbsphinx parser registration on Sphinx 6.x+
import nbsphinx
from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace

# def setup(app: Sphinx):
#     nbsphinx.setup(app)  # 手动调用 nbsphinx 的注册
