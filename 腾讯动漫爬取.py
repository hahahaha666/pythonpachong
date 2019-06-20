from selenium import  webdriver
from  selenium.webdriver.common.action_chains import ActionChains
from lxml import  etree
from urllib import  request
import  os
import time
from queue import  Queue
import  threading


class one(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(one,self).__init__(*args,**kwargs)
        self.page_queue=page_queue
        self.img_queue=img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.par_url(url)
    def par_url(self,url):
        driver_path=r"D:\charomdriver\chromedriver.exe"
        driver=webdriver.Chrome(executable_path=driver_path)
        driver.get(url)
        i=0
        while True:
            ones=driver.find_elements_by_xpath("//ul[@id='comicContain']//li")
            for one in ones:
                # print(one)
                driver.execute_script("arguments[0].scrollIntoView();",one)
                time.sleep(0.4)
            target = driver.find_element_by_id("mainControlNext")
            driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
            data=driver.page_source
            datas=etree.HTML(data)
            url=datas.xpath("//ul[@id='comicContain']//li//img/@src")
            actions = ActionChains(driver)
            actions.move_to_element(target)
            actions.click(target)
            actions.perform()
            if not driver.find_element_by_id("mainControlNext"):
                break
            for ur in url:
                i+=1
                print(ur)
                self.img_queue.put((ur,i))


class two(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(two,self).__init__(*args,**kwargs)
        self.page_queue=page_queue
        self.img_queue=img_queue
    def run(self):

        ur,i=self.img_queue.get()
        image_name = str(i) + ".jpg"
        request.urlretrieve(ur,"表情包/"+image_name)
        print("下载完成")

def main():
    page_queue=Queue(100)
    img_queue=Queue(1000)
    url="http://ac.qq.com/ComicView/index/id/539443/cid/1"
    page_queue.put(url)
    for x in range(5):
        t=one(page_queue,img_queue)
        t.start()
    for x in range(50):
        t=two(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()
