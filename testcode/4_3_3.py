#list_of_num=[num**3 for num in range(1,6)]
#print(list_of_num)
#digits=[value for value in range(1,21,2)]
#for i in range(0,len(digits)):
#    print(digits[i])

#3的倍数
#nums=[num for num in range(1,101)]
#print(nums)
#rems=[]
#for i in range(0,100):
#    rem = nums[i]%3
#    if rem == 0:
#        rems.append(nums[i])
#    i=i+1
#print(rems)

#立方
lists=[]
for x in range(1,11):
    lists.append(x**3)
print(lists[0:5])

lists_2 = [num**3 for num in range(1,11)]
print(lists_2[5:10])

