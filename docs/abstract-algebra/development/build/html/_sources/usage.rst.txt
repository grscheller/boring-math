Usage
=====

How to installing the package
-----------------------------

Install the project into your Python environment:

.. code:: console

    $ pip install boring-math-abstract-algebra

Importing the modules
---------------------

Import classes needed to define your own algebras.

.. code:: python

    from boring_math.abstract_algebra.magma import Magma
    from boring_math.abstract_algebra.semigroup import Semigroup
    from boring_math.abstract_algebra.monoid import Monoid
    from boring_math.abstract_algebra.group import Group

Algebra class hierarchy
-----------------------

Arrows point from super class to sub classes.

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        CommutativeMonoid -> AbelianGroup;
        CommutativeSemigroup -> CommutativeMonoid;
        BaseSet -> CommutativeSemigroup;
        Ring -> Field;
        Monoid -> Group;
        BaseSet -> Magma;
        Semigroup -> Monoid;
        AbelianGroup -> Ring;
        BaseSet -> Semigroup;
    }
