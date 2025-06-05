# -- Project info -----------------------------------------------------
project = 'HDVAE Documentation'
author = 'Your Name'
release = '0.1'

# -- General config ---------------------------------------------------
extensions = []  # 不需要 myst-nb 或 nbsphinx

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output config -----------------------------------------------
html_theme = 'alabaster'  # 或 sphinx_rtd_theme（更适合 RTD）
html_static_path = ['_static', 'notebooks_html']  # 添加 HTML notebook 文件目录
