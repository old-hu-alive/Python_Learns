# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/18 23:25
@Auth ： 小胡
@File ：random模块.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    模块random:
        1、randint():将两个整数作为参数，随机返回一个位于这两个整数之间（包含这两个整数）的整数。
        2、choice(): 将一个列表、元组或者 字符串 作为参数，并随机返回其中一个元素。
'''
import random
num = random.randint(1,6)
print(num)

#将字符串作为参数
res = random.choice('1489789wee')
print(res)
#将列表作为参数
lis = ['1','哈哈','小胡','我知道了']
res = random.choice(lis)
print(res)

#将元组作为参数
tuples = ('1','哈哈','小胡','我知道了')
res = random.choice(tuples)
print(res)

