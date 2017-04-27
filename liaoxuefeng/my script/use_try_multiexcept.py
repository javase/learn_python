# -*- coding: utf-8 -*-
try:
	print('try...')	
	# r = 10/int('a')
	r = 10/int('1')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('End')	