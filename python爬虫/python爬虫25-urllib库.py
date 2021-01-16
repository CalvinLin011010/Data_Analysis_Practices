# from urllib import request

# # 返回响应信息
# res = request.urlopen("http://www.baidu.com")
# print(res.getcode())

# from urllib import request

# 想把整个html页面扒下来，保存成一个文件，保存在本地

# request.urlretrieve("https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fcbu01.alicdn.com%2Fimg%2Fibank%2F2016%2F788%2F633%2F3659336887_1099643411.jpg&refer=http%3A%2F%2Fcbu01.alicdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1612771623&t=f963ec260ade850f4d15942ab3c3d505", "meihualu.jpg")




# from urllib import request
# from urllib import parse

# url = "http://www.baidu.com/s"
# data = {"wd": "痛仰乐队"}
# param = parse.urlencode(data)
# print(url + "?" + param)
# res = request.urlopen(url + "?" + param)
# # 该request返回百度搜索的痛仰乐队的html页面的所有内容
# # print(res.read())

# # parse_qs()函数可以将编码后的url参数进行解码
# s = parse.parse_qs(param)
# print(s)
# print(s.get("wd"))



"""
data = {"name": "茅台自家把持产量，跟戴比尔斯一个思路", "str": "helloworld", "age": 18}
#将data中的内容转换成url编码，并用一个变量param接收
param = parse.urlencode(data)
print(param)
"""










from urllib import parse

url = "http://www.baidu.com/s?wd=python&name=是#1"
result = parse.urlsplit(url)
print(result)

print(result.scheme)
print(result.netloc)
print(result.path)
print(result.params)
print(result.query)
print(result.fragment)