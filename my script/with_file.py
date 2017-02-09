#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
	f = open('E:/技术/学习研究/Python/my script/test.txt','r')
	# 注意： .read() 需要打印出来才可以在控制台看到输出
	print('f.read():',f.read())
finally:	
	if f:
		f.close()
		
# 更加简洁的写法
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
with open('E:/技术/学习研究/Python/my script/test.txt','r') as f:
	print('f.read():',f.read())
	
# 一行一行读取
with open('E:/技术/学习研究/Python/my script/test.txt','r') as f:
	i = 1
	for line in f.readlines():
			print('读取第%d行内容：%s' %(i,line.strip())) # 把末尾的'\n'删掉
			# i++ 不可用
			i+=1

# zhudi-02.jpg		读取二进制文件
with open('E:/技术/学习研究/Python/my script/zhudi-thumb.jpg','rb') as fb:
	for bLine in fb.readlines():
		print(bLine.strip())
		
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
# 忽略UnicodeDecodeError ： errors='ignore'
with open('E:/技术/学习研究/Python/my script/test.txt','r',encoding='gbk',errors='ignore') as f3:	
	print('f.read():',f3.read())

from datetime import datetime	
# 写文件
with open('E:/技术/学习研究/Python/my script/test.txt','w',encoding='utf-8') as fw:
	for i in range(50):
		s = '写入第' + str(i+1) + '行 '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n'
		print(s)
		fw.write(s)
