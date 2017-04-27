# -*- coding: utf-8 -*-
def add(x,y,f):
	return f(x) + f(y)
	
print('两个数字的绝对值之和：',add(-8,-10,abs))	