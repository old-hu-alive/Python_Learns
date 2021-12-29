# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/12 23:41
@Auth ： 小胡
@File ：练习2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
names = ['小胡','admin','小王','小徐','小郑']
if names:
    if 'admin' in names:
        for name in names:
            if name == 'admin':
                print(f'你好{name},很高兴你能使用我们的网站')
            else:
                print(f'你好{name},欢迎登陆')
    else:
        print('没有admin这个用户！')
else:
    print('没有一个用户名')

nums = [1,2,3,4,5,6,7,8,9]
for num in nums:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')