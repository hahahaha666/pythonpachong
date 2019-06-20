# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  os
from  urllib import  request
from scrapy.pipelines.images import  ImagesPipeline
from qiche import  settings


class QichePipeline(object):
    def __init__(self):
        # 获取上上一级路径
        self.image_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"image")
        if not os.path.exists(self.image_path):
            os.mkdir(self.image_path)
        else:
            print("文件夹已存在")

    def process_item(self, item, spider):
        title=item["title"]
        urls=item["urls"]
        title_path=os.path.join(self.image_path,title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)
        else:
            print("分类文件夹已经存在")
        i=0
        for url in urls:
            image_name=str(i)+".jpg"
            request.urlretrieve(url,os.path.join(title_path,image_name))
            i+=1
        return  item
class QicheImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs=super(QicheImagePipeline, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item=item
        return request_objs

    def file_path(self, request, response=None, info=None):
        path=super(QicheImagePipeline, self).file_path(request,response,info)
        title=request.item.get('title')
        images_store=settings.IMAGES_STORE
        title_path=os.path.join(images_store,title)
        if  not os.path.exists(title_path):
            os.mkdir(title_path)
        else:
            print("文件已存在")
        image_name=path.replace("full/","")
        image_path=os.path.join(title_path,image_name)
        return  image_path



