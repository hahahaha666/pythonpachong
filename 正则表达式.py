import  re
# text="8798-989"
# ret=re.match("[\d\-]+",text)
# print(ret.group())

# 匹配手机号码
# text="14847832700"
# ret=re.match('1[34578]\d{9}',text)
# print(ret.group())

# 匹配邮箱
# text="1296851@qq.com"
# ret=re.match('\w+@[a-z0-9]+\.[a-z]+',text)
# print(ret.group())

#验证任意的url
# text="https://www.52pojie.cn/forum.php?mod=viewthread&tid=656217"
# ret=re.match('(http|https|ftp)://[^\s]+',text)
# print(ret.group(0))

# 替换字符
# text="https://www.52pojie.cn/forum.php?mod=viewthread&tid=656217"
# ret=re.sub('\d+',"0",text)
# print(ret)
#
html="""<asdasd>按实际大拉萨市凯迪拉克就是阿打算快乐大
        件大事空间的克拉斯卡时间段可垃圾是考虑到
        <askhd>asdasdklals;<asdkjla >
     <asdkajsda>"""

rey=re.sub("<(.*?)>","也有",html)
print(rey.strip())
#
# # split函数
# text="asdkklk371231923h131b2kj1984I&)*(J896"
# yu=re.split('[^a-zA-Z]',text)
# print(yu)

