from collections import Iterable

d = {'a':1,'b':2,'c':3,'d':4,'e':5}
def iter_d(d):	
	for key in d:
		print(key)
	print('----')	
		
print('对dict进行N次迭代')		
iter_d(d)
iter_d(d)
iter_d(d)
print('d是否为一个可迭代对象？ ',isinstance(d,Iterable))

print('对List按照索引进行迭代')
L = ['A','B','C']
for i, value in enumerate(L):
	print(i,value)