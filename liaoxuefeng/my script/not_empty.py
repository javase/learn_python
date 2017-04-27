def not_empty(s):
	return s and s.strip()
	
L = list(filter(not_empty,['A','b','',None,'C',' ']))	
print(L)