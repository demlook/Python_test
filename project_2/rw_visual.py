import matplotlib.pyplot as plt

from random_walk import RandomWalk

# # 创建一个RandomWalk实例
# while True:
# 	rw = RandomWalk()
# 	rw.fill_walk()
# 	# 设置绘图窗口尺寸
# 	plt.figure(figsize=(10, 6))

# 	point_numbers = list(range(rw.num_points))
# 	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.viridis, s=1)

# 	# 突出显示起点
# 	plt.scatter(0, 0, c='black', s=50)
# 	# 突出显示终点
# 	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='black', s=50)

# 	# 隐藏坐标轴
# 	plt.axes().get_xaxis().set_visible(False)
# 	plt.axes().get_yaxis().set_visible(False)

# 	plt.show()

# 	keep_running = input("Make another walk? (y/n): ")
# 	if keep_running == 'n':
# 		break
##########################################################################
rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, c='red', linewidth=1)
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.viridis, s=20)


# 突出显示起点
plt.scatter(0, 0, c='black', s=50)
# 突出显示终点
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='black', s=100)

# 隐藏坐标轴
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

plt.show()
