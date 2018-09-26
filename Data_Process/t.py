# import numpy as np
# import matplotlib.pyplot as plt


# x1 = np.linspace(0.0, 5.0)
# x2 = np.linspace(0.0, 2.0)

# y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
# y2 = np.cos(2 * np.pi * x2)

# # subplot(row, column, index)
# plt.subplot(2, 2, 1)
# plt.plot(x1, y1, '*-')
# plt.title('A tale of 2 subplots')
# plt.ylabel('Damped oscillation')

# plt.subplot(2, 2, 4)
# plt.plot(x2, y2, '.-')
# plt.xlabel('time (s)')
# plt.ylabel('Undamped')

# plt.show()
# #######################################################################
# from __future__ import (absolute_import, division, 
# 						print_function, unicode_literals)
# from urllib.request import urlopen

# import json

# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)
# # 读取数据
# req = response.read()
# # 将数据写入文件
# filename = 'btc_close_2017_urllib.json'
# with open(filename, 'wb') as f_j:
# 	f_j.write(req)
# # 加载json格式
# # file_urllib = json.loads(req)
# # print(file_urllib)

# with open(filename) as f_j:
# 	f = f_j.read()
# 	print(f)
# 	file = json.loads(f)
# 	print(file)
# #######################################################################
# # 使用request模块改进以上代码
# import requests
# import json

# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)
# with open('btc_close_2017_request.json', 'w') as f_j:
# 	f_j.write(req.text)
# # req.json()与json.loads(req)作用相同
# file_requests = req.json()
# file = json.loads(req.text)
# print(file_requests)
# ########################################################################
# 提取数据
import json
import pygal
import math

from itertools import groupby

filename = 'btc_close_2017.json'
with open(filename) as f_j:
	btc_data = json.load(f_j)
# # 打印每一天的信息
# for btc_dict in btc_data:
# 	date = btc_dict['date']
# 	month = btc_dict['month']
# 	week = btc_dict['week']
# 	weekday = btc_dict['weekday']
# 	close = btc_dict['close']
# 	print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))
	
# 将字符串转换为数值
for btc_dict in btc_data:
	date = btc_dict['date']
	month = int(btc_dict['month'])
	week = int(btc_dict['week'])
	weekday = btc_dict['weekday']
	# python不能直接将含有小数点的字符串转换为整型，需要先将字符串转换为浮点型才行
	close = int(float(btc_dict['close']))
	print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

# 绘制折线图
# 创建五个列表
dates, months, weeks, weekdays, close = [], [], [], [], []
for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))

# # import pygal
# # 让x轴的日期标签顺时针旋转20°，以及不用显示所有x轴标签
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价（￥）'
# line_chart.x_labels = dates
# N = 20
# # x轴每隔20天显示一个
# line_chart.x_labels_major = dates[::N]
# line_chart.add('收盘价', close)
# line_chart.render_to_file('收盘价折线图(￥).svg')
######################################################################
# 时间序列特征
# 半对数变换
# import math
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20
# x轴每隔20天显示一个
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图(￥).svg')
#######################################################################
# 收盘价均值
# from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
	xy_map = []
	for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
		y_list = [v for _, v in y]
		xy_map.append([x, sum(y_list) / len(y_list)])
	x_unique, y_mean = [*zip(*xy_map)]
	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.x_labels = x_unique
	line_chart.add(y_legend, y_mean)
	line_chart.render_to_file(title+'.svg')
	return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值(￥)',
							'月日均值')
line_chart_month








