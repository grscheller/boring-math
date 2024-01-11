# grscheller.boring_math.integer_math module

## Library of functions of an integer pure math nature.

### Number theoretic 

* Function **gcd**(fst: int, snd: int) -> int
  * takes two integers, returns greatest common divisor (gcd)
  * where gcd >= 0.
  * gcd(0,0) returns 0 but in this case the gcd does not exist

* Function **lcm**(fst: int, snd: int) -> int
  * takes two integers, returns least common multiple (lcm)

* Function **primes**(start: int=2, end_before: int=100) -> Iterator
  * takes two integers, returns least common multiple (lcm)

### Pythagorean Triples

* Function **merge**(*iter: iterator) -> Iterator
  * Merge multiple iterator streams until one is exhausted

### Pythagorean Triples

* TODO:

### Ackermann's Function

* Function **ackerman**(m: int, n: int) -> int
  * Ackermann's function is a doublely recursively defined function
  * An example of a computable but not primitive recursive function
  * Becomes numerically intractable after m=4

### Fibonacci Sequences

* TODO:
