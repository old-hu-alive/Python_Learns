# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/14 22:15
@Auth ： 小胡
@File ：字典嵌套练习.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
people_1 = {'first_name':'胡','last_name':'云峰','age':'24','city':'成都'}
people_2 = {'first_name':'胡','last_name':'琴明','age':'49','city':'广安'}
people_3 = {'first_name':'何','last_name':'冬林','age':'50','city':'广安'}
peoples = [people_1,people_2,people_3]

for people in peoples:
    value = list(people.values())
    print(value)
    print(f'姓名：{value[0]}{value[1]},年龄：{value[2]},居住地：{value[3]}')