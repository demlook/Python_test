# # 方法一
# import json

# from urllib.request import urlopen 

# url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
# response = urlopen(url)
# req = response.read()
# f = json.loads(req)
# print(f.keys())
#########################################################################
# # 方法二
# import requests

# # 执行API调用并存储响应
# url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
# resource = requests.get(url)
# print("Status code: ",resource.status_code)

# # 将API响应存储在一个变量中
# response_dict = resource.json()
# print(response_dict.keys())
# '''
# 其中 incomplete_results 为false表示请求成功
# 若github无法全面处理该API，则返回的值为true
# 所以在执行复杂API调用时，程序应该检查该键值

# '''
#########################################################################
import requests

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
resource = requests.get(url)
print("Status code:",resource.status_code)

# 将API响应存储在一个变量中
response_dict = resource.json()
print("Total repositories:",response_dict['total_count'])

# 搜索有关仓库信息
r_dicts = response_dict['items']
# 仓库总数
print("repositories returned:",len(r_dicts))

# 研究第一个仓库
r_dict = r_dicts[0]
# print(r_dict.keys())
print("keys:",len(r_dict))


