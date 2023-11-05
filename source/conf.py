# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'debug record'
copyright = '2023, org.debugrecord'
author = 'org.debugrecord'
release = '0.1-SNAPSHOTS'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = {
    '.rst': 'restructuredtext',
#   '.txt': 'restructuredtext',
    '.md': 'markdown',
}

## myst parser extentions

# By adding "colon_fence" to myst_enable_extensions (in the sphinx conf.py configuration file), 
# you can also use ::: delimiters to denote directives, instead of ```
myst_enable_extensions = ["colon_fence"]

# Add line numbers to code blocks with these languages (default: [])
myst_number_code_blocks = ["python"]