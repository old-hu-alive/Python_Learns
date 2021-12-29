# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/19 21:20
@Auth ： 小胡
@File ：练习1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
with open('cats.txt','w',encoding='utf8') as f:
    f.write('大橘\n')
    f.write('小白\n')
    f.write('花花\n')

with open('dogs.txt','w',encoding='utf8') as f:
    f.write('大黄\n')
    f.write('小黑\n')
    f.write('壮壮\n')

def read_file(file_name):
    try:
        with open(file_name,encoding='utf8') as f:
            res = f.read()
            print(f'{file_name[:3]}包括：\n{res.strip()}')
    except FileNotFoundError:
        print(f'{file_name}文件找不到！')
file_names = ['cats.txt','dogs.txt','hhh.txt']
for file_name in file_names:
    read_file(file_name)