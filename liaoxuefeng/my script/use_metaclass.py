# -*- coding: utf-8 -*-
# metaclass 是类的模版，所以必须从'type'类型派生
class ListMetaClass(type):
	# 1.当前准备创建的类的对象
	# 2.类的名字
	# 3.类继承的父类集合
	# 4.类的方法集合
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value: self.append(value)
		return type.__new__(cls,name,bases,attrs)
		
class MyList(list,metaclass=ListMetaClass):		
	pass 
	
L = MyList()
L.add(1)	
print(L)
	