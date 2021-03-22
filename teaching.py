import requests
import json

bilibili_api = requests.get("http://api.bilibili.com/x/relation/stat?vmid=1")  # 访问网址，数据存到变量，1是用户UID
extracting_json = bilibili_api.text  # 提取bilibili_api的text数据
python_dictionary = json.loads(extracting_json)  # json对象转换为python字典
print(python_dictionary['data']['follower'])  # 访问python对象，data里的follower
