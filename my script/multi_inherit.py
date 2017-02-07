# -*- coding: utf-8 -*-
# 多重继承
class Animal(object):
	pass
	
# 大类
# 哺乳类
class Mammal(Animal):
	pass
# 鸟类	
class Bird(Animal):
	pass
	
# 各种动物
class Dog(Mammal):
	pass
	
class Bat(Mammal):
	pass 
	
class Parrot(Bird):
	pass 

# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn	
class RunnableMixIn(object):
	def run(self):
		print('Running...')
		
class FlyableMixIn(object):
	def fly(self):
		print('Flying...')
		
class Dog(Mammal,RunnableMixIn):
	pass 
	
dog = Dog()
dog.run()	