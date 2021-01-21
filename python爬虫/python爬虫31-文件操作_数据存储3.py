import csv

headers = ["Team", "Goals", "Shots on target"]

# 列表中以字典的形式存放
values = [
	{"Team": "Germany", "Goals": "5", "Shots on target": "13"},
	{"Team": "England", "Goals": "6", "Shots on target": "15"},
	{"Team": "France", "Goals": "7", "Shots on target": "18"}
]

# 第二种形式
with open("demoCSV2.csv", "w") as fp:
	# 传入字典 dict  ，再传入headers告诉计算机传入的表头
	writer = csv.DictWriter(fp, headers)
	# 根据刚才传入的headers参数自动加入表头到创建的csv中
	writer.writeheader()
	# 写数据
	writer.writerows(values)
