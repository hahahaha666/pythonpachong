# -*- coding: utf-8 -*-
import scrapy
from qiche.items import QicheItem


class QichezjSpider(scrapy.Spider):
    name = 'qichezj'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454507']

    def parse(self, response):
        uboxs=response.xpath("//div[@class='uibox']")
        for ubox in uboxs:
            title=ubox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls=ubox.xpath(".//ul//li/a/img/@src").getall()
            # for url in urls:
            #     # 自动拼接url 跟下面的一个意思
            #     # url=response.urljoin(url)
            #     url="https:"+url
            #     print(url)
            # 遍历出urls里面额每一项传给url 然后执行response.urljoin(url)并返回
            urls=list(map(lambda url:response.urljoin(url),urls))
            # print(urls)
            item=QicheItem(title=title,image_urls=urls)
            yield item
