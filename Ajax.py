from selenium import  webdriver
import  time
driver_path=r"D:\charomdriver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")
inputtag=driver.find_element_by_id("kw")
inputtag.send_keys("777")
subint=driver.find_element_by_id("su0")
subint.click()
# 获取网页源代码
# print(driver.page_source)
# time.sleep(5)
# driver.close()
# time.sleep(5)
# driver.quit()

# 操作表单元素
# inputtag=driver.find_element_by_id("kw")
# inputtag.send_keys("777")
# time.sleep(5)
# inputtag.clear()


# 豆瓣操作
# driver.get("https://www.douban.com/")
# checkbooox=driver.find_element_by_id("account-form-remember")
# checkbooox.click()

# select操作
# from selenium.webdriver.support.ui import Select
# driver.get("www.dobai.cn")
# selectbn=Select(driver.find_element_by_id("jkjk"))
# # 按照第几个来
# selectbn.select_by_index("1")
# # 按照值来
# selectbn.select_by_value("你要输入的值")
# # 取消所有选中
# selectbn.deselect_all()