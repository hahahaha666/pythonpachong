import  requests
import  re
from lxml import etree
from bs4 import  BeautifulSoup
def parge(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    }
    response=requests.get(url,headers=headers).content.decode("utf-8")
    gushi=[]
    zuozhew=[]
    zhengwen=[]
    title=re.compile("<b>(.*?)</b>").findall(response)
    for titl in title:
        gushi.append(titl.strip())
    zuozhes=re.compile('<p class="source">.*?<a.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<a.*?>(.*?)</a>').findall(response)
    for zuozhe in zuozhes:
        zuozhe=''.join(zuozhe)
        zuozhew.append(zuozhe )
    pat='<div class="contson".*?>(.*?)</div>'
    ppp=re.compile(pat,re.S).findall(response)
    for pp in ppp:
        # pp=pp.replace('\r','').replace('\n','').replace('\t','')
        pp=re.sub("<(.*?)>","",pp)
        zhengwen.append(pp.strip())
    all=[]
    for value in zip(gushi,zuozhew,zhengwen):
        one,two,three=value
        al={
            '题目':one,
            '作者':two,
            '诗词':three
        }
        all.append(al)
    for i in all:
        print(i)
        print("="*30)




def main():
    url="https://www.gushiwen.org/default_{}.aspx"
    for i in range(1,10):
        ur2=url.format(i)
        print(ur2)
        parge(ur2)
        print("第"+str(i)+"页")
if __name__ == '__main__':

    main()