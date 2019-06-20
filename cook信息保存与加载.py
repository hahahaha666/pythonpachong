from urllib import  request
from http.cookiejar import  MozillaCookieJar

cookjar=MozillaCookieJar('cook.txt')
hanler=request.HTTPCookieProcessor(cookjar)
opener=request.build_opener(hanler)

resp=opener.open("https://www.baidu.com/")
cookjar.save()
