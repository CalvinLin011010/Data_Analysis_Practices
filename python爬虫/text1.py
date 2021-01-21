'''
a = 123
print(a)
print(type(a))


b = 3.14
print(b)

c = "good morning!"
print(c)
'''
"""
money = input("please input how much you want:")

max = 1000

if int(money) <= max and (int(money)%100==0):
	print("please take your money")
else:
	print("beyond max,go to make money")
"""

"""
num = input("please input nums:")
print(num)
print(type(num))
#nums=(int(num))
num = int(num)
print(num)
print(type(num))

while num != 0:
	print(num%10)
	num //= 10
str
#while num != NULL:
"""
"""
b = "2"

c = int(b) + 10
print(c) 

s = 123456
v = list(str(s))
print(v)

# list(ww)

for item in v:
    #item = int(item) + 10
    ww = int(item) + 10

print(v)
print(ww)
ss = v.copy()
print(ss)

l = [1, 2, 3, 4, 5, 6]
print(l)
for item in l:
	item = item + 10
print(l)

"""



"""
l1 = [1, 2, 3, 4, 5, 6]
########法1
def test_map(array):
	# temp = [1, 2, 3, 4, 5, 6, ]
	# 创建一个新列表
	temp = []
	# 遍历传入的列表
	for item in array:
		# 将源列表中的每一个元素执行+10操作
		temp.append(item + 10)  # 注意这里的append 后面接的是 () ，不是 [] .  这是列表，不是字典
		# 注意函数不能当字典用，不然会返回'builtin_function_or_method' object is not subscriptable
	return temp 

c =test_map(l1)
print(c)

########法2
def test_map2(array, func):
	temp = []
	for item in array:
		temp.append(func(item))
	return temp

v = test_map2(l1, lambda x: x + 10)
print(v)

#######法3m 
vv = map(lambda x: x + 10, l1)
print(type(vv))  # map
print(list(vv))


#####################
#####################

movie = ["欧美:beauty", "国产:你好", "欧美:pljj", "国产:桃花侠"]

# vw = map(lambda x : x.values(), dic)
# print(list(vw))

def test_map3(array):
	temp = []
	for item in array:
		temp.append(item[item.find(":")+1:])
	return temp

vvv = test_map3(movie)
print(vvv)

# map 可以对某一个列表中的每一个元素进行操作，
# 并把操作过后的值返回过来，组成一个新的列表，并返回一个object
vvvv = map(lambda x : x[x.find(":")+1:], movie)
print(vvvv)  #map返回的object需要强制类型转换再输出
print(list(vvvv))
"""

# 2021.01.01
dic = {"name":"张飞", "age":"31", "hometown":"涿州", "weapon":"蛇矛"}

print(dic)
print(type(dic))
 
 # 获取某一个key对应的值，可以使用索引
print(dic["name"])
print(dic["weapon"])

# 默认情况下字典在for循环中获取的是key
for item in dic:
	print(item)

for item in dic.keys():
	print(item)

for item in dic.items():
	print(item)

print(dic)

dic.popitem()
print(dic)

print(dic.get("weapon"))

print(dic["age"])
print(dic["hometown"])
# print(dic["weapon"])
dic["name"] = "关羽"
print(dic["name"])


v = dict.fromkeys(["a", "b", "c"])
print(v)

v = dict.fromkeys(["A", "B", "C"], 12345)
print(v) 