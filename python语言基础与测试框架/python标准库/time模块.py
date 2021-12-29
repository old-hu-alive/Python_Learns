# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/20 21:09
@Auth ： 小胡
@File ：time模块.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    time.asctime() : 获取国外的时间格式 --- Mon Dec 20 21:16:25 2021
    time.time() : 获取时间戳 ,返回float格式 的 秒数 --- 1640006340.5587215
    time.sleep(n) : 等待n秒
    time.localtime() : 将时间戳转成时间元组 --- time.struct_time(tm_year=2021, tm_mon=12, tm_mday=20, tm_hour=21,
                                                                tm_min=19, tm_sec=2, tm_wday=0, tm_yday=354, tm_isdst=0)
    time.strftime() : 将当前时间戳转成带格式的时间 --- 2021-12-20 21-21-08
        格式：time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()) 
'''
import time
print(time.asctime())
print(time.time())
time.sleep(2)
print('hhh')
print(time.localtime())
res = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
print(res)

'''获取两天前的时间'''
#获取当前的时间戳
now_time = time.time()
#计算两天前的时间戳
two_day_time = now_time - 60*60*24*2
#将时间戳转换为 时间元组
time_tuple = time.localtime(two_day_time)
#将时间元祖转换成带格式的时间
res = time.strftime('%Y-%m-%d %H-%M-%S',time_tuple)
print(f'两天前的时间为：{res}')
