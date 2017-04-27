# -*- coding: utf-8 -*-
#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
def foo(s):
	return 10/int(s)
	
def bar(s):
	return foo(s)*2
	
def main():
	try:
		bar('abc')
	except Exception as e:
		print('Error:',e)
	finally:
		print('finally...')
		
main()		

# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦