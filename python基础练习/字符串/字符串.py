# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/24 21:39
@Auth ： 小胡
@File ：字符串.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
#统计字符串中指定字符出现的个数：count() 方法   字符串.count（）
str = 'java'
count_num = str.count('a')
print(f'字符串中"a"的个数是：{count_num}')
# 字符串方法：title() --- 将单词首字母转换为大写
name = 'hu yun feng'
print(name.title())

#字符串方法：upper() ---将字符串全部转换为大写
#字符串方法：lower() ---将字符串全部转换为小写
name = 'Hu yUn feng'
print(name.upper())
print(name.lower())

first_name = 'hu'
last_name = 'yun feng'
full_name = f'{first_name} {last_name}'
message = f'Hello，{full_name.title()}'
print(message)

#字符串方法：rstrip() ---删除字符串末尾的空白
favorite_language = 'python  '
print(favorite_language.rstrip())

#字符串方法：lstrip() ---删除字符串开头的空白
favorite_language = '  Java'
print(favorite_language.lstrip())

#字符串方法：strip() ---同时删除字符串两端的空白
favorite_language = ' Python '
print(favorite_language.strip())