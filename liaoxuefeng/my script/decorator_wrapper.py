# -*- coding: utf-8 -*-
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():' %func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2017年1月16日 16:56:54')
		
now()		