# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Practitioners Guide to Building Actuarial Reserving Workflows Using chainladder-python"
copyright = "2024, John Bogaardt, Gene Dan, Kenneth Hsu"
author = "John Bogaardt, Gene Dan, Kenneth Hsu"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import chainladder as cl

extensions = ["IPython.sphinxext.ipython_directive", "nbsphinx"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv", "tmp"]
# latex_additional_files = ['preamble.sty']
latex_elements = {
    'extraclassoptions': 'openany,oneside'
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = []
