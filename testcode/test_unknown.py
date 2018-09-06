#循环输入
nums = [1,2,3,4,5]
for i in range(0,5):
	nums[i] = int(input())
print(nums)

#匹配
current_users = ["admin","root","guest","passenger","visitor"]
new_users = ["RoOt","guEst","reader","cook","driver"]
for new_user in new_users:
	for current_user in current_users:
		if new_user.lower() == current_user.lower():
			print("please use another username!")
			break
		break
	print(new_user + " can be used!")