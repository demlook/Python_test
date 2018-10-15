""" 为应用程序users定义URL模式 """

from django.conf.urls import url
# 导入默认视图login
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	# 登录页面
	# login表示让Django将请求发送给默认视图login
	# 视图实参为login，不是views.login
	url(r'^login/$', login, {'template_name': 'users/login.html'}, 
		name='login'),

	# 注销
	url(r'^logout/$', views.logout_view, name='logout'),

	# 注册页面
	url(r'^register/$', views.register, name='register'),

]
