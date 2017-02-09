#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
print('os.name:',os.name) # 操作系统类型
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
# print('os.uname():',os.uname())
print('查看环境变量os.environ:',os.environ)
print('查看指定值的环境变量：os.environ.get(\'HomePath\')',os.environ.get('HomePath'))
print(r"查看当前目录的绝对路径 os.path.abspath('.'):",os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
print(os.path.join('E:/技术/学习研究/Python/my script/','testdir'))
# 然后创建一个目录:
print(os.mkdir('E:/技术/学习研究/Python/my script/testdir'))
# 删掉一个目录:
print(os.rmdir('E:/技术/学习研究/Python/my script/testdir'))
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('E:/技术/学习研究/Python/my script/test.txt'))
# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('E:/技术/学习研究/Python/my script/test.txt'))
# 对文件重命名
try:
	os.rename('test.txt','testio.txt')
except Exception as e:
	print('rename error:',e)
	
# 删除文件
try:
	os.remove('testio.txt')
except Exception as e:
	print('del error:',e)	

print('列出当前目录下的所有目录')
print([x for x in os.listdir('.') if os.path.isdir(x)])
print('列出所有的.py文件')
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
