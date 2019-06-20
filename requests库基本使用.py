import  requests
# 获取网页信息text或者content。decode（）
# response=requests.get("https://www.baidu.com/")
# print(response.text)
# print(response.content.decode("utf-8"))
params={
    'wd':'英国'
}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    # 'Cookie':'anonymid=jw6ali52-qw6ldx; depovince=GUZ; _r01_=1; JSESSIONID=abcv45u4hL5Z0cQdde5Rw; ick_login=99f8241c-bfc0-4cda-9ed9-a1126aa9021e; t=dd1e75d66334a9699f53bc6ddb8c20ea3; societyguester=dd1e75d66334a9699f53bc6ddb8c20ea3; id=970973463; xnsid=6eedc27; jebe_key=5ac606a2-3b4f-4863-80e9-1f0a22bfec2e%7C5f5e2728ff534657c04151fc12f87207%7C1558956815778%7C1%7C1558956814761; XNESSESSIONID=cdf65a586a5f; jebecookies=3b4a8a1d-30fc-44c3-8fe6-fd6adc9781b7|||||; ver=7.0; loginfrom=null; wp_fold=0'
}
req=requests.get("https://www.baidu.com/s",params=params,headers=headers)
with open("baidu.html",'w',encoding="utf-8") as fp:
    fp.write(req.content.decode("utf-8"))
print(req.url)
