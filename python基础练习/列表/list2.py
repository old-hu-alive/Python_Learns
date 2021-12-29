# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/30 22:50
@Auth ： 小胡
@File ：list2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    列表排序：
        1、方法 sort()：对列表永久排序，括号内没有参数，就是 正向排序（升序）; 括号内加参数-----reverse=True,就是反向排序（倒序）
        2、函数 sorted()：对列表临时排序，括号内没有参数，就是 正向排序（升序）; 括号内加参数-----reverse=True,就是反向排序（倒序）
        3、reverse(): 倒着打印列表（永久性），只是 反转列表的输入顺序，不是反向排序。若要恢复原来的顺序，再次调用reverse()方法即可。
    确定列表的长度：
        使用函数：len()
'''
cars = ['bmw','audi','toyota','subaru']
# 永久-正向排序
cars.sort()
print(f'永久-正向排序:{cars}')
# 永久-反向排序
cars.sort(reverse=True)
print(f'永久-反向排序:{cars}')
# 临时-正向排序（生成一个新列表，而不是原来的列表）
new_cars = sorted(cars)
print(f'临时-正向排序:{new_cars}')
# 临时-反向排序（生成一个新列表，而不是原来的列表）
new_cars = sorted(cars,reverse=True)
print(f'临时-反向排序:{new_cars}')
# 倒着打印列表，反转列表的输入顺序
cars.reverse()
print(f'倒着打印列表:{cars}')

#统计列表的长度
num = len(cars)
print(f'列表长度为：{num}')