"""
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


x = 3
y = 5
total = 0


while x < 1000:
	total += x
	x += 3

while y < 1000:
	if y % 3 == 0:
		pass
	else:
		total += y
	y += 5

print 'The sum of all multiples of 3 and 5 under 1000 is %d' % total