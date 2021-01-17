from lxml import etree

parser = etree.HTMLParser(encoding = "utf-8")
html = etree.parse("python爬虫28-xpath_lxml .html", parser = parser)

# 获取所有的tr标签
# xpath返回值为list
# trs = html.xpath("//tr")
# for tr in trs:
# 	print(tr)


# 获取第二个tr标签
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr, encoding = "utf-8").decode("utf-8"))


