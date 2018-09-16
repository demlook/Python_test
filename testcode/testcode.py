test-1
import unittest
from city_function import city_country

class CcTestCase(unittest.TestCase):

	def test_city_country_1(self):
		result = city_country('beijing','china')
		self.assertEqual(result,'Beijing,China')

	def test_city_country_2(self):
		result = city_country('tokyo','japan','80000')
		self.assertEqual(result,'Tokyo, Japan - population 80000')

	def test_city_country_3(self):
		result = city_country('tokyo','japan')
		self.assertEqual(result,'Tokyo, Japan')

unittest.main()
#############################################################################
# test-2
import unittest
from tested_part import Employee

class EmployeeTestCode(unittest.TestCase):
	def setUp(self):
		""" 使用setUp方法创建调查对象和输入，供下面测试方法使用 """
		self.person = Employee('san','zhang',8000)
		
	def test_give_default_raise(self):
		self.person.give_raise()
		self.assertEqual(self.person.salary,13000)

	def test_give_custom_raise(self):
		self.person.give_raise(3000)
		self.assertEqual(self.person.salary,11000)

unittest.main()
#############################################################################
# test-2
# 测试give_raise()函数
import unittest
from tested_part import Employee

class EmployeeTestCode(unittest.TestCase):
	def setUp(self):
		""" 使用setUp方法创建调查对象和输入，供下面测试方法使用 """
		self.person = Employee('san','zhang',8000)
		
	def test_give_default_raise(self):
		self.person.give_raise()
		self.assertEqual(self.person.salary,13000)

	def test_give_custom_raise(self):
		self.person.give_raise(3000)
		self.assertEqual(self.person.salary,11000)

unittest.main()
