def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)
	
def fact(n)	:
	n = int(n)
	return fact_iter(n,1)

print('请输入要阶乘的数值:')	
n = input()
print(fact(n))	