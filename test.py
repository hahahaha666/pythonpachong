# o=[('南北朝', '：', '谢朓'), ('唐代', '：', '崔颢'), ('宋代', '：', '晏几道'), ('唐代', '：', '高适'), ('宋代', '：', '张孝祥')]
# for i in o :
#     # print(type(i))
#     # print(i)
#     # i.replace
#     # print(' '.join(i).strip())
#     a=''.join(i)
#     print(a.strip())
import  re
from bs4 import  BeautifulSoup
from lxml import etree
text="""
<div class="contson" id="contson14ba66b5ce8a">
    <p>夕殿下珠帘，流萤飞复息。<br />长夜缝罗衣，思君此何极。</p>
</div>
            """
# soup=BeautifulSoup(text,'lxml')
soup=etree.HTML(text)
print(soup)
ret=soup.xpath('//div[@class="contson"]//text()')
print(ret)