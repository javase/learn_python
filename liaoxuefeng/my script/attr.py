# -*- coding: utf-8 -*-
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
		
obj = MyObject()
print('hasattr(obj, \'x\'):', hasattr(obj, 'x'))		
print('hasattr(obj, \'y\'):',hasattr(obj, 'y'))

setattr(obj,'y',19)
print('hasattr(obj, \'y\'):',hasattr(obj, 'y'))
print('getattr(obj, \'y\'):',getattr(obj, 'y'))
# 获取属性'z'，如果不存在，返回默认值404
print('getattr(obj, \'z\', 404):',getattr(obj, 'z', 404))
# 也可以获得对象的方法
print('hasattr(obj, \'power\'):',hasattr(obj, 'power'))
fn = getattr(obj,'power')
print('fn:',fn)
print('fn():',fn())