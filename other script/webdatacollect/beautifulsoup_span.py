# -*- coding: utf-8 -*-

from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup 

def getHtml(url): 
	try: 
		html = urlopen(url) 
	except HTTPError as e: 
		return None 
	try: 
		bsObj = BeautifulSoup(html.read(),'lxml') 
		content = bsObj
	except AttributeError as e: 
		return None 
	return content 

content = getHtml("http://www.pythonscraping.com/pages/warandpeace.html") 
# 可以获取页面中所有指定的标签
nameList = content.findAll('span',{"class":"green"})
for name in nameList:
	# 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回一个只包含文字的字符串
	print(name.get_text())