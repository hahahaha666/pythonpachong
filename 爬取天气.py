import  requests
from bs4 import  BeautifulSoup
from pyecharts import  Bar

# pip install pyecharts==0.1.9.4用这个安装才能成功

alldata=[]
def parse_page(url):
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    data=requests.get(url,headers=headers).content.decode("utf-8")
    soup=BeautifulSoup(data,'html5lib')
    # # conMidtab=soup.find_all('div',attrs={'class':"conMidtab"},limit=1)
    # # print(type(conMidtab))
    # conMidtab=conMidtab.xpath("//table")
    # print(one)
    conMidtab=soup.find('div',class_='conMidtab')
    tables=conMidtab.find_all('table')
    for table in tables:
        trs=table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds=tr.find_all('td')
            city_td=tds[0]
            if index==0:
                city_td=tds[1]
            # stripped_strings返回城市td下面所有的文本信息，返回一个生成器
            city=list(city_td.stripped_strings)[0]
            wendu_td=tds[-2]
            min_wendu=list(wendu_td.stripped_strings)[0]
            alldata.append({"city":city,"最低气温":int(min_wendu)})
            # return  alldata
            # print({"city":city,"最低气温":min_wendu})

def main():
    urls=[
        "http://www.weather.com.cn/textFC/gat.shtml",
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml"
          ]
    for url in urls:
        parse_page(url)
    # 分析数据
    # 根据最低气温排序
    alldata.sort(key=lambda  data:data["最低气温"])
    data=alldata[0:10]
    cities=list(map(lambda  x:x["city"],data))
    temps=list(map(lambda  x:x["最低气温"],data))
    chart=Bar("中国最低气温排行榜")
    chart.add('气温排行榜',cities,temps)
    chart.render("最低气温排行.html")
    print(alldata)


if __name__ == '__main__':
    main()


