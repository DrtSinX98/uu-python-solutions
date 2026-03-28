# Configuration file for the Sphinx documentation builder.

import os
import sys
# This tells Sphinx to look in the parent directory for your Python files
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'simple_math'
copyright = '2026, Pritish Joshi'
author = 'Pritish Joshi'

# -- General configuration ---------------------------------------------------
# Add autodoc to pull docstrings, and napoleon to parse NumPy-style formatting
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']