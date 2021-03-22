import requests
import json
import time

# 需要修改的变量
uid = 9824766  # 用户UID
sleep_second = 60  # 多少秒检测一次
# 预定义变量 （不能修改）
assigned_value = 0  # 旧粉丝数变量是否赋值
fans_num_old = 0  # 上一次的粉丝数
while True:
    # 尝试访问链接，如果OSError输出连接失败，并break。
    try:
        bilibili_api = requests.get("http://api.bilibili.com/x/relation/stat?vmid={}".format(uid))  # 访问网址，数据存到变量
    except OSError:
        print('连接失败')
        break
    extracting_json = bilibili_api.text  # 提取bilibili_api的text数据
    python_dictionary = json.loads(extracting_json)  # json对象转换为python字典
    # 如果发送请求过多，被系统禁止获取数据，则提示并退出程序
    try:
        fans_num = python_dictionary['data']['follower']  # 粉丝数，访问python对象，data里的follower
    except TypeError:
        print('请求被拦截，需要更换IP访问')
        break
    # 判断旧粉丝数变量，是否被首次赋值
    if assigned_value != 1:
        fans_num_old = fans_num
        assigned_value = 1
    # 判断粉丝数是否变化
    if fans_num_old != fans_num:
        num_change = fans_num - fans_num_old
        num_charge_to_str = ''  # 预定义转换完的”改变多少粉丝数“变量
        if num_change > 0:  # 变化大于0就转字符串，再添加+号
            num_charge_to_str = '+' + str(num_change)
        else:
            num_charge_to_str = str(num_change)
        print('[', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '] B站粉丝数：', fans_num, '(', num_charge_to_str,
              ')',
              sep='')
        fans_num_old = fans_num  # 存储新粉丝数
    time.sleep(sleep_second)  # 每次循环检测等待秒数
