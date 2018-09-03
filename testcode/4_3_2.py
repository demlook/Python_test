list_of_num=[]
for i in range(0,5):
    list_of_num.append(i)
print(list_of_num)
for j in range(0,len(list_of_num)):
    square=list_of_num[j*2]**2
    list_of_num.insert((j+1)*2-1,square)
print(list_of_num)
list_of_num_2=[]
for i in range(1,6):
    list_of_num_2.append(i)
print(list_of_num_2)
for j in range(1,len(list_of_num_2)+1):
    square=list_of_num_2[(j-1)*2]**2
    list_of_num_2.insert(j*2-1,square)
print(list_of_num_2)


