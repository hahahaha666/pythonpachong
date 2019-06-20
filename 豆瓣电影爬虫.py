import  requests
from lxml import  etree

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Referer':'https://movie.douban.com/'
}
url="https://movie.douban.com/cinema/nowplaying/guangzhou/"
data=requests.get(url,headers=headers)
text=data.text
# xpath永远返回的是列表
html=etree.HTML(text)
ul=html.xpath("//ul[@class='lists']")[0]
li=ul.xpath("./li")
moviess=[]
for u in li :
    # print(etree.tostring(u,encoding="utf-8").decode("utf-8"))
    title=u.xpath("./@data-title")[0]
    data_score=u.xpath("./@data-score")[0]
    data_star=u.xpath("./@data-star")[0]
    data_actors=u.xpath("./@data-actors")[0]
    movies={
        "title":title,
        "data_score":data_score,
        "data_star":data_star,
        "data_actors":data_actors
    }
    moviess.append(movies)
print(moviess)