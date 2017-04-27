# -*- coding: utf-8 -*-
class Animal(object):
	def run(self):
		print('Animal is running...')
	# 此处，x并不是固定类型，只要x有run方法即可
	def run_twice(self,x):
		x.run()
		x.run()
		
class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating meat...')
	
class Cat(Animal):
	# 注意加上self关键字
	def run(self):
		print('Cat is running...')

dog = Dog()
dog.run()	
cat = Cat()
cat.run()
print('isinstance(cat,Cat):',isinstance(cat,Cat))
print('isinstance(cat,Animal):',isinstance(cat,Animal))
animal = Animal()
animal.run_twice(cat)
animal.run_twice(dog)

print('Timer没有继承Animal类，但是有run方法，也可以被传递给x参数')
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
class Timer(object):
	def run(self):
		print('Start ...')
		
class CantRun(object):
	def cantRun(self):
		print('can\'t run')
		
timer = Timer()		
animal.run_twice(timer)	
# 但是Timer类并不是Animal的子类
print('isinstance(timer,Animal):',isinstance(timer,Animal))
cantRun = CantRun()
animal.run_twice(cantRun)
# 如果传递一个没有run方法的对象，会报错“object has no attribute 'run'”
