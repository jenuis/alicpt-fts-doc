# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'alicpt-fts-doc'
copyright = '2024, Xiang Liu(刘祥)@ASIPP'
author = 'Xiang Liu@ASIPP'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sphinx_rtd_theme
 
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel']

templates_path = ['_templates']
exclude_patterns = []

#language = 'zh_CN'
language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
