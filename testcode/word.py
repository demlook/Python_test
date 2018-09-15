import os

class Word():
	def __init__(self,file_path):
		# self.file_name = file_name
		self.file_path = file_path

	def tra_file(self):
		""" 遍历文件夹下的所有文件，需要导入os模块 """
		# 将指定路径下的所有文件存入path_dir列表
		path_dir = os.listdir(self.file_path)
		novel_lists = []
		# return path_dir
		# print(path_dir)
		# 打印路径下的所有文件
		for all_dir in path_dir:
			child = os.path.join('%s%s' % (self.file_path, all_dir))
			novel_lists.append(child)
		return novel_lists
		
def count_words(file_name):
	""" 统计文件单词数量 """
	try:
		with open(file_name,'rb') as file_object:
			'''
			不加参数'rb' 报错：
			'gbk' codec can't decode byte 0xbf in position 2: illegal multibyte sequence
			需进一步研究！！！
			'''
			contents = file_object.read()
	except FileNotFoundError:
		message = print(file_name + " does not exist!")
		print(message)
	else:
		words = contents.split()
		words_num = len(words)
		print("The file " + file_name + " has " + str(words_num) + " words.")
