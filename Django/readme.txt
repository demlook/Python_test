1.�������⻷��
python -m venv ll_env
2.�������⻷��
source ll_env/bin/activate
����
source ll_env/Scripts/activate
3.�˳����⻷��
deactivate
4.��װDjango
pip install Django
5.������Ŀ
django-admin.py startproject learning_log .
6.�������ݿ�
python manage.py migrate
7.�鿴��Ŀ
python manage.py runserver
���������ַ���룺http://localhost:8000/
8.����Ӧ�ó���
python manage.py startapp learning_logs
9.ÿ���޸�ģ��ʱ����Ҫ����������
    1) �޸�model.py
    2) ��learning_logs����makemigrations:
        python manage.py makemigrations learning_logs
    3) ��DjangoǨ����Ŀ:
        python manage.py migrate
