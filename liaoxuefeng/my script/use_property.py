# -*- coding: utf-8 -*-
class Student(object):

# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be int type')
		if value<0 or value > 100:
			raise ValueError('score must between 0 ^ 100!')
		self._score = value	
		
		
		
s = Student()
s.score = 60
print('s.score:',s.score)	
# 备注：此时不可以这样设置属性 s.set_score(60)