# -*- coding: utf-8 -*-
def is_palindrome(n):
	n = str(n)
	s_len = len(n)
	# 一位长度，抛异常
	if s_len == 1:
		return False
	else :		
		ge = int(len(n)/2)
		# print('需要循环的次数：',ge)
		i = 0
		while i < ge:
			behind_index = s_len - i - 1
			# print('后对应位：',behind_index)
			# 如果对应位置上的字符不一致
			if n[i] != n[behind_index]:
				return False
			i += 1
			
		return True
		
output = filter(is_palindrome, range(1, 1000))	
print('回数有：\n',list(output))