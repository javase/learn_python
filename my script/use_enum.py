# -*- coding: utf-8 -*-
# 备注 如果文件名为：enum.py，会报错：ImportError: cannot import name 'Enum'
from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in Month.__members__.items():
	print('%s => %s,%s' %(name,member,member.value))
	
@unique
class Weekday(Enum):
	Sun = 0 
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
	
# 访问枚举值
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
print('Weekday.Mon:',Weekday.Mon)	
print('Weekday[\'Tue\']:',Weekday['Tue'])
print('Weekday.Mon.value:',Weekday.Mon.value)
print('Weekday(1):',Weekday(1))
