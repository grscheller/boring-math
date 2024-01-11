# grscheller.boring_math.integer_math module

Library of functions of an integer pure math nature.

## Number theoretic 

* Function **gcd**(fst: int, snd: int) -> int
  * takes two integers, returns greatest common divisor (gcd)
  * where gcd >= 0.
  * gcd(0,0) returns 0 but in this case the gcd does not exist

* Function **lcm**(fst: int, snd: int) -> int
  * takes two integers, returns least common multiple (lcm)

* Function **primes**(start: int=2, end_before: int=100) -> Iterator
  * takes two integers, returns least common multiple (lcm)

## Pythagorean Triples

The values a, b, c > 0 represent integer sides of a right triangle.

* Function **pythag3**(a_max: int=3, all_max: int|None=None) -> Iterator
  * Return an interator of tuples of Pythagorean Tiples
  * Side a <= a_max and sides a, b, c <= all_max
  * Iterator finds all primative pythagorean triples up to a given a_max

## Ackermann's Function

* Function **ackerman**(m: int, n: int) -> int
  * Ackermann's function is a doublely recursively defined function
  * An example of a computable but not primitive recursive function
  * Becomes numerically intractable after m=4

## Fibonacci Sequences

* TODO:
