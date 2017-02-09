#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
print('os.name:',os.name) # 操作系统类型
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
# print('os.uname():',os.uname())
print('查看环境变量os.environ:',os.environ)
print('查看指定值的环境变量：os.environ.get(\'HomePath\')',os.environ.get('HomePath'))
print(r"查看当前目录的绝对路径 os.path.abspath('.'):",os.path.abspath('.'))