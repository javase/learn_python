# -*- coding: utf-8 -*-
class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('diy error invalid value:%s' %s)
	return 10/n	
	
foo('0')	
# 尽量使用Python内置的错误类型