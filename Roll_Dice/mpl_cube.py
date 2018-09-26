import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [x**3 for x in input_value]
# 设置绘制图形的输入、输出、线宽、颜色
plt.plot(input_value, squares, linewidth=5, color='gold')
# 设置标题和字号
plt.title("Cube Number", fontsize=20)
# 设置x轴
plt.xlabel("value", fontsize=15)
# 设置y轴
plt.ylabel("cube of value", fontsize=15)
# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=15, colors='blue')
plt.show()
############################################################################
x_values = list(range(1,100))
y_values = [x**3 for x in x_values]
'''
绘制散点图，其中edgecolor表示散点轮廓颜色（可设置为none）
c参数表示散点填充色，可以指定颜色或使用一个三元组(R,G,B)，元组元素取值为0~1的小数
cmp(颜色映射)，设置渐变规则，可参考
https://matplotlib.org/gallery/color/colormap_reference.html
'''
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=66)
plt.title("Cube Number", fontsize=20)
plt.xlabel("value", fontsize=15)
plt.ylabel("cube of value", fontsize=15)
'''
axis参数表示设置的适用对象，可取值x, y, both
direction表示刻度的显示位置，可取值in, out, inout
'''
plt.tick_params(axis='both', direction='inout', labelsize=15, colors='blue')
# 设置每个坐标轴的取值范围
plt.axis([0,150,0,800000])
# plt.show()
# 保存图表
plt.savefig('cube_number.png', bbox_inches='tight')
