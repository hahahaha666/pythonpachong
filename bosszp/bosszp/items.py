# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BosszpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    money=scrapy.Field()
    city=scrapy.Field()
    year=scrapy.Field()
    xuexi=scrapy.Field()
    gongsi=scrapy.Field()
