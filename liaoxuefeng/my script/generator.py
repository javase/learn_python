# -*- coding: utf-8 -*-
L = [x*x for x in range(10)]
print(L)
print('g是一个generator')
g = (x*x for x in range(10))
print(g)
print('获取g的一个元素：',next(g))
print('获取g的一个元素：',next(g))
print('使用for对g进行迭代')
for n in g:
	print(n)