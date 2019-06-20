# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  bosszp.items import BosszpItem


class ZhipingSpider(CrawlSpider):
    name = 'zhiping'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100/?query=pyhton&page=1']

    rules = (
        # 匹配列表页规则
        Rule(LinkExtractor(allow=r'.+?\query=爬虫&page=\d'), follow=True),
        # 匹配详情页规则
        Rule(LinkExtractor(allow=r'.+job_detail/.+.html'),callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        title=response.xpath("//div[@class='name']/h1/text()").get().strip()
        money = response.xpath("//div[@class='name']/span/text()").get().strip()
        info=response.xpath("//div[@class='job-primary detail-box']//div[@class='info-primary']/p/text()").getall()
        city=info[0]
        year=info[1]
        xuexi=info[2]
        gongsi=response.xpath("//div[@class='company-info']//a/@title").get().strip()
        item=BosszpItem(title=title,money=money,city=city,year=year,xuexi=xuexi,gongsi=gongsi)
        yield  item