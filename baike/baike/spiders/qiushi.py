# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from baike.items import BaikeItem

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain="https://www.qiushibaike.com"
    def parse(self, response):
        # body=response.body.decode("utf-8","ignore")
        # print(body)
        datas=response.xpath("//div[@id='content-left']/div")
        for data in datas:
            zuozhe=data.xpath(".//h2/text()").get().strip()
            wenzi=data.xpath(".//div[@class='content']//text()").getall()
            wenzi="".join(wenzi).strip()
            print(zuozhe)
            print(wenzi)
            # duanzi={"zuozhe":zuozhe,"content":wenzi}
            item=BaikeItem(zuozhe=zuozhe,content=wenzi)
            yield  item
            next_url=response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
            if not next_url:
                return
            else:
                yield  scrapy.Request (self.base_domain+next_url,callback=self.parse)