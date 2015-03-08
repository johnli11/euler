"""
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

----------------------

Solution:

(1*2*3*5*7*11*13*17*19) * 			(2*2*3*2)  		   =   232,792,560
			|							|					    |
			|							|					    |
			|							|						|
							minimal primes needed to
  all primes up to 20   *  be divisible by non-primes  =  LCM of [1, 20]


Note: don't use commas when entering solution into Project Euler site or else it will say you entered the wrong site.
Took me an extra hour to figure this out after already getting the correct solution.
"""