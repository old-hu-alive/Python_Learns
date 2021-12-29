# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/15 22:44
@Auth ： 小胡
@File ：传递任意数量的实参.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    1、接收 任意数量实参 的形参：
        形参名： *args 中的 星号（*） ------ 是让python创建一个名为 args 的 空元组，并将实参列表中的所有值都封装到这个元组中。
    2、结合使用 位置实参 和 任意数量实参：
        函数名（位置实参，*args）
        如果要让函数接受不同类型的实参，必须将 接收 任意数量实参 的形参（*args）放在最后面。Python将：
            优先匹配 （位置实参）和（关键字实参），再将余下的实参都收集到 *args 中。
    3、使用任意数量的关键字实参：
        形参名：**kwargs 中的两个星号（**）--- 是让python创建一个名为 kwargs 的空字典，并将所收到的所有关键字实参（形参1=实参1）
                都放在这个字典中。
'''
#任意数量实参
def make_pizza(*args):
    print(args)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','pepperoni')

#结合使用 位置实参 和 任意数量实参：
def make_pizza(num,*args):
    print(num,args)
make_pizza(12,'pepperoni')
make_pizza(12,'mushrooms','green peppers','pepperoni')

#使用任意数量的关键字实参：
def make_pizza(**kwargs):
    print(kwargs)
make_pizza(hh = 'pepperoni')
make_pizza(hh = 'mushrooms',jj = 'green peppers',ll = 'pepperoni')