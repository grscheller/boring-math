# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# 
# Must match what is in pyproject.toml, also update proposed_release_string accordingly
# when generating the docs for an actual, not proposed, release.
#

project = 'Boring Math - Abstract Algebra'
copyright = '2025, Geoffrey R. Scheller'
author = 'Geoffrey R. Scheller'
release = '1.1.0' 

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
]
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'special-members': True,
    'inherited-members': True,
    'show-inheritance': True,
}
autodoc_member_order = 'bysource'
autoclass_content = 'both'
autodoc_class_signature = 'separated'
autodoc_typehints_format = 'short'
autodoc_use_type_comments = True
autodoc_docstring_signature = False
autodoc_preserve_defaults = True
autodoc_warningiserror = False

templates_path = ['_templates']
exclude_patterns: list[str] = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme_options = {
    "light_css_variables": {
        "color-link--visited": "var(--color-link)",
    },
    "dark_css_variables": {
        "color-link--visited": "var(--color-link)",
    },
}
html_theme = 'furo'
html_static_path = ['_static']
