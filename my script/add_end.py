def add_end(L=[]):
	L.append('END')
	return L
	
print('add_end([1,2,3]):' , add_end([1,2,3]))	
print('add_end():',add_end())
print('add_end():',add_end())
print('add_end():',add_end())
print('我们发现当不传递参数时,L默认值进行了追加')

print('\n----------------------------------\n')

def add_end_new(L=None):
	if L is None:
		L = []
	L.append('END')	
	return L

print('add_end_new([1,2,3]):' , add_end_new([1,2,3]))	
print('add_end_new():',add_end_new())
print('add_end_new():',add_end_new())
print('add_end_new():',add_end_new())
print('改造后,L默认值没有进行追加')	