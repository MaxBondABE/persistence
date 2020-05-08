persistence
===========

A Python program for searching for numbers with a high Base 10 multiplicative persistence.

Multiplicative Persistence is a property determined by multiplying all the digits of a
number together, and repeating the process on the resulting number, and so on, until
you arrive at a number with 1 digit. The number of iterations is the original number's
persistence. As it considers a number's representation in digits, it is inherently
related to the base you're working in.

This program takes an approach I've not seen elsewhere, and tries to climb up the ladder
by finding "reachable" numbers. A number is "reachable" if it can be factored by the
prime digits of your base - for base 10, that's 2, 3, 5, and 7. Successfully factoring
a number X with just those primes proves that there is a number Y that, when you run
1 iteration of multiplicative persistence, results in X - or, in other words, the
persistence of Y is the persistence of X, plus 1.

Additonally, there are many was to transform a number while preserving it's persistence.
For example, rearranging the digits.

It is conjectured that there exist no numbers with a persistence of 12. So the goal is
to transform numbers with a persistence of 11, searching for a reachable combination.
