import  pytesseract
from PIL import  Image
from  urllib import  request
import  time

# # 指定tesseract路径
# pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# # 打开图片
# image=Image.open(r"E:\爬虫强化训练\图片\a.jpg")
# text=pytesseract.image_to_string(image,lang="chi_sim")
# print(text)


# 处理拉勾网
# def main():
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     url="http://icode.renren.com/getcode.do?t=web_login&rnd=0.9768163173680533"
#     while True:
#         request.urlretrieve(url,r"E:\爬虫强化训练\图片\one.jpg")
#         image=Image.open(r"E:\爬虫强化训练\图片\one.jpg")
#         text=pytesseract.image_to_string(image)
#         print(text)
#         time.sleep(2)
# if __name__ == '__main__':
#
#     main()

sql ='10-15K'
print(type(sql))
print(sql)
sql = sql.replace('\'', '')
print(sql)
'10-15K'