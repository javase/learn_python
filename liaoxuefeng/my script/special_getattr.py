# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self):
		self.name = 'Michael'
	def __getattr__(self,attr):
		if attr=='score':
			return 99
	
s = Student()
print('s.name:',s.name)		
print('s.x:',s.x)	
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找	


class Chain(object):
	def __init__(self,path=''):
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s' %(self._path,path))
		
	def __str__(self):
		return self._path
	# __repr__==__str__
	# 传入的参数为：user
	def __call__(self,user):
		return self.__getattr__(":" + user)

print('Chain().status.user.timeline.list:',Chain().status.user.timeline.list)
print('Chain().users(\'michael\').repos:',Chain().users('michael').repos)