# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/1 21:45
@Auth ： 小胡
@File ：数值列表.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    函数 range(): 差一行为，从指定的第一个值开始，到达指定的第二个值时停止。因为在第二个值停止，所以不包含该值。
        1、两个参数：range(1,5)，输出-- 1、2、3、4
        2、一个参数：range(5),从0开始，输出---0、1、2、3、4
        3、三个参数：range(1,11,2),第三个参数为步长，输出---1、3、5、7、9
    使用函数 list()可将 range()的结果直接转换为列表。
    统计列表：
        找出最大值：max() 函数
        找出最小值：min() 函数
        求和：sum() 函数
    列表解析：
        列表名 = [表达式 for i in range(参数值，参数值)]
        例：num = [i**3 for i in range(1,11)]
            print(f'1-10每个数的立方为：{num}')
'''
num = []
for i in range(1,11,2):
    num.append(i)
print(f'1-10的奇数为：{num}')

#函数 list()可将 range()的结果直接转换为列表。
number = list(range(1,11))
print(number)

#最大值
max_num = max(number)
print(f'number列表中的最大值是：{max_num}')
#最小值
min_num = min(number)
print(f'number列表中的最小值是：{min_num}')
#求和
sum_num = sum(number)
print(f'number列表中值的总和是：{sum_num}')
