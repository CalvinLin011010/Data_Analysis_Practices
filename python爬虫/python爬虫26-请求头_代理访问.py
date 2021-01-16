from urllib import request, parse  
#发起一个带有头部信息的请求
url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
# 头部信息
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"  # 有点长可以换行
	              "(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
	"Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
}
# 照抄网页positionAjax.json?....的headers里面的Form Data 格式
data = {
	"frist": "true",
	"pn": 1,
    "kd": "python"
}
# 头部信息要以字典的形式传进来 # 把请求信息都加进去
req = request.Request(url, headers = headers, data = parse.urlencode(data).encode("utf-8"), method = "POST")
#                                                            /# 编码
# 这种请求方式是get，而该信息需要用post方式请求
res = request.urlopen(req)

#read()默认读到的是字节byte，我们还需要按照utf-8 的格式把它转换成汉字才行
print(res.read().decode("utf-8"))
