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

