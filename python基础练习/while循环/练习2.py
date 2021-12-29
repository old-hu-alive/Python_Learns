# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/14 23:17
@Auth ： 小胡
@File ：练习2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

#兴趣爱好
message = ['打游戏','看电影','吃东西']
new_message = []
# while message:
#     res = message.pop()
#     print(f'我喜欢{res}')
#     new_message.append(res)
# print(new_message)

for i in message:

    print(f'我喜欢{i}')
    new_message.append(i)
print(new_message)