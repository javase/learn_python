# -*- coding: utf-8 -*-
class Student(object):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	
	def print_score(self):
		print('%s:%s' % (self.__name,self.__score))
		
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
		
# 不用new关键字		
bart = Student('Tom',98)		
# print('访问私有变量 bart.__name:',bart.__name)
print('使用get访问私有变量 bart.get_name():',bart.get_name())
bartB = Student('Bart Simpson',98)
print('使用get访问私有变量 bartB.get_name():',bartB.get_name())
bartB.__name = 'New Name'
print('bartB.__name is ',bartB.__name)
print('直接给__name赋值，其实是又声明了一个变量')
print('使用get访问私有变量 bartB.get_name():',bartB.get_name())
print('用barB._Student__name设置私有变量，会报错')
print('直接访问私有变量(不推荐) bartB._Student__name:',bartB._Student__name)