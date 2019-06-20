from  selenium import  webdriver
from  lxml import  etree
import  re,time
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as  EC
from selenium.webdriver.common.by import By
class lagou(object):
    driver_path = r"D:\charomdriver\chromedriver.exe"
    options=webdriver.ChromeOptions()
    options.add_argument("--proxy-server=http://60.13.42.95:9999")
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=lagou.driver_path,chrome_options=self.options)
        self.url="https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput="

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver,timeout=5).until(EC.presence_of_element_located(By.XPATH,'//div[@class="pager_container"]/span[last()]'))
            self.pase_list(source)
            try:
                next_btn=self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
                if "pager_next_disabled" in next_btn.get_attribute("class"):
                    break
                else:
                    next_btn.click()
            except:
                print(source)
            time.sleep(1)

    def pase_list(self,source):
        html=etree.HTML(source)
        link=html.xpath('//a[@class="position_link"]/@href')
        for lin in link:
            self.parse_link(lin)
    def parse_link(self,lin):
        self.driver.execute_script("window.open('" + lin + "')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located(By.XPATH, '//span[@class="name"]/text()'))
        source=self.driver.page_source
        self.parse_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    def parse_page(self,source):
        html = etree.HTML(source)
        title = html.xpath('//span[@class="name"]/text()')[0]
        miaoshu = html.xpath('//dd[@class="job_request"]//span')
        gongsi = html.xpath('//span[@class="name"]/text()')[1]
        gongzi = miaoshu[0].xpath('.//text()')[0].strip()
        city = miaoshu[1].xpath('.//text()')[0].strip()
        city = re.sub(r"[\s/]", "", city).strip()
        jingyan = miaoshu[2].xpath('.//text()')[0].strip()
        jingyan = re.sub(r"[\s/]", "", jingyan).strip()
        xueli = miaoshu[3].xpath('.//text()')[0].strip()
        xueli = re.sub(r"[\s/]", "", xueli).strip()
        quanzhi = miaoshu[4].xpath('.//text()')[0].strip()
        zhiweimiaoshu = "".join(html.xpath('//div[@class="job-detail"]//text()')).strip()
        xinxi = {
            '公司': gongsi,
            '职位': title,
            '工资': gongzi,
            '城市': city,
            '经验': jingyan,
            '学历': xueli,
            '全职还是兼职': quanzhi,
            '职位描述': zhiweimiaoshu
        }
        print(xinxi)


if __name__ == '__main__':
    spider=lagou()
    spider.run()