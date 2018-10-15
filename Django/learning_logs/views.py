from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.urls import reverse(不同版本有差异)
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
	""" 学习笔记的主页 """
	return render(request, 'learning_logs/index.html')
	
'''
装饰器(decorator)是放在函数定义之前的指令，
python在函数运行前根据装饰器来修改函数代码的行为
这里用装饰器实现访问限制
@login_required将检查用户是否已登录：
如果用户已登录，才执行下面的函数；
否则，就重定向到登录页面。
重定向的实现需要在settings.py中添加LOGIN_URL = '/users/login/'

'''	
@login_required
def topics(request):
	""" 显示所有主题 """
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	# 将主题和条目存入字典context中
	context = {'topics':topics}
	# 将字典发回给模板topics.html
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	""" 显示单个主题及所有条目 """
	topic = Topic.objects.get(id=topic_id)
	# 确定请求的主题属于当前用户
	if topic.owner != request.user:
		raise Http404("你所访问的页面不存在！")
	# 按照date_added降序排列
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	""" 添加新主题 """
	if request.method != 'POST':
		# 未提交数据：创建一个新表单
		form = TopicForm()
	else:
		# POST提交的数据，对数据进行处理
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			# 使用reverse()获取页面的URL，并将其传递给HttpResponseRedirect()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	""" 在特定的主题中添加新条目 """
	topic = Topic.objects.get(id=topic_id)
	# 如果是GET请求，创建一个EntryForm实例。
	if request.method != 'POST':
		# 未提交数据，创建一个空表单
		form = EntryForm()
	else:
		# POST提交的数据，对数据进行处理
		form = EntryForm(data=request.POST)
		if form.is_valid():
			# 让Django创建一个新条目对象，存储到new_entry中，但不保存到数据库
			new_entry = form.save(commit=False)
			# 设置new_entry的属性topic
			new_entry.topic = topic
			# 把该条目保存到数据库中
			new_entry.save()
			# 将用户重定向到显示相关主题的页面，其中列表args要包含在URL中的所有实参
			return HttpResponseRedirect(reverse('learning_logs:topic',
												args=[topic_id]))
	
	context = {'topic':topic,'form':form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request,entry_id):
	""" 编辑既有条目 """
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if request.method != 'POST':
		# 初次请求，使用当前条目填充表单
		form = EntryForm(instance=entry)
	else:
		# POST提交的数据，对数据进行处理
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',
										args=[topic.id]))
	context = {'entry':entry, 'topic':topic, 'form':form}
	return render(request, 'learning_logs/edit_entry.html', context)







