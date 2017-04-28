# -*- coding: utf-8 -*-

from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup 
import re

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

# 墨迹天气获取闵行区的天气情况	
content = getHtml("https://tianqi.moji.com/today/china/shanghai/minhang-district") 

# 当天的日期
todayDate = content.find('div',{"class":"detail_time clearfix"}).get_text()
todayDate = todayDate[0:12] + todayDate[-5:-1]
# 获取当天的日出时间
sunRiseReg = re.compile("日出")
sunRise = content.find(text=sunRiseReg)
# 获取当天的日落时间
sunDown = content.find(text=re.compile("日落"))
#print('find函数返回的类型是：' ,type(sunRise))

print('[%s][%s]' %(todayDate,sunRise))
print('[%s][%s]' %(todayDate,sunDown))

