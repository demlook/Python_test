information = {'first_name':'san','last_name':'zhang','age':20,'city':'beijing',
			# 'first_name':'si','last_name':'li','age':25,'city':'shanghai',
			# 'first_name':'er','last_name':'wang','age':30,'city':'guangzhou',
			}
print("His name is " + information['last_name'].title() + 
    information['first_name'].title() + ". He is " + str(information['age']) + 
    " years old, who lives in " + 	information['city'] + ".")

#遍历字典
favorite_num = {'zhangsan':5,'lisi':6,'wanger':8}
print(str(favorite_num['wanger']) + str(favorite_num['zhangsan']) + 
    str(favorite_num['lisi']))
# items()返回键值对列表。键值对的返回顺序与存储顺序无关
for k,v in favorite_num.items():
    print(k.title() + "'s favorite number is " + str(v))

#test-1
#词汇表
dicts = {'hello':'你好','welcome':'欢迎',
    'thank you':'谢谢','love':'爱',
    'hero':'英雄','goodbye':'再见','thanks':'谢谢'}
#遍历所有键值对
for k,v in dicts.items():
    print(k + ":" + v +";")
#遍历所有键
for k in dicts.keys():
    print(k)
#遍历所有值
for v in dicts.values():
    print(v)
#按顺序遍历字典中的所有键
for k in sorted(dicts.keys()):
    print(k + ":" + dicts[k])
#使用函数set()创建集合，去除重复元素
for v in set(dicts.values()):
    print(v)

#rivers
rivers = {
    'nile':'egypt',
    'changjiang':'china',
    'amazon':'brazil'
    }
for k,v in rivers.items():
    print("The " + k.title() + " runs through " + v.title() + ".")

#嵌套
##列表元素为字典
user_0 = {'first_name':'san','last_name':'zhang','age':20,'city':'beijing',}
user_1 = {'first_name':'si','last_name':'li','age':25,'city':'shanghai',}
user_2 = {'first_name':'er','last_name':'wang','age':30,'city':'guangzhou',}

people = [user_0, user_1, user_2]

for user in people:
    # for k,v in user.items():
    #     # print(k,v)
        full_name = user['last_name'] + " " + user['first_name']
        age = user['age']
        location = user['city']
        print("His name is " + full_name.title() + " who is " + str(age) + 
            " years old." + " He lives in " + location + ".")

#test-2
lele = {'specy':'dog','owner':'xiao ming'}
doudou = {'specy':'cat','owner':'xiao wang'}
guagua ={'specy':'dog','owner':'xiao jun'}

pets = [lele, doudou, guagua]

for i in range(0,len(pets)):
    # print("Name:" + str(pets[i]))错误
    print("\tSpecy:" + pets[i]['specy'].title())
    print("\tOwner:" + pets[i]['owner'].title())
# for pet in pets:
#     print("\tSpecy:" + pet['specy'].title())
#     print("\tOwner:" + pet['owner'].title())

##在字典中存列表
favorite_places = {
    'zhang san':['beijing','shanghai','guangzhou'],
    'li si':['yunnan','guizhou','sichuan'],
    'wang er':['hangzhou'],
    }

# #打印favorite_places的value列表
# for v in favorite_places.values():
#     for place in v:
#         print(place)
#     # for i in range(0,len(v)):
#     #     print(v[i])

for name,places in favorite_places.items():
    if len(places) != 1:
        print(name.title() + "'s favorite places are:")
        for place in places:
            print("\t" + place.title())
    else:
        print(name.title() + "'s favorite place is:" + "\n\t" + place.title())

##在字典中存字典
cities = {
    'beijing':{
        'country':'china',
        'population':'2100w',
        'describe':'capital',
        },
#字典中的逗号不能丢！！！
    'tokyo':{
        'country':'japan',
        'population':'1300w',
        'describe':'capital',
        },
    'new york':{
        'country':'america',
        'population':'850w',
        'describe':'the largest city of america',
        }
    }

for name,value in cities.items():
    print(name.title() + ":")
#访问字典内数据时，方括号内的引号不能忘！！！
    print("\tAmount of People:" + value['population'])
    print("\tDescribe:" + value['describe'])




