# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name = name
	def __call__(self):
		print('My name is %s.' %self.name)
	
s = Student('Michael')
# 直接用实例本身调用默认方法
s()  # self 参数不需要传入

# 判断是一个对象还是一个函数
print('callable(Student(1)):',callable(Student(1)))	
print('callable(max):',callable(max))
print('callable([1, 2, 3]):',callable([1, 2, 3]))
print('callable(None):',callable(None))
print('callable(\'str\'):',callable('str'))
print('callable(abs):',callable(abs))