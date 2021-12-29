# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/19 21:00
@Auth ： 小胡
@File ：练习.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    处理异常：try-except-else结构:
        将可能发生异常的代码，放在 try中，
        发生异常后，对异常的处理，放在except中，
        try代码块中执行成功，需要输出的代码放在else中。

    方法：split() ----- 以分隔符将字符串拆分成多个部分，存储到一个列表中。  括号中可以为 ， 。或者为空格都行。
'''
# 加法运算
print('即将进行加法运算')
while True:
    num1 = input('请输入第一个数：')
    num2 = input('请输入第二个数：')


    def add(num1, num2):
        try:
            sum = float(num1) + float(num2)
        except ValueError:
            print('数学运算需要输入正确的数值！')
        else:
            print(f'{num1}+{num2}的和为：{sum}')


    add(num1, num2)
    res = input('是否继续输入？y/n:')
    if res == 'n':
        print('即将退出......')
        break