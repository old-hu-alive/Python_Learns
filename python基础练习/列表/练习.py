# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/30 22:10
@Auth ： 小胡
@File ：练习.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
names = ['小胡','小徐','小王']
res = names.pop(1)
print(f'"{res}"无法来参加聚会。')
names.append('小张')
for i in names:
    print(f'"{i}"你好，记得准时来参加我的聚会哟~')
print('---------我找到了更大的餐桌，那就在邀请三个人来参加聚会吧~----------------')
names.insert(0,'小郑')
names.insert(2,'小梁')
names.append('小李')
for i in names:
    print(f'"{i}"你好，记得准时来参加我的聚会哟~')

print('---------新买的餐桌无法及时送达，所以我只能邀请两位嘉宾共进晚餐了----------------')
flag = True
while flag:
    num = len(names)
    if num > 2:
        res = names.pop()
        print(f'"{res}"你好，很抱歉无法邀请你来参加我的聚会~')
    else:
        flag = False
        break
print('---------------------------------------------')
for i in names:
    print(f'"{i}"你好，你仍然在我的邀请人之列~')
print('---------------删除所有嘉宾------------------')
del names[0]
del names[-1]
print(names)
