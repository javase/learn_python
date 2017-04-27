def power(x,n=2):
	s = 1
	#print('method power()')
	if not isinstance(x,(int,float)):
		print('x type neet to convert')
		x = float(x)
	if not isinstance(n,(int)):
		print('n type neet to convert')
		n = int(n)	
	while n > 0:
		n = n - 1
		s = s*x
	return s

print('请输入x(int,float):')	
x = input()
print('请输入n(int):')	
n = input()
s = power(x,n)
print('power(x,n):%.2f' %s)
s = power(x)
print('默认参数n为2，power(x):%.2f' %s)