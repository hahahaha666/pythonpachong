from  lxml  import  etree

# # 解析html字符窜 使用lxml.etree.HTML进行解析
# htmlElement=etree.HTML(text)
# print(etree.tostring(htmlElement,encoding="utf-8").decode("utf-8"))
# # 解析html文件 lxml.etree.parse进行解析，
# htmlElement=etree.parse("tente.html")
# print(etree.tostring(htmlElement,encoding="utf-8").decode("utf-8"))
# # 这个函数默认使用xml解析器，所以碰到一些不规范的html代码的时候会解析错误，这个额时候我们要自己创建html解析器
# parse=etree.HTMLParser(encoding="utf-8")
# htmlElement=etree.parse("11.html",parser=parse)
# print(etree.tostring(htmlElement,encoding="utf-8").decode("utf-8"))


# 下面是示范例子
htmlElement=etree.HTMLParser(encoding="utf-8")
html=etree.parse("11.html",parser=htmlElement)

# 1.获取第2个tr标签
trs=html.xpath("//tr[2]")[0]
for tr in trs:
    print(etree.tostring(tr,encoding="utf-8").decode("utf-8"))
# 2.获取除了第一个以外所有的tr标签
trs=html.xpath("//tr[position>1]")
for tr in trs:
    # 在某个标签下，再执行xpath函数，获取这个标签下面的子孙元素
    # 那么应该在//前面加.,代表实在当前元素下获取
    href=tr.xpath(".//a/@href")