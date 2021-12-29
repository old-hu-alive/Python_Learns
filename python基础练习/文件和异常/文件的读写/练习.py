# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/19 16:49
@Auth ： 小胡
@File ：练习.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'编写一个程序，提示用户输入名字，用户做出响应后，将名字写入文件guest.txt中'
# name = input('请输入您的姓名：')
# if name:
#     with open('guest.txt','w',encoding='utf8') as file_name:
#         file_name.write(name)
# else:
#     print('您的姓名无效！')

'''
    编写一个while循环，提示用户输入名字。用户输入名字后，在屏幕上打印一句问候语，并将一条记录添加到文件guest_book.txt中。确保这个文件中
    记录每条都独占一行。
'''
while True:
    name = input('请输入您的姓名：')
    if name:
        print(f'欢迎您，{name}!')
        res = f'{name}刚刚访问了网站。'
        with open('guest_book.txt', 'a', encoding='utf8') as file_name:
            file_name.write(f'{res}\n')
    else:
        print('您的姓名无效！')
    print('-------------------------------')
    mess = input('是否继续输入？y/n:')
    if mess == 'n':
        break