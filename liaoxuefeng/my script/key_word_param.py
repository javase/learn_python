def person(name,age,**kw):
	print('name:%s,age:%s,other:%s' %(name,age,kw))
	
person('Jack',25)
person('Jack',25,city='上海',gender='male')
extra = {'city':'上海','gender':'male'}
print('试着传入一个dict，注意引用时需要使用两个星号。dict extra is ',extra)
person('Jack',25,**extra)