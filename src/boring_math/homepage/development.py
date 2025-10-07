"""
Module dependencies
===================

Arrows point from modules to their dependencies.

Internal dependencies
---------------------

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        "integer_math.combinatorics" -> "integer_math.number_theory";
        pythagorean_triples -> "integer_math.number_theory";
    }

External dependencies
---------------------

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        integer_math -> "collections.abc";
        integer_math -> typing;
        integer_math -> "pythonic_fp.circulararray";
        integer_math -> "pythonic_fp.iterables";
        probability_distributions -> abc;
        probability_distributions -> "collections.abc";
        probability_distributions -> math;
        probability_distributions -> typing;
        probability_distributions -> "mathplotlib.pyplot";
        probability_distributions -> "pythonic_fp.fptools";
        pythagorean_triples -> "collections.abc";
        pythagorean_triples -> sys;
        recursive_functions -> "collections.abc";
    }

Semantic versioning
===================

Maintainer has adopted strict 3 digit
`semantic versioning <https://semver.org>`_
and does not use
`caps on dependencies <https://iscinumpy.dev/post/bound-version-constraints>`_.
This allows for more package management flexibility for developers and
access to the latest features.

Periodically known consistent releases of versions are done for those
concerned with stability. These are also posted in the project's CHANGELOG.

CHANGELOG
=========

Pythonic FP overarching
`CHANGELOG <https://github.com/grscheller/boring-math/blob/main/CHANGELOG.rst>`_.

Each individual *Boring Math* project has its own CHANGELOG too.

"""
