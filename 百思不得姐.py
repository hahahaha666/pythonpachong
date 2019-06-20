import  threading
import  requests
from lxml import  etree
from queue import  Queue
import  csv
class Page(threading.Thread):
    def __init__(self,one_queue,two_queue,*args,**kwargs):
        super(Page,self).__init__(*args,**kwargs)
        # self.base_domain = 'http://www.budejie.com'
        self.one_queue=one_queue
        self.two_queue=two_queue
    def run(self):
        while True:
            if self.one_queue.empty():
                break
            url=self.one_queue.get()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            }
            resopnse = requests.get(url, headers=headers)
            one = resopnse.content.decode("utf-8")
            two = etree.HTML(one)
                # print(two)
            titles=two.xpath('//div[@class="j-r-list-c-desc"]')
            num=0
            for title in titles:
                pp=title.xpath('.//text()')
                pp="\n".join(pp).strip()
                print(pp)
                self.two_queue.put((pp))
                num=num+1
            print('=='*30+"第%s页下载完成！"%num+"=="*30)



class xz(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    def __init__(self,two_queue,writer,gLock,*args,**kwargs):
        super(xz,self).__init__(*args,**kwargs)
        self.two_queue=two_queue
        self.writer=writer
        self.lock=gLock

    def run(self):
        while True:
            try:
                xz_info=self.two_queue.get(timeout=40)
                info=xz_info
                self.lock.acquire()
                self.writer.writerow((info))
                self.lock.release()
                print("保存一条")
            except:
                break




def main():
    one_queue=Queue(10)
    two_queue=Queue(1000)
    gLock=threading.Lock()
    fp = open('bsbdj.csv', 'a',newline='', encoding='utf-8')
    writer = csv.writer(fp)
    for x in range(1,10):
        url="http://www.budejie.com/text/%d" %x
        one_queue.put(url)
    for x in range(5):
        t=Page(one_queue,two_queue)
        t.start()
    for i in range(5):
        t=xz(two_queue,writer,gLock)
        t.start()
if __name__ == '__main__':
    main()