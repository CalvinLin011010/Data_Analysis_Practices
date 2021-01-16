# import requests
# keyword = {"wd": "痛仰乐队"}

# url = "http://www.baidu.com/s"

# # 头部信息
# headers = {
# 	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
# 	"AppleWebKit/537.36 (KHTML, like Gecko) "  # 因为太长而换行
# 	"Chrome/87.0.4280.88 Safari/537.36"
# }


# # 把头部信息放到请求中
# res = requests.get(url, params = keyword, headers = headers)
# # 所有的参数都可以往params里传  # 在这个字典里可以放很多对东西，最后往params里传参数就行

# print(res.content.decode("utf-8"))



import requests

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
	              "AppleWebKit/537.36 (KHTML, like Gecko) "
	              "Chrome/87.0.4280.88 Safari/537.36",
	"Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
}

data = {
	"first": "true",
	"pn": 1,
	"kd": "python"
}

# 发送请求————更加方便（函数名体现了请求方式，省去了写method）
res = requests.post(url, headers = headers, data = data)
#
# 对比from urllib import request下的请求方式
# req = request.Request(url, headers = headers, data = parse.urlencode(data).encode("utf-8"), method = "POST")    

print(res.content.decode("utf-8"))











