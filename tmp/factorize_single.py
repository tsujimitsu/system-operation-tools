# -*- coding: utf-8 -*-

from time import time

def factorize(number):
    for i in range(1, number + 1):
	    if number % i == 0:
		    yield i

numbers = [2139079, 1214759, 1516637, 1852285]
start = time()
for number in numbers:
    list(factorize(number))
end = time()

print('Took %.3f seconds' % (end - start))
