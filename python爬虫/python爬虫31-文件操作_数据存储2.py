import csv

# 申明列名（字段名/表头）
headers = ["Team", "Goals", "Shots on target"]
# 列表中以元组的形式存放
values = [
	("克罗地亚", "4", "13"),
	("Czech Republic", "4", "13"),
	("Denmark", "4", "10")
]

# 列表里面放字典或元组，
# 写爬虫取回来的数据也是以列表的形式保存的，列表里面是一个一个的字典

# csv文件，对它进行写操作，如果文件不存在就会自动创建一个
# 第一种形式
with open("demoCSV1.csv", "w", encoding = "UTF-8") as fp:
	# 希望以指定的格式往csv文件里面写东西
	# csv有固定的形式，所以引入csv模块 (import csv)
	
	# 文件名字取名为writer
	writer = csv.writer(fp)
	# 写一行，写列名（字段名/表头）
	writer.writerow(headers)
	writer.writerow(values)