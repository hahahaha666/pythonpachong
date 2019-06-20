import  requests

proxy={
    'http':'163.204.241.14:9999'

}

resop=requests.get("http://httpbin.org/ip",proxies=proxy)
print(resop.text)