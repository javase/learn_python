#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
d = dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))

with open('dump.txt','wb') as f:
	pickle.dump(d,f)
	
with open('dump.txt','rb') as f:
	print('读取dump.txt的内容：\n%s' %f.read())
	
with open('dump.txt','rb')	as f:
	d = pickle.load(f)
	print('反序列化 pickle.load(f): %s\n反序列化后的对象类型是：%s' %(d,type(d)))	

print('\n\n\njson')	
import json 
print('json.dumps(d):',json.dumps(d))	
print('type(json.dumps(d)):',type(json.dumps(d)))	
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换
json_str = json.dumps(d)
print('json.loads(json_str):',json.loads(json_str))
print('type(json.loads(json_str)):',type(json.loads(json_str)))

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
	def __str__(self):
		return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)
		
s = Student('Jack',20,90)
# 把任意class的实例变为dict		
print('json.dumps(s):',json.dumps(s,default=lambda obj:obj.__dict__))

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])
	
print('把json转为Student类型：',json.loads(json_str,object_hook=dict2student))	