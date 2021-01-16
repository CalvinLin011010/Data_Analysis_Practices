from urllib import request

# 没有代理的
# url = "http://httpbin.org/ip"
# res = request.urlopen(url)
# print(res.read())

# 使用代理的
url = "http://httpbin.org/ip"
# 1.使用ProxyHandler,传入代理的相应参数创建一个handler
# 参数为字典{"协议": "ip:port"}
# 
# 创建一个代理对象
handler = request.ProxyHandler({"http": "113.195.232.22:9999"})

# 光有代理还不够，还要想如何与对方的服务器建立连接
# （即代理服务器和目标服务器建立连接）
# 2.使用上买创建的handler，构建一个opener
# 我们用opener向服务器发起请求
opener = request.build_opener(handler)

# 3.使用opener发起请求
res = opener.open(url)
# 对比没有代理的情况下res = request.urlopen(url)

print(res.read())