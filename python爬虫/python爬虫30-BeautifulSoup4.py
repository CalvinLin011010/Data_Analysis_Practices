from bs4 import BeautifulSoup

html = """
<table border = "1" align = "center" width = "60%">
	<tr>
		<td>学号</td>
		<td>姓名</td>
		<td>年龄</td>
		<td>性别</td>
		<td>家庭住址</td>
	</tr>
	<tr>
		<td>1001</td>
		<td><a href="http://www.qunar.com" id="test" class="test">张三</a></td>
		<td>20</td>
		<td>男</td>
		<td>北京市东城区</td>
	</tr>
	<tr class="abc">
		<td>1002</td>
		<td><a href="http://www.baidu.com" id="test" class="test">李四</a></td>
		<td>18</td>
		<td>男</td>
		<td>南京市鼓楼区</td>
	</tr>
	<tr>
		<td>1003</td>
		<td>王五</td>
		<td>19</td>
		<td>女</td>
		<td>上海市宝山区</td>
	</tr>
	<tr class="abc">
		<td>1004</td>
		<td>赵六</td>
		<td>21</td>
		<td>男</td>
		<td>福建省莆田市</td>
	</tr>
</table>
"""

# 现在是html，要让python去认识它，获取它里面的数据
# 通过BeautifulSoup先一整套的解析，变成一棵完整的树(有结构了)
bs = BeautifulSoup(html, "lxml")

# （自动对齐和完善代码，源html里没有的<html></html> <body></body>,在输出中已经被补齐了）
# print(bs.prettify())


# 1.获取所有的tr标签(BeautifulSoup4语法)
trs = bs.find_all("tr")
# print(trs)
# 输出的内容被放在一个 [  ,  ,  ,  ] 内，可以理解为一个大列表
# print(type(trs))
# 输出的类型是一个结果集 <class 'bs4.element.ResultSet'>

# for tr in trs:
#     print(tr)
#     print(type(tr))
#     # 里面各个元素的数据类型<class 'bs4.element.Tag'> ，
#     # 是BeautifulSoup中自定义的类型（面向对象），不是python中的类型
#     print("="*20)  # 分割各组数据


# 2.获取第二个tr标签
# tr = bs.find_all("tr", limit = 2)[1]  # (最多)获取2个tr标签
# 用limit来限制你获取内容的个数
# print(tr)


# 3.获取所有的class="abc"的tr标签
# trs =  bs.find_all("tr", class_ = "abc")
# # class 在面向对象编程的语言中是关键字，所以要加一个下划线来区分
# # 表示是class属性里值为abc的东西
# for tr in trs:
# 	print(tr)
# 	print("=" * 20)



# 3.2第二种方法
# trs = bs.find_all("tr", attrs = {"class": "abc"})
# # attrs————attribute属性，后面 = 字典（写标签中的属性和值 
# for tr in trs: 
# 	print(tr)
# 	print("=" * 20)


# 4.将所有id = "test" 并且 class = "test" 的a标签提取出来
# alist = bs.find_all("a", id = "test", class_ = "test")
# for a in alist:
# 	print(a)


# # 4.2 第二种方法
# alist = bs.find_all("a", attrs = {"id": "test", "class": "test"})
# for a in alist:
# 	print(a)



# # 5. 获取所有a标签的bref属性
# alist = bs.find_all("a")
# # 方法1：通过索引方式获取
# for a in alist:
# 	href = a["href"]
# 	print(href)

# print('\n')

# # 方法2：通过attrs方式获取
# for a in alist:
# 	href = a.attrs["href"]
# 	print(href)


# # 6.获取所有的学生信息，将每一名学生的信息放入一个字典中，
# # 最后将所有的学生信息放入一个列表中
# trs = bs.find_all("tr")[1:] 
# # 做切片，去掉表头，从第二行开始一直取到最后

# movies = []  # 列表存储
# for tr in trs:
# 	movie = {}  # 字典
# 	tds = tr.find_all("td")
# 	stu_id = tds[0]
# 	# print(stu_id)
# 	# 如果想要去掉标签，只输出内容。可以加string
# 	# print(stu_id.string)
# 	name = tds[1]
# 	age = tds[2]
# 	sex = tds[3]
# 	address = tds[4]
# 	# 下面这样写相当于直接创建新的键值对
# 	movie["stu_id"] = stu_id.string
# 	movie["name"] = name.string
# 	movie["age"] = age.string
# 	movie["sex"] = sex.string
# 	movie["address"] = address.string
# 	movies.append(movie)
# print(movies)


# 6.获取所有的学生信息，将每一名学生的信息放入一个字典中，
# 最后将所有的学生信息放入一个列表中
# 另一个相对简单的方法
trs = bs.find_all("tr")[1:]
movies = []
for tr in trs:
	# print(tr.string)
	# info = list(tr.strings)
	# print(info) 
	# 强制转换
	# 把所有非标签的内容都取出
	movie = {}
	info = list(tr.stripped_strings)
	# print(info)
	movie["stu_id"] = info[0]
	movie["name"] = info[1]
	movie["age"] = info[2]
	movie["sex"] = info[3]
	movie["address"] = info[4]
	movies.append(movie)

print(movies)

