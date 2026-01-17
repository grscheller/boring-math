# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
#
# Must match what is in pyproject.toml, also update proposed_release_string accordingly
# when generating the docs for an actual, not proposed, release.

from typing import Any
from sphinx.application import Sphinx

project = 'Boring Math - Abstract Algebra'
copyright = '2026, Geoffrey R. Scheller'
author = 'Geoffrey R. Scheller'
release = '1.1.0'


def skip_abc_methods(
    app: Any, what: str, name: str, obj: Any, skip: bool, options: Any
) -> bool:
    if name in [
        '__init_subclass__',
        '__subclasshook__',
        '__class_getitem__',
        '__weakref__',
    ]:
        return True  # Skip these members
    return skip


def setup(app: Sphinx) -> None:
    app.connect('autodoc-skip-member', skip_abc_methods)


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
]
autodoc_default_options = {
    'members': True,
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
    'light_css_variables': {
        'color-link--visited': 'var(--color-link)',
    },
    'dark_css_variables': {
        'color-link--visited': 'var(--color-link)',
    },
}
html_theme = 'furo'
html_static_path = ['_static']
