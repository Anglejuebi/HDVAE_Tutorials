# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'HDVAE Tutorials'
copyright = '2025, JunHua Yu'
author = 'JunHua Yu'
release = '1.0'

# -- General configuration
extensions = [
   'nbsphinx',
]

# Support for file suffixes
source_suffix = ['.ipynb']

# nbsphinx configuration
nbsphinx_allow_errors = True
nbsphinx_execute = 'never'

# HTML output configuration
html_theme = 'sphinx_rtd_theme'
templates_path = ['_templates']

# Language setting
language = 'en'  # English
