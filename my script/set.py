s1 = set([1,2,3,4])
s2 = set([2,3,5,6])
print('s1:%s' %s1)
print('s2:%s' %s2)
print('并集 s1 | s2:%s' %(s1 | s2))
print('交集 s1 & s2:%s' %(s1 & s2))

print('---------------\nput list in set ')
list = [1,2,3]
print('list:%s' %list)
print(set([1,list]))