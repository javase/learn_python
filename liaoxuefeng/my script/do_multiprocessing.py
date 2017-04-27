#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 备注：如果文件名为：multiprocessing，会报错：ImportError: cannot import name 'Process'
from multiprocessing import Process
import os
# 子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)...' %(name,os.getpid()))
	
if __name__ == '__main__':
	print('Parent process %s.' %os.getpid())
	p = Process(target=run_proc,args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')