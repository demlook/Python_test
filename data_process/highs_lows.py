import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f_obj:
	reader = csv.reader(f_obj)
	# 获取文件的第一行
	header_row = next(reader)
	# print(header_row)
	# enumerate()获取，查看每个元素对应的索引和值
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)
	
	# 获取每天日期和最高气温
	dates = []
	highs = []
	for row in reader:
		c_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(c_date)
		highs.append(int(row[1]))

fig = plt.figure(figsize=(10,6))
plt.plot(dates, highs, c='red')
plt.title("The max temperatures of July,2014", fontsize=25)
plt.xlabel('', fontsize=15)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.show()
#####################################################################
filename = 'sitka_weather_2014.csv'
with open(filename) as f_obj:
	reader = csv.reader(f_obj)
	header_row = next(reader)

	dates = []
	highs = []
	lows = []
	for row in reader:
		c_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(c_date)
		highs.append(int(row[1]))
		lows.append(int(row[3]))

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, color='red')
plt.plot(dates, lows, color='blue')
# 填充两个y值之间的区域，alpha指定透明度
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.382)
plt.title("The max and min temperatures of 2014", fontsize=25)
plt.xlabel("Date", fontsize=15)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=15)
plt.tick_params(axis='both', labelsize=10)
plt.show()
######################################################################
# 异常处理
filename = 'death_valley_2014.csv'
with open(filename) as f_obj:
	reader = csv.reader(f_obj)
	header_row = next(reader)
	print(header_row)

	dates ,highs, lows = [], [], []
	for row in reader:
		try:
			c_date = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(c_date, 'missing data')
		else:
			dates.append(c_date)
			highs.append(high)
			lows.append(low)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, color='red')
plt.plot(dates, lows, color='blue')
# 填充两个y值之间的区域，alpha指定透明度
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.382)
plt.title("The max and min temperatures of 2014", fontsize=25)
plt.xlabel("Date", fontsize=15)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=15)
plt.tick_params(axis='both', labelsize=10)
plt.show()
