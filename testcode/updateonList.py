#创建一个空列表
list_of_num=[]
#append()方法在列表末尾添加新元素
for i in range(0,5):    
    list_of_num.append(i)  
print(list_of_num)
#for循环，切记不要忘记冒号 : 与合理的缩进
for j in range(0,len(list_of_num)):
    square=list_of_num[j*2]**2
    #在列表任意位置插入新元素，第一个参数为插入位置索引
    list_of_num.insert((j+1)*2-1,square)
print(list_of_num)
#创建一个空列表
list_of_num_2=[]
for i in range(1,6):
    list_of_num_2.append(i)
print(list_of_num_2)
for j in range(1,len(list_of_num_2)+1):
    square=list_of_num_2[(j-1)*2]**2
    list_of_num_2.insert(j*2-1,square)
print(list_of_num_2)


#3-4
names=['zjx','hsr','zyl','zj']
for name in names:
	print("hello!"+name.title()+" welcome to my party!")
#3-5
absent_guest = 'zj'
print(absent_guest.title() +" can\'t come on time!")
#已知元素值，可使用remove()方法删除
names.remove(absent_guest)
names.append('lyy')
print(names)
#3-6
print('i find a bigger desk')
names.insert(0,'lpk')
print(names)
names.insert(len(names)//2,'wx')
print(names)
names.append('ws')
print(names)
print("welcome to my party!")
#3-7
print('sorry,i can only invite two persons')
'''
删除元素
1.使用del语句直接删除
del names[0] 语句，直接将对应元素删除且无法再访问该元素
2.使用pop()方法删除
使用pop()方法将列表末尾的元素删除/弹出，并能够使用弹出的元素
pop(n) 指定删除索引值为 n 的元素
3.根据值删除元素
remove()方法与pop()类似，可以在删除的时候使用该元素的值

'''
while len(names) != 2:
    names_pop = names.pop().upper()
    print('sorry,goodbye my darlin '+names_pop)
print(names)

