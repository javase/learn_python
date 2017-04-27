# -*- coding: utf-8 -*-
import threading,multiprocessing

def loop():
	x = 0
	while True:
		x += 1 

for i in range(4):
	print('CPU个数为：',multiprocessing.cpu_count())
	t = threading.Thread(target=loop)
	t.start()