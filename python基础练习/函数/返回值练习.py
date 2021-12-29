# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/15 22:04
@Auth ： 小胡
@File ：返回值练习.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
def city_country(city,country):
    res = f'"{city},{country}"'
    return res
message = city_country('上海','中国')
print(message)
message = city_country('纽约','美国')
print(message)
message = city_country('伦敦','英国')
print(message)

#让参数变成可选的，
def make_album(make,album,num=None):
    if num:
        res = {'歌手':make,'专辑':album,'歌曲数':num}
    else:
        res = {'歌手': make, '专辑': album}
    return res
message = make_album('周杰伦','七里香',10)
print(message)
while True:
    print('下面要填写歌手的信息：')
    make = input('请输入歌手名：')
    album = input('请输入专辑名：')
    num = input('请输入歌曲数：')
    message = make_album(make,album,num)
    print(message)
    print('-----------------------------------------')
    mess = input('是否继续输入？y/n：')
    if mess == 'n':
        break