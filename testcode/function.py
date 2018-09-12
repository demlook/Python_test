#函数
def favorite_book(book):
	print("One of my favorite book is " + book + ".")

favorite_book('Alice in Wonderland')
###############################################
# 1 位置实参，顺序必须与形参一致
def make_shirt(size,phrase):
	print("This T-shirt's size is " + size + ".")
	print("Imprinted phrase is " + "\"" + phrase + "\"")

make_shirt('L','hello world!')

# 2 关键字实参，顺序无关
def make_shirt(size,phrase):
	print("This T-shirt's size is " + size + ".")
	print("Imprinted phrase is " + "\"" + phrase + "\"")

make_shirt(phrase='hello world!',size='XL')

# 3 使用默认值，有默认值的形参必须放形参列表最后
def make_shirt(size,phrase,color='white'):
	print("This " + color + " T-shirt's size is " + size + ".")
	print("Imprinted phrase is " + "\"" + phrase + "\"")

make_shirt('L','hello world!')
make_shirt('XL','smile','black')
###########################################################
def city_country(city,country):
	return city.title() + "," + country.title()

print(city_country('beijing','China'))
print(city_country('tokyo','Japen'))
print(city_country('new york','America'))

##########################################################
def make_album(name_1,name_2,number=''):
	# music_albums = {}
	# music_albums['singer'] = name
	music_albums = {'singer':name_1,'album_name':name_2}
	if number:
		music_albums['amount'] = number
	return music_albums

while True:
	print("You can enter 'q' to quit at any time!")

	s_name = input("What's the singer's name? ")
	if s_name == 'q':
		break

	a_name = input("What about the name of the music album? ")
	if a_name == 'q':
			break

	album_1 = make_album(s_name,a_name)
	print(album_1)
###############################################################
def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	for n in range(0,len(magicians)):
		magicians[n] = "the Great " + magicians[n]
	return magicians
	'''
	for magician in magicians:
		magician = "the Great " + magician
	for magician in magicians:
		print(magician)
	该方式并不能修改列表元素，只能通过索引修改
	'''
	
names = ['zhangsan','lisi','wangwu']
names_2 = []
# 使用切片表示法为 names 列表创建副本
names_2 = make_great(names[:])
show_magicians(names_2)
show_magicians(names)
#####################################################################
#传递任意数量的实参
'''
*topping 使用*号 让python创建一个名为topping的空元组，
并将收到的所有值都封装到这个元组中
'''
def make_sandwich(*toppings):
	print("You order the sandwich with:")
	for topping in toppings:
		print("-" + topping)


make_sandwich('tomato','egg','ham')
make_sandwich('egg')
make_sandwich('meat','fruit','tomato','pepper')

#使用任意数量关键字实参
'''
**user_info **让python创建名为user_info的字典，
并将接收到的所有 名称-值 对封装到字典里
'''
# 1
def build_profile(first,last,**user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last

	for key,value in user_info.items():
		profile[key] = value

	return profile

user_profile = build_profile('san','zhang',weight='70kg',location='China')
print(user_profile)

# 2
def make_profile(manufacturer,model_num,**car_info):
	profile = {}
	profile['manufacturer'] = manufacturer
	profile['model_num'] = model_num

	for k,v in car_info.items():
		profile[k] = v

	return profile

car_profile = make_profile('Volkswagen','SUV',calor='black',price='12w-20w')
print(car_profile)
########################################################################
#将函数存入模块

#1 导入整个模块
#指定导入模块名称和模块内函数名，并用 . 连接
import printing_function

user_profile = printing_function.build_profile('san','zhang',weight='70kg',location='China')
print(user_profile)

#2 导入特定函数
#from 模块名 import 函数名,调用函数时可以不使用模块名和 .
from printing_function import build_profile

user_profile = build_profile('si','li',weight='60kg',location='China')
print(user_profile)

#3 使用as给函数和模块指定别名
import printing_function as pf

user_profile = pf.build_profile('san','zhang',weight='70kg',location='China')
print(user_profile)

from printing_function import build_profile as bp

user_profile = bp('si','li',weight='60kg',location='China')
print(user_profile)
####################################################################
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

#####################################################################
'''
注意事项：
1.from 模块名 import * ,可以导入模块中的所有函数，且无需使用点号(.)表示法。
然而，如果模块中存在函数名称与本项目中函数名称相同的情况，则可能会导致意料之外的结果。
要么只导入需要使用的函数，要么使用点号(.)表示法。
2.函数应使用描述性名称，且仅使用小写字母和下划线构成
3.给形参或者实参指定默认值时，等号两边不应有空格。
4.参数列表过长时使用换行，如
def function(
		p_1,p_2,p_3,
		p_4,p_5):
	function body...

'''