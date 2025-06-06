import os
import sys

# -- Path setup -----------------------------------------------------
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information --------------------------------------------
project = 'HDVAE'
copyright = '2025, JunHua Yu'
author = 'JunHua Yu'
release = '1.0.0'

# -- General configuration ------------------------------------------
extensions = []
templates_path = ['_templates']
exclude_patterns = []

# -- HTML output ----------------------------------------------------
html_theme = 'sphinx_rtd_theme'

html_extra_path = ['notebooks']