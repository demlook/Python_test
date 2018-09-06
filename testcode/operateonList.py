#列表解析，将for循环与创建新元素的代码合并
list_of_num=[num**3 for num in range(1,6)]
print(list_of_num)

'''
range(m,n[,s])使用range()函数打印 m 到 n-1 的数字
也可通过参数 s 指定步长
还可以搭配list()函数将range()的结果直接转换为列表，如：
numbers = list(range(2,6))
print(numbers)
'''
digits=[value for value in range(1,21,2)]
#不知道元素个数，可以使用len()函数
for i in range(0,len(digits)):
    print(digits[i])

#求3的倍数
#nums=[num for num in range(1,101)]
#print(nums)
#rems=[]
#for i in range(0,100):
#    rem = nums[i]%3
#    if rem == 0:
#        rems.append(nums[i])
#print(rems)

#求立方,切片与复制
lists_1=[]
for x in range(1,11):
    lists_1.append(x**3)
#使用切片打印列表中索引为0,1,2,3,4的元素,以下两种方式等价
print(lists_1[0:5])
print(lists_1[:5])
#循环遍历时，直接对遍历对象进行切片
for s in lists_1[:5]:
	print(s)

#使用列表解析创建列表
lists_2 = [num**3 for num in range(1,11)]
#使用切片打印列表中索引为5,6,7,8,9的元素,以下两种方式等价
print(lists_2[5:10])
print(lists_2[5:])

#复制列表
'''
同时缺省列表的起始索引和终止索引，然后将其赋值给一个新的列表
即完成了列表的复制
注意：lists=lists_2 
不能实现列表的复制
该操作类似C语言中，两个指针指向了同一个列表
虽然有两个列表名，但实际两个变量指向的是同一个列表
对任一列表进行操作，另一个列表元素也会改变
'''
lists=lists_2[:]

#元组
'''
列表是可以修改的，然而有时需要创建一些不可修改的元素
Python将不能修改的值称为不可变的，而不可变的列表被称为元组
元组使用圆括号将元素括起来
'''
#元组，修改元组中的元素将会报错，但可以重新赋值
len_side=(55,66,77)
#列表  
len_side=[55,66,77]












