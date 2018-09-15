# test-1
class Restaurant():
	"""docstring for Restaurant"""
#开头和末尾两个下划线
	def __init__(self, restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("Restaurant Name:" + self.restaurant_name.title())
		print("Cuisine Type:" + self.cuisine_type)

	def open_restaurant(self):
		print("We are open!")


restaurant_1 = Restaurant('good day','Sichuan cuisine')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('old changsha','Hunan cuisine')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Sha-Xian Delicacies','Fujian cuisine')
restaurant_3.describe_restaurant()
##########################################################################
# test-2
class User():
	"""docstring for User"""
	def __init__(self,first_name,last_name,**user_info):
		self.first_name = first_name
		self.last_name = last_name
		self.user_info = user_info
		self.full_name = last_name + " " + first_name
		
	def describe_user(self):
		print("The user's profiles are as follow:")
		print("\t-Full name: " + self.full_name.title())
		for k,v in self.user_info.items():
			self.user_info[k] = v
			print("\t-" + k.title() + ": " + v)

	def greet_user(self):
		print("Hello! My dear " + self.full_name.title() + "!")

user_1 = User('san','zhang',height='180cm',weight='75kg')
user_1.greet_user()
user_1.describe_user()
user_2 = User('si','li')
user_2.greet_user()
user_2.describe_user()
user_3 = User('er','wang',favorite_fruit='strawberry')
user_3.greet_user()
user_3.describe_user()
#############################################################################
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		""" 餐馆的基本信息 """
		print("Restaurant Name:" + self.restaurant_name.title())
		print("Cuisine Type:" + self.cuisine_type)

	def open_restaurant(self):
		print("We are open!")

	def read_number_served(self):
		""" 获取餐馆的就餐人数 """
		print("We have served " + str(self.number_served) + " guestes.")

	def set_number_served(self,number):
		""" 设置就餐人数 """
		self.number_served = number

	def increment_number_served(self,increment):
		""" 使用增量对属性进行更新 """
		self.number_served += increment


restaurant_1 = Restaurant('good day','Sichuan cuisine')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
#直接通过实例修改属性值
restaurant_1.number_served = 888
restaurant_1.read_number_served()
restaurant_1.set_number_served(1200)
restaurant_1.read_number_served()
restaurant_1.increment_number_served(500)
restaurant_1.read_number_served()
############################################################################
class User():
	"""docstring for User"""
	def __init__(self, first_name,last_name,**user_info):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = last_name + " " + first_name
		self.user_info = user_info
		self.login_attempts = 0

	def describe_user(self):
		print("The user's profiles are as follow:")
		print("\t-Full name: " + self.full_name.title())
		for k,v in self.user_info.items():
			self.user_info[k] = v
			print("\t-" + k.title() + ": " + v)

	def greet_user(self):
		print("Hello! My dear " + self.full_name.title() + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempt(self):
		self.login_attempts = 0


user_1 = User('san','zhang',height='180cm',weight='75kg')
user_1.describe_user()
for i in range(0,6):
	user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempt()
print(user_1.login_attempts)
########################################################################
#继承
#test-1
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type,*flavors):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavors

	def icecream_list(self):
		print("We have some flavors below: ")
		for flavor in self.flavors:
			print("\t-" + flavor + " icecream")


icecream = IceCreamStand('snowdream','dessert','vanilla','chocolate','strawberry')
icecream.icecream_list()
icecream.number_served = 200
icecream.read_number_served()
icecream.set_number_served(1000)
icecream.read_number_served()
icecream.increment_number_served(500)
icecream.read_number_served()
############################################################################
#test-2
class Admin(User):
	def __init__(self,first_name,last_name,role,**user_info):
		super().__init__(first_name,last_name,**user_info)
		self.role = role
		self.privileges = ['can add post','can delete post','can ban user']

	def show_privileges(self):
		if self.role == 'admin':
			print("You have follow privileges:")
			for privilege in self.privileges:
				print("\t-" + privilege)
		else:
			print("You " + self.privileges[0] + "!")

user = Admin(last_name='zhang',first_name='san',role='admin')
user.describe_user()
user.show_privileges()

user_2 = Admin(last_name='zhang',first_name='san',role='guest')
user_2.show_privileges()
############################################################################
#test-3 把实例用作属性
class Privileges():
	def __init__(self,role):
		self.privileges = ['can add post','can delete post','can ban user']
		self.role = role

	def show_privileges(self):
		if self.role == 'admin':
			print("You have follow privileges:")
			for privilege in self.privileges:
				print("\t-" + privilege)
		else:
			print("You " + self.privileges[0] + "!")


class Admin(User):
	def __init__(self,first_name,last_name,role,**user_info):
		super().__init__(first_name,last_name,**user_info)
		self.role = role
		#Admin实例包含了Privileges实例
		self.privilege = Privileges(self.role)

user = Admin('san','zhang','admin',weight = '70kg')
#user通过privilege属性调用Privileges实例中的方法
user.privilege.show_privileges()
user.describe_user()

user_2 = Admin(last_name='zhang',first_name='san',role='guest')
user_2.privilege.show_privileges()

###########################################################################
# Python 标准库
# test-1
from collections import OrderedDict

favorite_singers = OrderedDict()

favorite_singers['Jack'] = 'Taylor'
favorite_singers['Tim'] = 'Justin'
favorite_singers['Bob'] = 'Rihanna'
favorite_singers['Rose'] = 'S.H.E.'

for name,singer in favorite_singers.items():
	print(name + "'s favorite singer is " + singer)

#test-2
from random import randint
class Die():
	def __init__(self,sides=6):
		self.sides = sides

	def roll_die(self):
		print(randint(1,self.sides))

dice = Die(20)
for n in range(1,11):
	dice.roll_die()

###########################################################################
'''
# 导入类
1.导入单个类
from 模块名 import 类名
2.从一个模块导入多个类
from 模块名 import 类1,类2...
3.导入整个模块
import 模块名
模块名.类名()
4.导入模块中所有类（不建议使用）
from 模块名 import *
5.从一个模块中导入另一个模块
如：子类与父类不在一个模块时，子类需要导入父类
6.类名应采用驼峰命名法（ElectricCar），即每个单词首字母都大写且不使用下划线
7.实例名和模块名都采用小写格式（add_privileges），并在单词之间添加下划线
8.先导入标准库中模块，空一行后再添加导入自己编写的模块

'''