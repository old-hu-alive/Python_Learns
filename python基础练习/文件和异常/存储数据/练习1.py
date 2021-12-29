# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/19 21:58
@Auth ： 小胡
@File ：练习1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import json
num = input('请输入您喜欢的数：')
with open('love_num.json','w',encoding='utf8') as f:
    json.dump(num,f)
with open('love_num.json',encoding='utf8') as f:
    num = json.load(f)
    print(f'我知道你喜欢的数是：{num}')