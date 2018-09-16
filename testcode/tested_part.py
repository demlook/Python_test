# # part-1
# #对函数进行测试
# def city_country(city,country,population=''):
# 	# 使用反斜杠(\)或括号让代码换行
# 	if population:
# 		c_c = city.title() + ", " + country.title() + " - " + \
# 			"population " + population
# 	else:
# 		c_c = city.title() + ", " + country.title()
# 	return c_c

# def city_country(city,country,**population):
# 	# 使用反斜杠(\)或括号让代码换行
# 	if population:
# 		c_c = city.title() + ", " + country.title() + " - " + \
# 			"population " + population
# 	else:
# 		c_c = city.title() + ", " + country.title()
# 	return c_c
###########################################################################
# part-2
# 对类进行测试
class Employee():
	def __init__(self, first_name, last_name, salary):
		self.full_name = last_name.title() + " " + first_name.title()
		self.salary = salary
		self.informations = {}
	
	def give_raise(self,increment = 5000):
		self.salary += increment

	def store_information(self):
		self.informations[self.full_name] = self.salary

	def show_information(self):
		print(self.informations)


person = Employee('san','zhang',8000)
person.give_raise()
person.store_information()
person.show_information()

person_2 = Employee('si','li',10000)
person_2.give_raise(6000)
person_2.store_information()
person_2.show_information()