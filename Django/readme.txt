1.建立虚拟环境
python -m venv ll_env
2.激活虚拟环境
source ll_env/bin/activate
或者
source ll_env/Scripts/activate
3.退出虚拟环境
deactivate
4.安装Django
pip install Django
5.创建项目
django-admin.py startproject learning_log .
6.创建数据库
python manage.py migrate
7.查看项目
python manage.py runserver
在浏览器地址输入：http://localhost:8000/
8.创建应用程序
python manage.py startapp learning_logs
9.每次修改模型时都需要三步操作：
    1) 修改model.py
    2) 对learning_logs调用makemigrations:
        python manage.py makemigrations learning_logs
    3) 让Django迁移项目:
        python manage.py migrate
