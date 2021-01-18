#打开文件，做读取操作
data = open("demo1.txt", "r", encoding = "UTF-8")
# 相对路径



# 读取一行之后自动跳至下一行行首
# print(data.readline())  
# print(data.readline())


# 读取文件中所有内容
# print(data.read())
# 或者
#print(data.readlines()) 
# 再者
with open("demo1.txt", "r", encoding = "UTF-8") as data:
	print(data.read())


# 关闭文件
data.close()