# Configuration file for the Sphinx documentation builder.
#
# Update Release string to agree with boring-math/pyproject.toml
# before a PyPI release.
#

project = 'Boring Math'
copyright = '2016-2026, Geoffrey R. Scheller'
author = 'Geoffrey R. Scheller'
release = '3.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
]

autodoc_member_order = 'bysource'
autoclass_content = 'both'

templates_path = ['_templates']
exclude_patterns: list[str] = []

html_theme_options = {
    'light_css_variables': {
        'color-link--visited': 'var(--color-link)',
    },
    'dark_css_variables': {
        'color-link--visited': 'var(--color-link)',
    },
}
html_theme = 'furo'
html_static_path = ['_static']
