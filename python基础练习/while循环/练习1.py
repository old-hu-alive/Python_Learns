# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/14 22:45
@Auth ： 小胡
@File ：练习1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from while循环 import 练习1

#10的整数倍
message = input('请输入一个数：')
message = int(message)
if message % 10 == 0:
    print('10的整数倍')
else:
    print('不是10的整数倍')
#餐馆定位
flag = True
while flag:
    message = input('请问你们有多少人用餐：')
    message = int(message)
    if (message <= 0):
        print('请说正确的人数！')
    else:
        if message <= 8:
            print('有空位')
            flag = False
        else:
            print('没空位,欢迎下次光临')
            flag = False
