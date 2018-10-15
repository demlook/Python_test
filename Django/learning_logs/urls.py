""" 定义learning_logs的url模式 """

from django.conf.urls import url

# 从当前文件所在路径下导入视图
from . import views

'''
URL模式是一个对函数url()的调用，这个函数接受三个实参。
第一个参数是一个正则表达式，正则表达式定义了Django可查找的模式。
第二个参数指定了要调用的视图函数。
第三个参数指定URL模式的名称，让我们能在代码的其他地方直接使用这个名称引用它，而不用编写URL。

'''
urlpatterns = [
	# 主页
	# 正则表达式，r让python将接下来的字符串视为原始字符串，^让python查看字符串开头，$让python查看字符串结尾
	url(r'^$', views.index, name='index'),

	# 显示所有主题
	url(r'^topics/$', views.topics, name='topics'),

	# 特定主题的详细页面
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

	# 用于添加新主题的网页
	url(r'^new_topic/$', views.new_topic, name='new_topic'),

	# 用于添加新条目的页面
	# (?P<topic_id>\d+)捕获ulr中的数字值，并存储在变量topic_id中
	# \d+与包含在两个斜杠之间的任意数字都匹配，无论有多少位
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

	# 用于编辑条目的页面
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]