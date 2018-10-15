''' 
创建基于表单的页面：
1.定义一个url
2.编写一个视图函数
3.编写一个模板
4.导入forms.py模块
'''

from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		# 根据模型Topic创建表单，该模型只包含字段text
		fields = ['text']
		# 让Django不要为text字段创建标签
		labels = {'text':''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text':''}
		# 小部件(widgets)是一个html表单元素，包括单行文本框、多行文本框、下拉列表
		widgets = {'text':forms.Textarea(attrs={'cols':80})}
