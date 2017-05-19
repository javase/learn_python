import urllib
from urllib.request import urlopen


try:
    html = urlopen("http://ipythonscraping.com/pages/page1.html")
except Exception as e:	
    print('打开出错',e)	
	
	
# html = urlopen("http://ipythonscraping.com/pages/page1.html")	