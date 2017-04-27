import math

def move(x,y,step,angle=0):
	nx = int(x) + int(step) * math.cos(angle)
	ny = int(y) + int(step) * math.sin(angle)
	return nx,ny

print('please input x:')
x = input()	
print('please input y:')	
y = input()
print('please input step:')	
step = input()
nx,ny = move(x,y,step)
print('return nx is %s,ny is %s' %(nx,ny))
print('move(x,y,step):',move(x,y,step))