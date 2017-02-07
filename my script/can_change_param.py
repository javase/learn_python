def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum	
print('可变参数调用：calc(1,2,3):',calc(1,2,3))	
listNumbers = [1,2,3]
print('listNumbers is %s' %listNumbers)
print('可变参数传入list calc(*listNumbers):',calc(*listNumbers))