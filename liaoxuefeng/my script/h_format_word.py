# -*- coding: utf-8 -*-
def firstUpper(s):
	all = ''
	first = s[0]
	# 首字母大写
	all += first.upper()
	# 剩下的部分
	others = s[1:]
	# 转小写
	for i in others:
		all += i.lower()	
	return all
	
L1 = ['adam', 'LISA', 'barT']	
print('L1 is ',L1)
L2 = list(map(firstUpper,L1))
print('L2 is ',L2)
	
	