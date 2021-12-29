# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/19 21:51
@Auth ： 小胡
@File ：json格式.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    json.dump():用来存储数据
        json.dump()接收两个实参，第一个是：要存储的数据；第二个是：存储数据的文件
    json.load():读取数据到内存中
        json.load(存储数据的文件名)
'''
import json
number = [1,2,3,4,5]
with open('number.json','w',encoding='utf8') as f:
    json.dump(number,f)
with open('number.json',encoding='utf8') as f:
    number = json.load(f)
    print(number)