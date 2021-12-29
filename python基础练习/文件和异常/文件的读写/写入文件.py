# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/19 16:36
@Auth ： 小胡
@File ：写入文件.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    如果写入的文件不存在，open()将自动创建。
    以写入模式（'w'）打开文件时，如果指定的文件已经存在，Python将在返回文件对象前 清空改文件的所有内容。
    Python只能将字符串写入文本文件，如果要写入数值数据，须使用str()将其转换为字符串。
    函数write() 不会在写入的文本末尾添加换行符。
'''
with open('写入文件1.txt', 'w', encoding='utf8') as file_name:
    file_name.write('hello,world!\n')
    file_name.write('hello,china!\n')