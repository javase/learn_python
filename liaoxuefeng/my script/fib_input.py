# -*- coding: utf-8 -*-
def fib(max):
    # 默认input是str类型
    max = int(max)
    n,a,b = 1,0,1
    # max：求几个斐波那契数
    while(n <= max):
        yield b
        # 这一步很关键   f(n) = f(n-1) + f(n-2)
        # 1 1 2 3 5 8 
        a,b = b,a+b
        n += 1
    return 'done'

print('求斐波那契前N个数？请输入N：')    
max = input()
g = fib(max)
print('使用python生成器获取斐波那契前%s个数：' %max)
for n in g:
	print(n)
	
while True:
		try:
			x = next(g)
			print('g:',x)
		except StopIteration as e:
			print('Generator return value:',e.value)
			break