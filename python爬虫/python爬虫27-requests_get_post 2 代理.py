









import requests

proxy = {
	"http": "36.249.109.9:9999"
}

requests.get("https://www.12306.cn/index/", verify = False)
#                      安全证书不通过可以加 verify = false










# res = requests.get("http://httpbin.org/ip", proxies = proxy)
# print(res.content.decode("utf-8"))
# # print(res.read())  错误