""" 定义learning_logs的url模式 """

from django.conf.urls import url
# 从当前文件所在路径下导入视图
from . import views

urlpatterns = [
	# 主页
	url(r'^$', views.index, name='index'),

	# 显示所有主题
	url(r'^topics/$', views.topics, name='topics'),

	# 特定主题的详细页面
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]