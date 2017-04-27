# -*- coding: utf-8 -*-
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a+b
		return a 

f = Fib()
# 获取n个斐波那契数
for n in range(50):
	print('f[%s]:%s' %(n+1,f[n]))