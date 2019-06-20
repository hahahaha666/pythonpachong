import  requests

proxy={
    'http':'163.204.241.14:9999'
}
data={
    'first':'true',
    'pn':'1',
    'kd':'python'
}
headers={
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    # 'Cookie':'_ga=GA1.2.622895100.1558876367; _gid=GA1.2.2005222962.1558876367; user_trace_token=20190526211347-9b6344a3-7ed3-4ff0-9fd4-d999911bb0b7; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558876429,1558946573; LGUID=20190526211351-1b1b85a7-7fb8-11e9-a72c-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAAADEAAFIF1E944EB6DB082F115CD812EC316C42D; X_HTTP_TOKEN=bc6b577572fbd0708166798551e9c36d43e34e5ec9; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558976617; LGRID=20190528010338-5f2e1fd9-80a1-11e9-a789-525400f775ce; TG-TRACK-CODE=index_search; _gat=1; LGSID=20190528010338-5f2e1d93-80a1-11e9-a789-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; SEARCH_ID=80d7087ce45b40e8be88312855a14d03',
    # 'Host':'www.lagou.com',

}
respones=requests.post("https://www.lagou.com/jobs/positionAjax.json?city=广州&needAddtionalResult=false",data=data,headers=headers,proxies=proxy)
print(respones.text)