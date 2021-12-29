# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/20 23:21
@Auth ： 小胡
@File ：yaml文件.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    yaml.load(): 从yaml文件中读取数据
        yaml文件中：前面有 - 读出来为列表
                    如果是 a: 1 这样的格式，读出来是字典。
        格式：yaml.load(文件名,Loader=yaml.FullLoader)
    yaml.dump():将数据写入yaml文件
        格式：yaml.dump(要写入的数据,文件名,[allow_unicode=True])
        如果写入数据时包含中文，就要加上参数：allow_unicode=True
'''
import yaml
#读取yaml文件的内容
with open('demo1.yml',encoding='utf8') as f:
    print(yaml.load(f,Loader=yaml.FullLoader))
#将数据写入yaml文件
with open('demo2.yml','w',encoding='utf8') as f:
    yaml.dump('姓名:小小胡',f,allow_unicode=True)