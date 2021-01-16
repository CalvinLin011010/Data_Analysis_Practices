from lxml import etree

# 一般的换行每次要加\n ,太麻烦
# 太多行字符串可以用 """   """ 来赋值

text = """
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
		<td>张三</td>
		<td>20</td>
		<td>男</td>
		<td>北京市东城区</td>
	</tr>
	<tr>
		<td>1002</td>
		<td>李四</td>
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
	<tr>
		<td>1004</td>
		<td>赵六</td>
		<td>21</td>
		<td>男</td>
		<td>福建省莆田市</td>
	</tr>
</table>
"""
# 假设这份代码是我们从网页上读取的，要让程序识别并遍历

# etree对html字符串进行解析  字符串
# html = etree.HTML(text)
# print(type(html))
# print(etree.tostring(html, encoding = "utf-8").decode("utf-8"))

# 引入文件
# html = etree.parse("python爬虫28-xpath_lxml .html")
# print(type(html)) 
# print(etree.tostring(html, encoding = "utf-8").decode("utf-8"))


# 传入的惠html代码标签不一定是成对，而from lxml import etree是对xml文件进行解析的
# xml文件本身就是严格标签一对一对的
# 所以在对html文件进行解析时，最好先创建一个解析器
parser = etree.HTMLParser(encoding = "utf-8")
html = etree.parse("python爬虫28-xpath_lxml_lagou.html", parser = parser)
print(etree.tostring(html, encoding = "utf-8").decode("utf-8"))



