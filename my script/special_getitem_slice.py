# -*- coding: utf-8 -*-
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a 
		if isinstance(n,slice): # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x>= start:
					L.append(a)
				a,b = b,a+b	
			return L	

f = Fib()
# 获取n个斐波那契数
for n in range(50):
	print('f[%s]:%s' %(n+1,f[n]))
print('f[:10]:',f[:10])	
# 通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口