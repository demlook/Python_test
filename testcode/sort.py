desires=['beijing','shanghai','guangzhou','shenzhen','chengdu','chongqing']
print(desires)
#使用函数sorted()对列表临时排序
print(sorted(desires))
#反向排序
print(sorted(desires , reverse = True))
#使用reverse()方法将列表反向打印，不是反向排序
desires.reverse()
print(desires)
#再次使用反向打印，列表恢复正常
desires.reverse()
print(desires)
#使用sort()方法对列表永久排序(与sorted()临时排序不同)
desires.sort()
print(desires)
#反向排序
desires.sort(reverse=True)
print(desires)
#计算列表长度，即元素个数=最大索引数+1
print(len(desires))

#######################################################################
# 对字典排序

'''
对字典进行排序的常见形式：
sorted(dict.items(),lambda e:e[0],reverse=True)
其中，dict.items()返回一个以键值对为元组而组成的列表
e 表示dict.items()中的一个元素，e[0]表示按键排序，e[1]表示按值排序
'''

# method_1 
'''
对字典排序通用方法
'''
a = {'c':6,'g':2,'a':9,'d':3,'l':5}
print(a)
b = sorted(a.items(), key=lambda a:a[0])
print(b)  # [('a', 9), ('c', 6), ('d', 3), ('g', 2), ('l', 5)]
print(dict(b))  # {'a': 9, 'c': 6, 'd': 3, 'g': 2, 'l': 5}

# method_2

def dict_value_sort(adict):
	""" 按值排序并打印键 """
	b = adict.items()
	print(b)
	c = sorted(b,key=lambda b:b[1])
	print(c)
	return [key for key,value in c]  #返回键列表

a = {'c':6,'g':2,'a':9,'d':3,'l':5}
b = dict_value_sort(a)
print(b)

# method_3
def dict_key_sort(adict):
	""" 按键排序并打印值 """
	b = list(adict.items())  #不使用list(),将会报错：'dict_items' object has no attribute 'sort'
	print(b)
	b.sort()
	print(b)
	return [value for key,value in b]  #返回值列表

a = {'c':6,'g':2,'a':9,'d':3,'l':5}
b = dict_key_sort(a)
print(b)

# method_4
def  dict_value_sort(adict):
	""" 按键排序 """
	keys = list(adict.keys())
	keys.sort()
	return [adict[key] for key in keys]  #提取键并排序，然后按照排序的键列表打印对应值

a = {'c':6,'g':2,'a':9,'d':3,'l':5}
b = dict_value_sort(a)
print(b)  #[9, 6, 3, 2, 5]