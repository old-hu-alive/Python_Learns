# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/12 15:13
@Auth ： 小胡
@File ：练习1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

'''
    在if语句中，列表名 作为条件表达式时，将在列表至少包含一个元素时返回True,如果列表为空，返回False.
    判断列表是否为空：
        if 列表名：
            输出
        nums = []
        如：if nums:
                pass
            else:

'''

# 设置变量age的值，编写一个if-elif-else的结构。
age = 64.9
if age < 2:
    name = '婴儿'
elif age < 4:
    name = '幼儿'
elif age < 13:
    name = '儿童'
elif age < 20:
    name = '青少年'
elif age < 65:
    name = '成年人'
else:
    name = '老年人'
print(f'这是一个{name}')