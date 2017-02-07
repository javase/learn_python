# -*- coding: utf-8 -*-
def triangles():
	L = [1]
	while True:
		yield L
		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]

n = 0		
for t in triangles():
	print(t)
	n += 1
	if n == 20:
		break