# -*- coding: utf-8 -*-
def is_palindrome(n):
	s_n = str(n)
	# 个位数，不是回数
	if len(s_n) < 2:
		return False
	# 使用python切片，如果这个字符串正着和反着是一样的，则是回数
	if s_n == s_n[::-1]:
		return True

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))	