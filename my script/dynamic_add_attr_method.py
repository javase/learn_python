# -*- coding: utf-8 -*-
class Student(object):
	pass

s = Student()
s.name = 'Michael'	
print('s.name:',s.name)

def set_age(self,age):
	self.age = age
	
from types import MethodType
s.set_age = MethodType(set_age,s)	# 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print('s.age:',s.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
# s2.set_age(25)
#  'Student' object has no attribute 'set_age'

# 给class绑定方法
def set_score(self,score):
	self.score = score
Student.set_score = set_score

s.set_score(100)
print('s.score:',s.score)
s2.set_score(99)
print('s2.score:',s2.score)