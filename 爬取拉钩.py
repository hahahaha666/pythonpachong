from urllib import  request,parse
url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

# 构造data伪装
data={
    'first':'true',
    'pn':'1',
    'kd':'python'
}
req=request.Request(url,headers=headers,data=parse.urlencode(data).encode("utf-8"),method='POST')
requ=request.urlopen(req)
print(requ.read().decode('utf-8'))