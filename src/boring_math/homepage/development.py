"""
Module Dependencies
===================

All non-typing related dependencies.
Arrows point from modules to their dependencies.

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        combinatorics -> "pythonic_fp.circulararray";
        combinatorics -> "pythonic_fp.iterables";
        combinatorics -> number_theory;
        number_theory -> "pythonic_fp.circulararray";
        number_theory -> "pythonic_fp.iterables";
        pythagorean_triples -> sys;
        pythagorean_triples -> number_theory;
        recursive_functions -> sys;
        recursive_functions -> "pythonic_fp.iterables";
    }

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        probability_distributions -> math;
        probability_distributions -> "mathplotlib.pyplot";
        probability_distributions -> "pythonic_fp.fptools";
        special_functions -> cmath;
        special_functions -> math;
    }

Semantic Versioning
===================

Boring Math Projects
--------------------

Maintainer has adopted strict 3 digit
`semantic versioning <https://semver.org>`_
and does not put
`caps on dependencies <https://iscinumpy.dev/post/bound-version-constraints>`_
for library modules. The few example executables also do not have caps
since their purpose is to show library usage.

This allows for more package management flexibility for software
developers using these libraries, and provides easier access
to the latest features.

Homepage & Integrated Testing (pythonic-fp)
-------------------------------------------

The meanings for version numbers can change with paradigm shifts.
Currently they are

- major: for paradigm shifts
- minor: homepage changes, additional tests
- patch: typos, git/pypi thrashing, pure eye-candy

Changelog
=========

Boring Math overarching
`CHANGELOG <https://github.com/grscheller/boring-math/blob/main/CHANGELOG.md>`_.

Each individual Boring Math project has its own CHANGELOG too.

"""
