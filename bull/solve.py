#!/usr/bin/python

import itertools

def count_digits(number):
	ret = ''
	for k,g in itertools.groupby(number):
		ret += str(len(list(g))) + k

	return ret

a = [ '1' ]

for i in range(1,31):
	a.append(count_digits(a[i-1]))

print len(a[30])
