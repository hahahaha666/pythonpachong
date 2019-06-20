# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用

class BosszpPipeline(object):
    def __init__(self):
        # self.fp=open("job.json",'wb')
        # self.ex=JsonLinesItemExporter(self.fp,ensure_ascii=False)
        self.wb=workbook.Workbook("E:\kami1.xlsx")
        self.ws=self.wb.active
        self.ws.append(['电影名', '年份', '地区', '剧情类型', '导演', '主演'])

    def process_item(self, item, spider):
        # self.ex.export_item(item)
        self.ws.append(item)
        return item
    def close(self,spider):
        # self.fp.close()
        self.wb.save('test2.xlsx')