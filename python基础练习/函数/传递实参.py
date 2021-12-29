# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/15 21:22
@Auth ： 小胡
@File ：传递实参.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    1、位置实参：顺序很重要，一个形参 对应着相应位置 顺序的 实参。如：
        def work(形参1,形参2):
            pass
        work(实参1,实参2)
    2、关键字参数：顺序不重要，因为调用函数时---在实参列表中 指定了各个 实参对应的形参。如：
        def work(形参1,形参2):
            pass
        work(形参2=实参2,形参1=实参1)
        但是在使用关键字实参时，务必准确指定函数定义中的形参名。

    3、默认值参数：编写函数时，可给每个形参指定默认值。如：
        def work(形参2,形参1=实参1):
            pass
        work(实参2)
            调用函数时，如果给形参提供了实参，将使用指定的实参值；否则，将使用形参的默认值。
            上述例子中，修改了形参的顺序。因为形参1 指定了默认值，不再需要通过实参来获取数据；所以调用函数时就只包含一个实参了
                python依然将这个实参视为 位置参数，它将关联到第一个形参，所以将形参2放在了第一个。
            所以，在使用默认值参数时，先在形参列表中：列出没有默认值的形参，在列出有默认值的形参。
'''


# 位置参数
def describe_pet(animal_type, pet_name):
    '显示宠物信息'
    print(f'\n我有一只{animal_type}')
    print(f'我的{animal_type}名字叫{pet_name}')


describe_pet('狗', '小黄')


# 关键字参数
def describe_pet(pet_name, animal_type):
    '显示宠物信息'
    print(f'\n我有一只{animal_type}')
    print(f'我的{animal_type}名字叫{pet_name}')


describe_pet(animal_type='狗', pet_name='小黄')


# 默认值参数
def describe_pet(pet_name, animal_type='猫'):
    '显示宠物信息'
    print(f'\n我有一只{animal_type}')
    print(f'我的{animal_type}名字叫{pet_name}')


describe_pet('小白')