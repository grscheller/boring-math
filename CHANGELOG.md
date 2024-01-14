# CHANGELOG: grscheller.boring_math

Will become CHANGELOG for grscheller.boring_math

## Overview

* Single Maintainer PyPI Package
* Rolling Release Model
  * maintained on GitHub, software is an Alpha release 
  * maintainer will not back port bug fixes to previous versions
  * main branch will be the release branch
    * will either be the current PyPI release, or
    * will be the release canidate for the next PyPI release
    * PyPI releases are tagged with a leading "v" on GitHub
  * devel branch will be the only software development tracking branch
    * will attempt to keep relatively stable, but
    * may not be fully tested
  * feature branches begin with "feature_" and are places to
    * explore new directions
    * commit potentially very broken code
    * could be deleted from GitHub anytime WITHOUT WARNING
* Semantic versioning for PyPI releases:
  * first digit signifies a major event, epoch, or paradigm shift
  * second digit means
    * breaking API changes
    * major changes
  * third digit either means
    * API additions
    * bugfixes or minor changes
    * documentation updates
  * forth digit (develoment branches only)
    * commit count
    * development environment thrashing
    * not to be taken too seriously

## Version - PyPI releases begin with "v"

### Veresion 0.0.8 - commit date 2024-01-14

* working on pyproject.toml infrastructure for PyPI releases
* will use Flit as the packaging/publishing tool
* replaced bin/ scripts with boring_math.integer_math_cli entry pts

### Veresion 0.0.4 - commit date 2024-01-10

* first coding changes in years!
* configured gh-pages

### Version 0.0.0.3 - commit date 2023-12-06

* added pyproject.toml

### Version 0.0.0.2 - commit date 2023-12-06

* got package working again
  * did not understand iterators that well when I first wrote this package
* replaced my `take` with `itertools.islice`
* generated docs from docstrings with pdoc3

### Version 0.0.0.1 - commit date 2023-12-06

* fixed Markdown issues with first commit
* Added .gitignore file to anticipate pytest & __pycache__ directories
 
### Version 0.0.0.0 - commit date 2023-12-06

* first commit of source code with with the old pipfile build
  infrastructure removed.
