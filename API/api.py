# 方法一
import json

from urllib.request import urlopen 

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
response = urlopen(url)
req = response.read()
f = json.loads(req)
print(f.keys())
########################################################################
# 方法二
import requests

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
resource = requests.get(url)
# 状态码200 表示请求成功
print("Status code: ",resource.status_code)

# 将API响应存储在一个变量中
response_dict = resource.json()
print(response_dict.keys())
'''
其中 incomplete_results 为false表示请求成功
若github无法全面处理该API，则返回的值为true
所以在执行复杂API调用时，程序应该检查该键值

'''
########################################################################
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
resource = requests.get(url)
print("Status code:",resource.status_code)

# 将API响应存储在一个变量中
response_dict = resource.json()
# print("Total repositories:",response_dict['total_count'])

# 搜索有关仓库信息
r_dicts = response_dict['items']
# 仓库总数
# print("repositories returned:",len(r_dicts))

# 研究第一个仓库
r_dict = r_dicts[0]
# print(r_dict.keys())
# print("keys:",len(r_dict))
# for key in sorted(r_dict.keys()):
# 	print(key)

# # 打印第一个仓库的相关信息
# print("The information of the first repository:")
# print('Name:',r_dict['name'])
# print('Login Name:',r_dict['owner']['login'])
# print('Stars:',r_dict['stargazers_count'])
# print('Repository',r_dict['html_url'])
# print('Created:',r_dict['created_at'])
# print('Updated',r_dict['updated_at'])
# print('Description:',r_dict['description'])

# # 打印每一个仓库的特定信息
# print("The information of each repository:")
# for r_dict in r_dicts:
# 	print('Name:',r_dict['name'])
# 	print('Login Name:',r_dict['owner']['login'])
# 	print('Stars:',r_dict['stargazers_count'])
# 	print('Repository',r_dict['html_url'])
# 	print('Created:',r_dict['created_at'])
# 	print('Updated',r_dict['updated_at'])
# 	print('Description:',r_dict['description'],'\n')

names,stars = [],[]
for r_dict in r_dicts:
	names.append(r_dict['name'])
	stars.append(r_dict['stargazers_count'])

# 可视化
my_style = LS('#333366',base_style=LCS)
# show_legend=False 隐藏图例, x_label_rotation=45 x轴标签顺时针旋转45°
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

# hist = pygal.Bar(base_style=LCS, x_label_rotation=45, show_legend=False)
# hist.title = 'Most-starred Python Projects on GitHub'
# hist.x_labels = names
# hist.y_title = 'Stargazers Count'
# hist.add('', stars)
# hist.render_to_file('python_repos_2.svg')

# 改进pygal图表
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# 截去标签名称至15个字符
my_config.truncate_label = 15
# 隐藏y轴水平线
my_config.show_y_guides = False
# 设置图表宽度
my_config.width = 800

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos_3.svg')
############################################################################
# 添加自定义工具提示
import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['awesome-python','system-design-primer','public-apis']

plot_dicts = [
	{'value':55924,'label':'Description of awesome-python'},
	{'value':49848,'label':'Description of system-design-primer'},
	{'value':42674,'label':'Description of public-apis'},
	]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')
###########################################################################
# 对图标添加描述-改进
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
resource = requests.get(url)

response_dict = resource.json()
r_dicts = response_dict['items']

names, plot_dicts = [],[]
# plot_dict = {}

for r_dict in r_dicts:
	names.append(r_dict['name'])

	# 结果不同？？？
	# plot_dict['value'] = r_dict['stargazers_count']
	# plot_dict['label'] = r_dict['description']
	# # print(plot_dict)
	# plot_dicts.append(plot_dict)
	# print(plot_dicts)

	plot_dict = {
		'value':r_dict['stargazers_count'],
		# 报错AttributeError: 'NoneType' object has no attribute 'decode'
		# 使用str()将r_dict[]转换为str类型即可
		'label':str(r_dict['description']),
		# 为图表添加可点击的链接
		'xlink':r_dict['html_url']
		}
	plot_dicts.append(plot_dict)

my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_4.svg')
###########################################################################
import requests

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
resource = requests.get(url)
print('Status_code:', resource.status_code)

# 处理每篇文章的信息
r_ids = resource.json()
r_dicts = []
titles = []
for r_id in r_ids[:30]:
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(r_id) + '.json')
	r = requests.get(url)
	print(r.status_code)
	response_dict = r.json()
	# print(response_dict)

	r_dict = {
		'title':response_dict['title'],
		'link':'https://news.ycombinator.com/item?id=' + str(r_id),
		# 不确定某个键是否包含在字典中，可使用dict.get()方法，后一个参数指定键不存在时的返回值
		'comments':response_dict.get('descendants', 0),
		}
	r_dicts.append(r_dict)

r_dicts = sorted(r_dicts,key=itemgetter('comments'),reverse=True)

for r_dict in r_dicts:
	print('Title:', r_dict['title'])
	print('Discussion link:', r_dict['link'])
	print('Comments:', r_dict['comments'])
#############################################################################
# 可视化-改进
import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
resource = requests.get(url)
print('Status_code:', resource.status_code)

# 处理每篇文章的信息
r_ids = resource.json()
titles, plot_dicts = [],[]

for r_id in r_ids[:30]:
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(r_id) + '.json')
	r = requests.get(url)
	print(r.status_code)
	response_dict = r.json()
	# print(response_dict)
	titles.append(response_dict['title'])

	plot_dict = {
		'label':response_dict['title'],
		'xlink':'https://news.ycombinator.com/item?id=' + str(r_id),
		# 不确定某个键是否包含在字典中，可使用dict.get()方法，后一个参数指定键不存在时的返回值
		'value':response_dict.get('descendants', 0),
		}
	plot_dicts.append(plot_dict)

plot_dicts = sorted(plot_dicts,key=itemgetter('value'),reverse=True)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 800

my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Coments of the news'
chart.x_labels = titles

chart.add('',plot_dicts)
chart.render_to_file('hacker-news.svg')














