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

# 上海智汇园小区的坐标查询	
content = getHtml("http://richurimo.51240.com/121.52197000000001__jw__31.077308__richurimo/") 
# 可以获取页面中所有指定的标签
# nameList = content.findAll('td',{"style":"font-weight:bold;"})

# 当天的日期
todayDate = content.find('td',{"style":"font-weight:bold;","bgcolor":"#FFFFFF"})
# 获取当天的日出时间
sunRise = content.find('td',{"style":"font-weight:bold;","bgcolor":"#D7E7A7"})
# 获取当天的日落时间
sunDown = content.find('td',{"style":"font-weight:bold;","bgcolor":"#FFC3AD"})
print('find函数返回的类型是：' ,type(sunRise))
print('[%s] 日出时间为 [%s]' %(todayDate.get_text(),sunRise.get_text()))
print('[%s] 日落时间为 [%s]' %(todayDate.get_text(),sunDown.get_text()))
