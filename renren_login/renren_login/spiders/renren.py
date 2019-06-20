# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url="http://www.renren.com/PLogin.do"
        data={"email":"13192272582","password":"qwer520988"}
        request=scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield  request
    def parse_page(self, response):
        with open("renren.html","w",encoding="utf-8")as fp:
            fp.write(response.text)
        requeset=scrapy.Request(url="http://www.renren.com/880151247/profile",callback=self.one)
        yield  requeset
    def one(self,response):
        with open("renrendapeng.html", "w", encoding="utf-8")as fp:
            fp.write(response.text)