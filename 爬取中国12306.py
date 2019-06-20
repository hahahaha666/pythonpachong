from selenium import  webdriver


class qiangpiao(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\charomdriver\chromedriver.exe")
        self.login_url="https://kyfw.12306.cn/otn/resources/login.html"

    def login(self):
        self.driver.get(self.login_url)

    def qiang(self):
        pass

    def run(self):
        pass




if __name__ == '__main__':
    spider=qiangpiao()
    spider.run()