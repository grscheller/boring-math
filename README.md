# PyPI grscheller.boring-math Project

Daddy's boring math library.

* Python package of functions of a mathematical nature
* Project name suggested by my then 13 year old daughter Mary
* Example of a Python package with both libraries and executables
* [grscheller.boring-math][1] project on PyPI
* [Detailed API documentation][2] on GH-Pages
* [Source code][3] on GitHub

## Overview

Here are the modules and executables which make up the
grscheller.boring_math package.

### Library Modules

* [Integer Math Module](#integer-math-module)
  * [Number Theory](#number-theory)
  * [Combinatorics](#combinatorics)
  * [Fibonacci Sequences](#fibonacci-sequences)

* [Pythagorean Triple Module](#pythagorean-triple-module)
  * [Pythagorean Triple Iterator](#pythagorean-triple-iterator)

* [Recursive Function Module](#recursive-function-module)
  * [Ackermann's Function](#function-ackermann)

---

### CLI Applications

* [Pythagorean Triples](#pythagorean-triples)
  * [Pythagorean Triples App](#pythagorean-triple-app)

* [Recursive Function Theory](#recursive-function-theory)
  * [Ackermann's Function App](#ackermanns-function)

## Libraries

### Integer Math Module

#### Number theory

* Function **gcd**(fst: int, snd: int) -> int
  * takes two integers, returns greatest common divisor (gcd)
  * where `gcd >= 0`
  * `gcd(0,0)` returns `0` but in this case the gcd does not exist

* Function **lcm**(fst: int, snd: int) -> int
  * takes two integers, returns least common multiple (lcm)

* Function **primes**(start: int=2, end_before: int=100) -> Iterator
  * takes two integers, returns an iterator of primes
  * starting at first prime at or after `start`
  * ending at last prime before `end_before`

* Function **coprime**(m: int, n: int) -> Tuple(int, int)
  * make two integers coprime by dividing out their common factors
  * returns `(0, 0)` when `n = m = 0`

* Function **iSqrt**(n: int) -> int
  * return the unique `m` such that `m*m <= n < (m+1)*(m+1)`
  * raises: ValueError if `n < 0`

* Function **isSqr**(n: int) -> bool
  * returns true if `n` is a perfect square
  * raises ValueError if `n < 0`

---

#### Combinatorics

* Function **comb**(n: int, m: int) -> int
  * returns C(n,m) - the number of n items taken m at a time
  * contains two additional default parameters that can be adjusted
    * factorsNumerator = 66
    * factorsDenonator = 4
  * actually comb(n, m, 1, 1) runs faster for reasonably small n and m
    * better choice for inner loops and printable results
    * about 3 times slower than C based math.comb(n, m)
    * the default paramenters
      * are better for larger results
      * work reasonably well for smaller results

---

#### Fibonacci sequences

* Function **fibonacci**(f0: int=0, f1: int=1) -> Iterator
  * return an iterator for a Fibonacci sequence
  * defaults to `0, 1, 1, 2, 3, 5, 8, ...`

### Pythagorean Triple Module

#### Pythagorean triple iterator

The values `a, b, c > 0` represent integer sides of a right triangle.

* Method **Pythag3.triples**(a_start: int=3, a_max: int=3, max: int=0) -> Iterator
  * Returns an interator of tuples of primative Pythagorean Triples
  * Side `a <= a_max` and sides `a, b, c <= max`
  * Iterator finds all primative pythagorean within the given parameters

### Recursive Function Module

#### Function **ackermann**

An example of a total computable function that is not primitive recursive.

* Function **ackermann**(m: int, n: int) -> int
  * Ackermann's function is a doublely recursively defined function
  * Becomes numerically intractable after m=4

## CLI Applications

Implemented in a platform independent way via pyproject.toml.

### Pythagorean Triples

#### Pythagorean triple app

* CLI App **pythag3**
  * A Pythagorean triple is a 3-tuple of integers `(a, b, c)` such that
    * `a*a + b*b = c*c` where `a,b,c > 0` and `gcd(a,b,c) = 1`
  * The integers `a, b, c` represent the sides of a right triangle
  * Usage: `pythag3 [n1 [n2 [n3]]`
    * 3 arguments print all triples with n1 <= a <= n2 and a,b,c <= n3
    * 2 arguments print all triples with n1 <= a <= n2
    * 1 argument prints all triples with a <= n1
    * 0 arguments print all triples with 3 <= a <= 100

### Recursive Function Theory

#### Ackermann's function

Ackermann, a student of Hilbert, discovered early examples of totally
computable functions that are not primitively recursive.

A [fairly standard][4] definition of the Ackermann function is
recursively defined for `m,n >= 0` by

```
     ackermann(0,n) = n+1
     ackermann(m,0) = ackermann(m-1,1)
     ackermann(m,n) = ackermann(m-1, ackermann(m, n-1))
```

* CLI App **ackerman**
  * Given two non-negative integers, evaluates Ackermann's function
  * Implements the recursion via a Python array
  * Usage: `ackerman m n`

[1]: https://pypi.org/project/grscheller.boring-math/
[2]: https://grscheller.github.io/boring-math/API/development/html/grscheller/boring_math/index.html
[3]: https://github.com/grscheller/boring-math
[4]: https://mathworld.wolfram.com/AckermannFunction.html
