# -*- coding: utf-8 -*-
def fact(n):
    '''
	# 注意：>>> 后面有一个空格
	>>> fact(1)
	1
	>>> fact(5)
	120
	>>> fact(-1)
	Traceback (most recent call last):
	ValueError
	'''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
	
print('fact(5):',fact(5))	
