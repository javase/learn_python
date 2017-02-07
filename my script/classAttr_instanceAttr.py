# -*- coding: utf-8 -*-
class Student(object):
	name = 'ClassAttr_Student'
	#def __init__(self,name):
	#	self.name=name

# s = Student('Bob')		
# 并不指定属性name的值
s1 = Student()
print('s1.name:',s1.name)
print('Student.name:',Student.name)
s1.name = 'Michael'
# 给实例绑定name属性
print('s1.name:',s1.name)
# 但是类属性并未消失，用Student.name仍然可以访问
print('Student.name:',Student.name)
# 如果删除实例的name属性
del s1.name
# 再次调用s1.name，由于实例的name属性没有找到，类的name属性就显示出来了
print('s1.name:',s1.name)
# 在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

