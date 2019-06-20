# import  requests
# from lxml import  etree
# from  urllib import request
# import  os
# import  re
# from queue import  Queue
# import  threading
#
# class Producter(threading.Thread):
#     def __init__(self,page_queue,img_queue,*args,**kwargs):
#         super(Producter,self).__init__(*args,**kwargs)
#         self.page_queue=page_queue
#         self.img_queue=img_queue
#     def run(self):
#         while True:
#             if self.page_queue.empty():
#                 break
#             url=self.page_queue.get()
#             self.parse_url(url)
#     def parse_url(self,url):
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
#         }
#         resopnse=requests.get(url,headers=headers)
#         one=resopnse.content.decode("utf-8")
#         two=etree.HTML(one)
#         titles=two.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
#         for title in titles:
#             img_url=title.get("data-original")
#             tou=title.get("alt")
#             alt=re.sub(r'[\?？\.，。！!\/\*]','',tou)
#             suffix=os.path.splitext(img_url)[1]
#             three=tou+suffix
#             self.img_queue.put((img_url,three))
#
# class xiaofeizhe(threading.Thread):
#     def __init__(self,page_queue,img_queue,*args,**kwargs):
#         super(xiaofeizhe,self).__init__(*args,**kwargs)
#         self.page_queue=page_queue
#         self.img_queue=img_queue
#     def run(self):
#         while True:
#             if self.img_queue.empty() and self.page_queue.empty():
#                 break
#             img_url,three=self.img_queue.get()
#             request.urlretrieve(img_url,'表情包/'+three)
#             print(three+"下载完成")
#
# def main():
#     page_queue=Queue(100)
#     img_queue=Queue(1000)
#     for x in range(0,100):
#         url="http://www.doutula.com/photo/list/?page=%d" %x
#         page_queue.put(url)
#     for x in range(5):
#         t=Producter(page_queue,img_queue)
#         t.start()
#     for x in range(5):
#         t=xiaofeizhe(page_queue,img_queue)
#         t.start()
# if __name__ == '__main__':
#     main()


i=0
while True:
    i+=1
    if i==9:
        break
    # return i
print(i)