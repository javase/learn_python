# -*- coding: utf-8 -*-
L = [36, 5, -12, 9, -21]
print('L is :',L)
print('sorted(L):',sorted(L))
print('sorted(L,key=abs):',sorted(L,key=abs))
word_l = ['bob', 'about', 'Zoo', 'Credit']
print('word_l:',word_l)
print('对字符串排序，是按照ASCII的大小比较的,sorted(word_l):',sorted(word_l))
print('忽略大小写，注意str参数名称是固定的 sorted(word_l,key=str.lower):',sorted(word_l,key=str.lower))
print('反序输出 sorted(word_l,key=str.lower,reverse = True):',sorted(word_l,key=str.lower,reverse = True))