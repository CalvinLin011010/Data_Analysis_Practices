import requests
from lxml import etree

# 1.将目标网站的页面内容抓取下来
url = "https://movie.douban.com/cinema/nowplaying/shanghai/"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
	              "AppleWebKit/537.36 (KHTML, like Gecko) "
	              "Chrome/87.0.4280.88 Safari/537.36",
	 "Referer": "https://movie.douban.com/"
}

response = requests.get(url, headers = headers)
# print(response.text)
# response 中有两个--text 和 content
# text --按照Unicode编码解码之后的字符串
# content --没有解码的数据

text = response.text
# 这就相当于获取了想要爬取的目标网页的全部内容

# 下一步就要根据爬下来的数据按照一定的规则进行提取和解析
# 所以引入解码器from lxml import etree 

# 第一步，把爬到的页面放在一个对象/节点（html）
# 便于用xpath获取里面的内容
# 想要获取的目标内容————正在上映的所有上海电影的内容
html = etree.HTML(text)

# 获取第一个ul，该ul中放的是所有的正在上映的电影
ul = html.xpath("//ul[@class='lists']")[0] 
# print(etree.tostring(ul, encoding="utf-8").decode("utf-8"))
# 范围逐步缩小，我们想要的内容在li标签中

# print(ul)

# 获取当前ul下所有的li
lis = ul.xpath("./li")

# 2.将抓下来的数据根据一定的规则进行提取解析
# 遍历循环所有的li，将想要的内容提取出来，放入一个字典中，然后将字典放入一个list
movies = []

for li in lis:
	title = li.xpath("@data-title")[0]
	score = li.xpath("@data-score")[0]
	duration = li.xpath("@data-duration")[0]
	region = li.xpath("@data-region")[0]
	director = li.xpath("@data-director")[0]
	actors = li.xpath("@data-actors")[0]
	img = li.xpath(".//img/@src")[0]
# xpath 返回的是列表，哪怕列表里面只有一个值

    # 造一个movie 的字典，把东西都放进来
	movie = {
		"title": title,
		"score": score,
 		"duration": duration,
		"region": region,
		"director": director,
		"actors": actors,
		"img": img
	}
	movies.append(movie)

# print(title)
print(movies)  














