# -*- coding: utf-8 -*-
def calc_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax

def lazy_sum(*args)	:
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax	
	return sum
f = lazy_sum(1,3,5,7,9)	
print(f)
print('调用f():',f())

f2 = lazy_sum(1,3,5,7,9)
print('两次调用之后，返回的是新的函数 f == f2:',f == f2)