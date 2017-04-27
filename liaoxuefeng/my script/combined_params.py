def f1(a,b,c=0,*args,**kw):
	print('必选参数a=%s,b=%s,默认参数c=%s,可变参数args=%s,关键字参数kw=%s' %(a,b,c,args,kw))

def f2(a,b,c=0,*,d,**kw):
	print('必选参数a=%s,b=%s,默认参数c=%s,命名关键字参数d=%s,关键字参数kw=%s' %(a,b,c,d,kw))	
	
f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)
# 命名参数，名字不对会报错：f2() missing 1 required keyword-only argument: 'd'
#f2(1,2,dd=99,ext=None) 

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
args = (1,2,3,4)
kw = {'d':100,'x':'this is x'}
f1(*args,**kw)
args = (1,2,3)
f2(*args,**kw)
