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
		
# 不用new关键字		
bart = Student('Tom',98)		
# print('访问私有变量 bart.__name:',bart.__name)
print('使用get访问私有变量 bart.get_name():',bart.get_name())