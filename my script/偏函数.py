# -*- coding: utf-8 -*-
print('int(\'123456\'):',int('123456'))
print('int(\'12345\',base=6):',int('12345',base=6))

def int2(x,base=2):
	return int(x,base)
	
print('int2(\'1000000\'):%s' %int2('1000000'))	

import functools
int2_f = functools.partial(int,base=2)
print('int2_f(\'1000000\'):%s' %int2_f('1000000'))	