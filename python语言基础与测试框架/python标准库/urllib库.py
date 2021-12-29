# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/20 21:33
@Auth ： 小胡
@File ：urllib库.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
 urllib 库用于操作网页 URL,并对网页的内容进行抓取处理
    urllib.request - 打开和读取 URL:
        导包： import urllib.request
        urlopen(url地址): 打开指定的网址
            参数：status --- 获取响应状态码
            参数：read() --- 获取页面文本内容
'''
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())