# -*- coding: utf-8 -*-
from functools import reduce
def multiply(x,y):
	return x*y
def prod(l):
	return reduce(multiply,l)
	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))	


print('使用lambda表达式')
def prod_lambda(l):
	return reduce(lambda a,b:a*b,l)
print('3 * 5 * 7 * 9 =', prod_lambda([3, 5, 7, 9]))
	
	
	