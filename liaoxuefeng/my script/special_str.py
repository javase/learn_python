# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name = name
	# 有些像Java中的toString()方法	
	def __str__(self):
		return 'Student object (name:%s)' %self.name
print(Student('Michael'))		