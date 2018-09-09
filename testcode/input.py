#用户输入
# message = input("What's your name? ")
# print("Hello! " + message.title())

# #使用 += 运算符用于连接多行字符串
# message = "We want to verify your personal detail.Please tell us"
# message += "\nWhat's your name? "

# name = input(message)
# print("Hello!" + name.title())
######################################################################
# #使用标志
# active = True
# while active:
# 	message = input("输入一个单词: ")
# 	if message != "quit":
# 		print(message)
# 	else:
# 		active = False
####################################################################
# #使用break退出循环
# #active = True
# while True:
# 	message = input("输入一个单词: ")
# 	if message != "quit":
# 		print(message)
# 	else:
# 		break
#####################################################################
#test-1
# import time
# while True:
# 	message = input("the topping for the pizza: ")
# 	if message:
# 		if message == "quit":
# 			break
# 		else:
# 			time.sleep(0.5)
# 			print("we have added this " + message)
# 	else:
# 		continue
#################################################################
# #test-2
# #guess number
# import random

# #使用变量active来控制循环
# active = True
# while active:
# 	num = random.randint(0,100)
# 	guess_num = input("猜一猜数字吧：")
# 	while guess_num:
# 		if guess_num == "quit":
# 			print("goodbye！")
# 			active = False
# 			break
# 		elif int(guess_num) > num:
# 			guess_num = input("猜大了，重新试一试吧！")
# 		elif int(guess_num) < num:
# 			guess_num = input("猜小了，重新试一试吧！")
# 		else:
# 			print("恭喜你，猜对了！！！")
# 			# #猜对以后退出
# 			# active = False
# 			# break
# 			#猜对以后重新产生随机数
# 			break
###############################################################
#test-3
# unregister_countries = ['China','America','Africa','Brazil','Russia']
# register_countries = []

# while unregister_countries:
# #pop()函数弹出元素并存储到另一列表中
# 	register_country = unregister_countries.pop()
# 	print("The " + register_country + " is registering!")
# 	register_countries.append(register_country)
# print("The following countries have been registered:")
# for country in register_countries:
# 	print(country)
#################################################################
# #test-4
# fruit_orders = ['apple','banana','apple','watermelon','grape','apple']

# print("Apple has been sold out!")
# # for fruit in fruit_orders:
# # 	if fruit == 'apple':
# # 		fruit_orders.remove(fruit)

# #使用while判断特定元素是否存在列表中
# while 'apple' in fruit_orders:
# 	fruit_orders.remove('apple')
# print(fruit_orders)
################################################################
# unregister_pets = {'kk':'dog','hh':'cat',
# 	'oo':'cat','papa':'fish',
# 	'qq':'dog','gg':'dog'}
# register_pets = {}

# '''
# for循环中不应修改列表或字典
# 系统将会因为无法追踪元素而报错（dictionary changed size during iteration）！！！
# '''
# while unregister_pets:
# 	for name,breed in unregister_pets.items():
# 		print("The " + breed + " "+ name.upper() + " is registering!")
# 		#为register_pets字典添加元素
# 		register_pets[name] = breed
# 	unregister_pets.clear()
# 	# print(unregister_pets)
#     # unregister_pets.pop(key) 报错
	
# for name,breed in register_pets.items():
# 	print("The " + breed + " "+ name.upper() + " has been registered!")
######################################################################
feedback = {}
active_1 = True

while active_1:
	active_2 = True
	places = [] 

	name = input("What's your name? ")
	while active_2:
		place = input("Which places would you like to visit? ")
		places.append(place)
		response_1 = input("anyplace else? ")
		if response_1 == 'no':
			active_2 = False
	feedback[name] = places

	# feedback[name] = place 当值仅为字符串时
	response_2 = input("anyone else?")
	if response_2 == 'no':
		active_1 = False

print("------Poll Result------")
for name,places in feedback.items():
	print(name.title() + " want to visit: ")
	for place in places:
		print("\t" + place.title())


# a = {
# 	'zhangsan':['bj','sh','gz'],
# 	'lisi':['bj','xy'],
# 	'wanger':['hz','sz']
# 	}

# b = ['yn','gz','sc']
# n = 'zhaowu'
# print(a)
# a[n] = b
# print(a)
