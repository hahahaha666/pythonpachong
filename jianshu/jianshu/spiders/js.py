# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.+/p/[0-9a-z]{12}.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title=response.xpath("//h1[@class='title']/text()").get()
        avatar=response.xpath("//a[@class='avatar']/img/@src").get()
        author=response.xpath("//span[@class='name']/a/text()").get()
        content=response.xpath("//div[@class='show-content-free']//p/text()").getall()
        content=",".join(content)
        time=response.xpath("//span[@class='publish-time']/text()").get()
        url=response.url
        url1=url.split("?")[0]
        id=url1.split("/")[-1]
        item=JianshuItem(
            title=title,
            avatar=avatar,
            author=author,
            content=content,
            time=time,
            url=url,
            id=id
        )
        yield  item