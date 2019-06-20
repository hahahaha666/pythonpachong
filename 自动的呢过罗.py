from  urllib import request
from  http.cookiejar import  CookieJar
from urllib import  parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
}
def get_opener():
    # 1创建一个cookiejar对象
    cookiejar=CookieJar()
    # 2使用cookiejar创建一个HTTPCookieProcessor（cookiejar）
    handler=request.HTTPCookieProcessor(cookiejar)
    # 使用上一步创建的handler创建一个opener
    opener=request.build_opener(handler)
    return  opener
# 使用opener发送人人网登陆请求

def login_renren(opener):

    data={
        'email':'13192272582',
        'password':'qwer520988'
    }
    url="http://www.renren.com/PLogin.do"
    req=request.Request(url,data=parse.urlencode(data).encode("utf-8"),headers=headers)
    opener.open(req)

def tt(opener):
    url1="http://www.renren.com/880151247/profile"
    req=request.Request(url1,headers=headers)
    resp=opener.open(url1)
    with open("大鹏.html",'w',encoding="utf-8") as fp:
        fp.write(resp.read().decode("utf-8"))


if __name__ == '__main__':
    opener=get_opener()
    login_renren(opener)
    tt(opener)