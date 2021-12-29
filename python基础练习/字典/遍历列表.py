# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/13 22:34
@Auth ： 小胡
@File ：dir2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    1、方法：items() ----  返回一个键值对的列表
    遍历所有键值对：
        1、使用for循环，声明两个变量，用于存储 键名 和 值，
        2、使用 字典名.items()，返回一个键值对列表，将值赋给两个变量，然后打印出来。
    2、方法：keys() ---  返回一个列表，包含字典中所有的键名。
        遍历所有键名：
        1、使用for循环，声明一个变量，用于存储 键名 ，
        2、使用 字典名.keys()，返回一个包含所有键名的列表，将值赋给变量，然后打印出来。
        或者 直接 for循环中直接使用 字典名，不用带 keys（）方法，也是遍历键名，只是显示的使用keys()方法，更容易理解。例：
            for key in user:
                print(f'\nkey:{key}')
    3、按特定的顺序遍历字典中的所有键：
        使用 sorted() 来获取 顺序排列的键列表的副本：
            for key in sorted(user.keys()):
                print(f'\nkey:{key}')
    4、方法：values()  ---- 返回一个列表，包含字典中所有的 值 ：user.values()
        遍历字典中的所有值：
            1、使用for循环，声明一个变量，用于存储 值 ，
            2、使用 字典名.values()，返回一个包含所有 值 的列表，将值赋给变量，然后打印出来。
        values() 提取字典中所有的值，没有考虑重复，为了剔除重复项，可使用集合 set()：
            set(字典名.values())
'''
user = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
print(user.items())
print(f'字典中的所有键名：{user.keys()}')
print(f'字典中的所有值：{user.values()}')
#遍历所有键值对
for key,value in user.items():
    print(f'\nkey:{key}')
    print(f'value:{value}')
#遍历键名
for key in user:
    print(f'\nkey:{key}')
    # print(f'value:{value}')
#按特定的顺序遍历字典中的所有键：
print('按特定的顺序遍历字典中的所有键：')
for key in sorted(user.keys()):
    print(f'key:{key}')

languages = {
    'A':'python',
    'B':'java',
    'C':'C',
    'D':'python',
}
print('--------遍历字典中的所有值,并去除重复项----------')
#遍历字典中的所有值,并去除重复项
for language in set(languages.values()):
    print(language)