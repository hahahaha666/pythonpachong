# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    title=scrapy.Field()
    content=scrapy.Field()
    id=scrapy.Field()
    url=scrapy.Field()
    author=scrapy.Field()
    avatar=scrapy.Field()
    time=scrapy.Field()
