from selenium import  webdriver
from  selenium.webdriver.common.action_chains import ActionChains
import  time
# driver_path=r"D:\charomdriver\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.baidu.com/")
# inputtag=driver.find_element_by_id("kw")
# cliccko=driver.find_element_by_id("su")
#
# actions=ActionChains(driver)
# actions.move_to_element(inputtag)
# actions.send_keys_to_element(inputtag,"python")
# actions.move_to_element(cliccko)
# actions.click(cliccko)
# actions.perform()
#
# # 获取cook
# for  cookie in driver.get_cookies():
#     print(cookie)
# # 获取cookie值
# print(driver.get_cookie("BIDUPSID"))
# print("=="*30)
# #删除某一个cook
# driver.delete_cookie("BIDUPSID")
# # 删除所有cook
# driver.delete_all_cookies()
# for  cookie in driver.get_cookies():
#     print(cookie)

# 隐式等待
# driver_path=r"D:\charomdriver\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.douban.com/")
# driver.implicitly_wait(10)
# driver.find_element_by_name("8jhjhj")

# 切换窗口
# driver_path=r"D:\charomdriver\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.douban.com/")
# # 打开一个新的窗口
# driver.execute_script("window.open('https://www.baidu.com/')")
# print(driver.window_handles)
# # 切换到第二个串口
# driver.switch_to_window(driver.window_handles[1])
# print(driver.current_url)
# print(driver.page_source)

# 模拟滚动鼠标
driver_path=r"D:\charomdriver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)
driver.get("http://ac.qq.com/ComicView/index/id/539443/cid/1")
# driver.execute_script("""
#         (function () {
#             var y = document.body.scrollTop;
#             var step = 100;
#             window.scroll(0, y);
#             function f() {
#                 if (y < document.body.scrollHeight) {
#                     y += step;
#                     window.scroll(0, y);
#                     setTimeout(f, 50);
#                 }
#                 else {
#                     window.scroll(0, y);
#                     document.title += "scroll-done";
#                 }
#             }
#             setTimeout(f, 1000);
#         })();
#         """)
ones=driver.find_elements_by_xpath("//ul[@id='comicContain']//li")
for one in ones:
    print(one)
    driver.execute_script("arguments[0].scrollIntoView();",one)
    time.sleep(0.4)
#     # 拖动到可见的元素去
# # target = driver.find_element_by_id("mainControlNext")
# # driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
print(driver.page_source)
# while True:
#     js = "var q=document.documentElement.scrollTop=10000"
#     # js = "var q=document.body.scrollTop=10000"
#     driver.execute_script(js)
#     time.sleep(2)
