import pygal

from die import Die

die = Die()
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)
# print(results)

# 分析结果
# frequencies = {}
# for value in range(1, die.num_sides+1):
# 	frequency = results.count(value)
# 	frequencies[value] = frequency
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
# print(frequencies)

# 可视化结果
hist = pygal.Bar()

hist.title = "Roll die"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('die',frequencies)
hist.render_to_file("die_visual.svg")
#####################################################################
# 同时掷两个骰子
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('die',frequencies)
hist.render_to_file("dice_visual.svg")

############################################################################
# test-1
# 列表解析
die_1 = Die(10)
die_2 = Die(8)

# results = []
# for roll_num in range(1000):
# 	result = die_1.roll() + die_2.roll()
# 	results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
# 	frequency = results.count(value)
# 	frequencies.append(frequency)
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = pygal.Bar()
# hist.x_labels = [str(n) for n in range(2, max_result+1)]
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('die',frequencies)
hist.render_to_file("dice_visual.svg")






