from bs4 import  BeautifulSoup

# 1.获取所有tr标签
soup=BeautifulSoup("111.html",'lxml')
print(soup)
trs =soup.find_all('tr')
for tr in trs:
    print(tr)


# 2.获取第二个tr标签
tr=soup.find_all('tr',limit=2)[1]
print(tr)

# 3.获取所有class等于even的tr标签
trs=soup.find_all('tr',attrs={'class':"even"})
for tr in trs:
    print(tr)

# 4.将所有id等于test，class也等于test的a标签提取出来
aList=soup.find_all('a',id='test',calss='test')
aList=soup.find_all('a',attrs={"id":"test","class":"test"})
for a in aList:
    print(a)

# 5.获取所有a标签的href属性
aList=soup.find_all('a')
for a in aList:
    # 1.通过下表操作的方式
    href=a[href]
    print(href)
    # 2.通过attrs属性
    href=a.attrs['href']
    print(href)