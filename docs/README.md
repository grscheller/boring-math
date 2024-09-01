## Generating boring-math API Documentation

MathJax expressions are used by pdoc to generate mathematical
expressions in Python docstrings. This is done to render non-code
mathematical expressions.

```bash
   $ cd API/development/
   $ pdoc -o . grscheller.boring_math

```
The pdoc PyPI package, not pdoc3, generates boring-math's detailed HTML
based documentation. It is installed by pip.

MathJax is an open source JavaScript display engine for mathematics that
works in all modern browsers. MathJax is installed by my Linux
distribution's package manager.
