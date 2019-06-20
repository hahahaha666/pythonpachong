# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  pymysql
from pymysql import  cursors
from twisted.enterprise import  adbapi
class JianshuPipeline(object):
    def __init__(self):
        dp={
            'host':'localhost',
            'user':'root',
            'password':'123456',
            'database':'test',
            'port' : 3306,
            'charset':'utf8'
        }
        self.conn = pymysql.connect(**dp)
        self.cursor =self.conn.cursor()
        self._sql=None


    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['time'],item['id'],item['url']))
        self.conn.commit()
        print("插入一条成功")
        return item

    @property
    def sql(self):
        if not  self._sql:
            self._sql="""
            insert into xxone(id,title,content,author,avatar,time,编号,_url) values (null,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return  self._sql


class Jianhsuo(object):
    def __init__(self):
        dp={
            'host':'localhost',
            'user':'root',
            'password':'123456',
            'database':'test',
            'port' : 3306,
            'charset':'utf8',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool('pymysql',**dp)
        self._sql = None

    @property
    def sql(self):
        if not  self._sql:
            self._sql="""
            insert into xxone(id,title,content,author,avatar,time,编号,_url) values (null,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return  self._sql

    def process_item(self,item,spider):
        defer=self.dbpool.runInteraction(self.inser_item,item)
        defer.addErrback(self.handle_error,item,spider)
    def inser_item(self,cursor,item):
        cursor.excute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['time'],item['id'],item['url']))
    def handle_error(self,error,item,spider):
        print("="*30)
        print(error)
        print("=" * 30)
