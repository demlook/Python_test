# # test-1
# file_name = 'pi_million_digits.txt'
# with open(file_name) as file_object:
# 	lines = file_object.readlines()

# pi_string = ''
# for line in lines:
# 	pi_string += line.strip()

# birthday = input("Input your birthday: ")
# if birthday in pi_string:
# 	print("Congratulations!")
# else:
# 	print("Sorry!")


# # test-2
# file_name = 'pi.py'

# with open(file_name) as file_object:
# 	lines = file_object.readlines()

# t_string = ''
# for line in lines:
# 	t_string += line.strip()
# #替换字符串
# message = t_string.replace('name','nm')
# print(message)
# #################################################################
# # 统计指定路径下各文件单词数量
# from word import *

# pwd = 'ebook/'
# words_2 = Word(pwd)
# lists = words_2.tra_file()
# print(lists)
# for path in lists:
# 	# count_words(path)
# 	# 编码问题未解决！！！
# 	with open(path,'r',encoding='utf-8') as f_obj:
# 		contents = f_obj.read()
# 		# 统计指定字符出现的次数
# 		amount = contents.lower().count('love')
# 		print(amount)

####################################################################
# # 数值异常
# try:
# 	digit_1 = int(input("Please input two digits: "))
# 	digit_2 = int(input("Another one: "))
# except ValueError:
# 	print("Sorry, your input is incorrect!")
# else:
# 	num_sum = digit_1 + digit_2
# 	print(num_sum)

# # 数值异常——改进
# '''
# 如果运行 try 代码块时出现异常，程序将执行 except 代码块，不再执行 else 代码块
# 如果 try 代码块运行正常，程序紧接着将执行 else 代码块
# '''
# # 程序会在出现异常后重新开始执行 try 代码块
# while True:
# 	try:
# 		x = input("Input a number: ")
# 		if x == 'q':
# 			break
# 		x = int(x)

# 		y = input("Input another number: ")
# 		if y == 'q':
# 			break
# 		y = int(y)
# 	except ValueError:
# 		print("Please try it again!")
# 	else:
# 		num_sum = x + y
# 		print(str(x) + "+" + str(y) + "=" + str(num_sum))

######################################################################
# # 创建两个文件
# with open('cats.txt','w') as f1_obj:
# 	f1_obj.write("LiLi\n")
# 	f1_obj.write("Oreo\n")
# 	f1_obj.write("MiMi\n")

# with open('dogs.txt','w') as f2_obj:
# 	f2_obj.write("LeLe\n")
# 	f2_obj.write("DouDou\n")
# 	f2_obj.write("GuaGua\n")
# # 打印文件内容
# lists = ['cats.txt','dogs.txt']
# try:
# 	for s in lists:
# 		with open(s) as f_obj:
# 			contents = f_obj.read()
# 			print(contents.rstrip())
# except FileNotFoundError:
# 	print("Sorry,the file does not exist!")
#######################################################################
# # 存储数据
# import json

# file_name = 'username.json'
# try:
# 	with open(file_name) as f_obj:
# 		username = json.load(f_obj)
# except FileNotFoundError:
# 	username = input("What's your name? ")
# 	with open(file_name,'w') as f_obj:
# 		json.dump(username.title(),f_obj)
# 		print("Hello, " + username.title() + ", we will remember you.")
# else:
# 	print("Welcome back, " + username + " !")

#######################################################################
# # 重构
# import json

# def store_username(file_name):
# 	""" 若存在就返回用户名 """
# 	try:
# 		with open(file_name) as f_obj:
# 			username = json.load(f_obj)
# 	except FileNotFoundError:
# 		return None
# 	else:
# 		return username

# def greet_user(f_name):
# 	""" 若存在就问候用户，否则询问后创建文件 """
# 	username = store_username(f_name)
# 	if username:
# 		print("Welcome back, " + username + " !")
# 	else:
# 		username = input("What's your name? ")
# 		with open(f_name,'w') as f_obj:
# 			json.dump(username,f_obj)
# 			print("Hello, " + username.title() + ", we will remember you.")

# greet_user('us.json')


# # 重构-改进
# import json

# def store_username(file_name):
# 	""" 若存在就返回用户名 """
# 	try:
# 		with open(file_name) as f_obj:
# 			username = json.load(f_obj)
# 	except FileNotFoundError:
# 		return None
# 	else:
# 		return username

# def greet_user(f_name):
# 	""" 若存在就问候用户，否则询问后创建文件 """
# 	username = f_name.rstrip('.json')
# 	# 确定该用户名的文件是否已经创建
# 	if username == store_username(f_name):
# 		print("Welcome back, " + username.title() + "!")
# 	else:
# 		username = creat_username(f_name)
# 		print("Hello, " + username.title() + ", we will remember you.")

# 	# username = store_username(f_name)
# 	# if username:
# 	# 	print("Welcome back, " + username + " !")
# 	# else:
# 	# 	username = creat_username(f_name)
# 	# 	print("Hello, " + username.title() + ", we will remember you.")

# def creat_username(f_name):
# 	""" 提示用户输入用户名 """
# 	# 去掉字符串中指定字符（有待扩展！）
# 	username = f_name.rstrip('.json')
# 	with open(f_name,'w') as f_obj:
# 		json.dump(username,f_obj)
# 		return username

# # 创建与用户名同名文件
# fn = input("输入你的名字： ")
# greet_user(fn +'.json')
 		