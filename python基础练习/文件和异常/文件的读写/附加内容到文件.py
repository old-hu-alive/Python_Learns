# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/19 16:41
@Auth ： 小胡
@File ：附加内容到文件中.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    附加模式（'a'）打开文件时，不会清空文件的内容，而是将写入的内容添加到文件的末尾。

'''
with open('写入文件1.txt', 'a', encoding='utf8') as file_name:
    file_name.write('我用Python做测试\n')
with open('写入文件1.txt', encoding='utf8') as file_name:
    res = file_name.read()
    print(res.strip())