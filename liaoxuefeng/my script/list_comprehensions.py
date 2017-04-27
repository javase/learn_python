# -*- coding: utf-8 -*-
print('列表生成式')
print('list(range(1,11):',list(range(1,11)))
print('[x*x for x in range(1,11)]:',[x*x for x in range(1,11)])
print('加上if的列表生成式[x*x for x in range(1,11) if x%2 == 0]:',[x*x for x in range(1,11) if x%2 == 0])
print('两层循环[m + n for m in \'ABC\' for n in \'XYZ\']:',[m + n for m in 'ABC' for n in 'XYZ'])
print('两层循环[m + n for m in \'12\' for n in \'XYZ\']:',[m + n for m in '12' for n in 'XYZ'])

print('列出当前目录下的所有文件和目录名')
import os
l = [d for d in os.listdir('.')]
for i in l:
	print('当前目录文件:',i)
	
print('for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value')	
d = {'x':'1','y':'2','z':'3'}
for k,v in d.items():
	print('%s = %s' %(k,v))

print('列表生成式也可以使用两个变量来生成list')	
l_from_dict = [k + '=' + v for k,v in d.items()]
print(l_from_dict)

print('把一个list中所有的字符串变成小写')
upper_l = ['HELLO','YES','PYTHON','JAVA','SHELL']
lower_l = [s.lower() for s in upper_l]
print('转成小写的list：',lower_l)

print('list comprehensions homework')
L1 = ['Hello', 'World', 18, 'Apple', None]

def upper_to_lower_typecheck(power_l):
	return [s.lower() for s in power_l if isinstance(s,(str))]
		
L2 = upper_to_lower_typecheck(L1)
print(L2)	