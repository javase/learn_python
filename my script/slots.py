# -*- coding: utf-8 -*-
class Student(object):
	__slots__ = ('name','age')
	
s = Student()
s.name = 'Michael'	
s.age = 25
# s.score = 99 # 绑定属性'score'
# 这时会报错  AttributeError: 'Student' object has no attribute 'score'
# 要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class GraduateStudent(Student):
	pass
	
g = GraduateStudent()
g.score = 98	
print('子类不受__slots__影响,g.score:',g.score)