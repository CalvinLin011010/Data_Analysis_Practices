from lxml import etree

parser = etree.HTMLParser(encoding = "utf-8")
html = etree.parse("python爬虫28-xpath_lxml .html", parser = parser)


# # 获取所有tr中属性为“abc”的内容
# trs = html.xpath("//tr[@class='abc']")
# # 注意这里面的属性是单引号，如果是双引号的话电脑分不清哪些是成对的
# # print(trs)
# for tr in trs:
# 	print(etree.tostring(tr, encoding="utf-8").decode("utf-8"))


# # 获取所有a标签中的href属性
# aa = html.xpath("//a/@href")  # 记得加/  (类似路径分隔符)
#                               # 获取当前页面下所有a标签下含有hred属性的标签
# for a in aa:
# 	print(a)


# 获取所有人员的信息，一个人的信息放到一个字典中，最后将这些字典放入一个列表中
trs = html.xpath("//tr[position()>1]")  # 获取所有tr，但不包括第一行表头

infos = []
for tr in trs:   #每一个tr中 
    id = tr.xpath("./td[1]/text()")[0]
	# "."                表示在当前的目录下
	# "./td"             表示在当前的目录下寻找td标签
    # "./td[1]"          表示在当前的目录下寻找第一个td标签
    # "./td[1]/text()"   表示在当前的目录下寻找第一个td标签中的文本内容
    # print(id)
    # 注意tab键和4个空格是有区别的，尽量统一只用一种
    name = tr.xpath("./td[2]/text()")[0]
    age = tr.xpath("./td[3]/text()")[0]
    sex = tr.xpath("./td[4]/text()")[0]
    address = tr.xpath("./td[5]/text()")[0]

    info = {
        "id": id,
        "name": name,
        "age": age,
        "sex": sex,
        "address": address
    }
    
    infos.append(info)

print(infos)