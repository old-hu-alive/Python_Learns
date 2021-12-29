# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/19 15:51
@Auth ： 小胡
@File ：读取文件内容.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    打开文件时，可指定读取的模式：
        只读模式（'r'）,写入模式（'w'）,附加模式（'a'）,读写模式（'r+'）.
        如省略模式参数，默认以只读模式打开

    ' with open(文件对象) as 别名:
        pass

    函数open() 返回一个表示文件的对象
    关键字with 在不访问文件后，将文件关闭。
    1、方法 read(): 读取这个文件的全部内容，返回一个字符串。
        read()到达文件末尾时，返回一个空字符串，显示出来就是一个空行。可使用strip()删除空字符串。
    2、方法 readlines(): 从文件中读取每一行，并将其存储在一个列表中。
    3、readline()：可以每次读取一行内容
'''
# with open('读取文件1',encoding='utf8') as file_name:
#     # res = file_name.read()
#     # print(f'读取文件所有内容：\n{res}')
#     #遍历文件对象：
#     # for files in file_name:
#     #     print(files)
#     mess = file_name.readlines()
# print(mess)


with open('读取文件1', encoding='utf8') as file_name:
    res = file_name.readlines()
    print(res)
    for line in res:
        ll = line.replace('Python', 'C')
        print(ll)
        # line.replace('Python','C')
