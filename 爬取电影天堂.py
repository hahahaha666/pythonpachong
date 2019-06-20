import  requests
from lxml import etree
# url="https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
}
proxy={
    'https':'112.87.71.108:9999'
}
# response=requests.get(url,headers=headers)
# print(response.content.decode("gbk"))
test2=[]

for i in range(1,2):
    url="https://www.dytt8.net/html/gndy/dyzz/list_23_"+str(i)+".html"
    print(url)
    data=requests.get(url,headers=headers)
    text = data.content.decode("gbk")
    html=etree.HTML(text)
    table=html.xpath("//div[@class='co_content8']//table")
    for tabl in table:
        url1=tabl.xpath(".//a/@href")[0]
        url2="https://www.dytt8.net"+str(url1)
        print(url2)
        data2=requests.get(url2,headers=headers)
        text2 = data2.content.decode("gbk")
        html2 = etree.HTML(text2)
        info=html2.xpath("//div[@id='Zoom']//text()")
        print(type(info))
        test = {}
        # index是下标
        for index,inf in info :
            if inf.startswith("◎片　　名"):
                inf=inf.replace("◎片　　名","").strip()
                test['片名']=inf
                # print(test)
            elif inf.startswith("◎上映日期"):
                inf=inf.replace("◎上映日期","").strip()
                test['上映日期'] = inf
                # print(test)
            elif inf.startswith("◎导　　演"):
                inf = inf.replace("◎导　　演", "").strip()
                test['导演'] = inf
            elif inf.startswith("◎主　　演　"):
                inf=inf.replace("◎主　　演　","").strip()
                for x in range(index+1,len(info)):
                    a=inf[x]
                    print(a)



        # print(test)
        test2.append(test)

print(test2)

# <a href="thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5ZzQ1LmR5ZHl0dC5uZXQ6NjE2My8lRTklOTglQjMlRTUlODUlODklRTclOTQlQjUlRTUlQkQlQjF3d3cueWdkeTguY29tLiVFNiU5QyU4MCVFNCVCRCVCMyVFNyU5NCVCNyVFNSU4RiU4QiVFOCVCRiU5QiVFNSU4QyU5NiVFOCVBRSVCQS5IRC43MjBwLiVFNSU5QiVCRCVFOCVBRiVBRCVFNCVCOCVBRCVFNSVBRCU5Ny5ta3ZaWg==" target="_self" thunderpid="" thundertype="" thunderrestitle="ftp://ygdy8:ygdy8@yg45.dydytt.net:6163/阳光电影www.ygdy8.com.最佳男友进化论.HD.720p.国语中字.mkv" onclick="return OnDownloadClick_Simple(this,2);" oncontextmenu="ThunderNetwork_SetHref(this)" dxctpaft="thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5ZzQ1LmR5ZHl0dC5uZXQ6NjE2My8lRTklOTglQjMlRTUlODUlODklRTclOTQlQjUlRTUlQkQlQjF3d3cueWdkeTguY29tLiVFNiU5QyU4MCVFNCVCRCVCMyVFNyU5NCVCNyVFNSU4RiU4QiVFOCVCRiU5QiVFNSU4QyU5NiVFOCVBRSVCQS5IRC43MjBwLiVFNSU5QiVCRCVFOCVBRiVBRCVFNCVCOCVBRCVFNSVBRCU5Ny5ta3ZaWg==">ftp://ygdy8:ygdy8@yg45.dydytt.net:6163/阳光电影www.ygdy8.com.最佳男友进化论.HD.720p.国语中字.mkv</a>