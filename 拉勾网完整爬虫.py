import  requests
from lxml import etree
import  random
import  time
import  re

info=[]
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
def request_url():
    proxie = [
        "119.254.94.71:42788",
        "112.85.170.228:9999",
        "112.87.71.40	:9999", ]
    proxies = {
        "http": str(random.sample(proxie, 1))
    }
    #     agents = random.sample(agent, 1)
    url_start = "https://www.lagou.com/jobs/list_爬虫?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput="
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"

    for x in range(1, 2):
        data = {'first': 'true', 'pn': str(x), 'kd': '爬虫'}
        s = requests.Session()
        s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
        cookie = s.cookies  # 为此次获取的cookies
        response = s.post(url_parse, data=data, headers=headers, proxies=proxies, cookies=cookie, timeout=3)  # 获取此次文本
        time.sleep(5)
        result=response.json()
        ones=result["content"]["positionResult"]["result"]
        i=0
        for one in ones:
            positionId=one["positionId"]
            positionurl="https://www.lagou.com/jobs/%s.html"%positionId
            parse_posision_url(positionurl)
            print(positionurl)

def parse_posision_url(url):
    xinxi={}
    response=requests.get(url,headers=headers)
    two=response.text
    html=etree.HTML(two)
    title=html.xpath('//span[@class="name"]/text()')[0]
    miaoshu=html.xpath('//dd[@class="job_request"]//span')
    gongsi=html.xpath('//span[@class="name"]/text()')[1]
    gongzi=miaoshu[0].xpath('.//text()')[0].strip()
    city=miaoshu[1].xpath('.//text()')[0].strip()
    city=re.sub(r"[\s/]","",city).strip()
    jingyan=miaoshu[2].xpath('.//text()')[0].strip()
    jingyan=re.sub(r"[\s/]","",jingyan).strip()
    xueli=miaoshu[3].xpath('.//text()')[0].strip()
    xueli=re.sub(r"[\s/]","",xueli).strip()
    quanzhi=miaoshu[4].xpath('.//text()')[0].strip()
    zhiweimiaoshu="".join(html.xpath('//div[@class="job-detail"]//text()')).strip()
    xinxi={
        '公司':gongsi,
        '职位':title,
        '工资':gongzi,
        '城市':city,
        '经验':jingyan,
        '学历':xueli,
        '全职还是兼职':quanzhi,
        '职位描述':zhiweimiaoshu
    }
    info.append(xinxi)



def main():
    request_url()
    print(info)
if __name__ == '__main__':
    main()