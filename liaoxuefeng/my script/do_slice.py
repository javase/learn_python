L = list(range(100))
print('L is :',L)
print('L[0:3]:',L[0:3])
print('L[:3]:',L[:3])
print('从索引1开始取两个：L[1:3]:',L[1:3])
print('倒着取 L[:-2]:',L[:-2])
print('倒着取 L[-1:-2]:',L[-1:-2])
print('倒着取 L[-2:-1]:',L[-2:-1])
print('倒着取 L[-98:-97]:',L[-98:-97])
print('后面的数字需要比前面的大')
print('获取后10个数字：L[-10:]:',L[-10:])
print('前10到20个数字：L[10:20]:',L[10:20])
print('前20个数字，每2个取一个：L[:20:2]:',L[:20:2])
print('前50个数字，每5个取一个：L[:50:5]:',L[:50:5])
print('全部数字，每5个取一个：L[::5]:',L[::5])
print('什么都不写，复制一个List: L[:]:',L[:])
print('字符串也可以切片 \'ABCDEFG\'[:3]:','ABCDEFG'[:3])
print('\'ABCDEFG\'[::2]:','ABCDEFG'[::2])
print('倒着输出整个列表：L[::-1]:',L[::-1])
c = 'column10'
print(c[0:6])