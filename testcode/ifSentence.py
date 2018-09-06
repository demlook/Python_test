#conditional_tests

#test-1
print("What is your favorite number?Please input a number")
favorite_num = input()
print("Can you guess the number?Please input one")
guess_num = input()
# 判断是否非空
# if guess_num:
while guess_num != None:
	if guess_num > favorite_num:
		print("so bigger, please try again")
		guess_num = input()
	elif guess_num < favorite_num:
		print("so less, please try again")
		guess_num = input()
	else:
		print("Good jod!")
		break
	
#test-2
print("please input the color of the alien") 
alien_color = input()
if alien_color == "green":
	print("You get 5 coins!")
elif alien_color == "yellow":
	print("You get 10 coins!")
else:
	print("You get 15 coins!")

#test-3
print("input your age")
age = int(input())
if age < 2:
	role = "baby"
elif age < 4:
	role = "toddle"
elif age < 13:
	role = "child"
elif age < 20:
	role = "teenager"
elif age < 65:
	role = "adult"
else:
	role = "old man"
print("you are " + role + "!")

#test-4
favorite_fruits = ["orange","apple","pear"]
if "banana" in favorite_fruits:
	print("you like banana!")
if "watermelon" in favorite_fruits:
	print("you like watermelon!")
if "orange" in favorite_fruits:
	print("you like orange!")
if "apple" in favorite_fruits:
	print("you like apple!")
if "pear" in favorite_fruits:
	print("you like pear!")

test-5
Users = ["admin","root","guest","passenger","visitor"]
print("Please input your name:")
name = input()
if name:
	if name in Users:
		if name == "admin":
			print("hello admin!would you want to see the status of the system?")
		else:
			print("hello " + name + "!thanks for logging in again!")
	else:
		print("deny access!!!")

current_users = ["admin","root","guest","passenger","visitor"]
new_users = ["RoOt","guEst","reader","cook","driver"]
for new_user in new_users:
	if new_user.lower() in current_users:
		print("please use another username!")
	else:
		print(new_user + " can be used!")

#test-6
#digits = [digit for digit in range(1,10)]
digits = list(range(1,10))
for digit in digits:
	if digit == 1:
		print("1st")
	elif digit == 2:
		print("2nd")
	elif digit == 3:
		print("3rd")
	else:
#在字符串中使用整数时，需要显式地指出你希望将整数用作字符串
#调用str()函数，将非字符串转换为字符串
		print(str(digit) + "th")



	




















