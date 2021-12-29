# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/20 20:56
@Auth ： 小胡
@File ：python标准库.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    mkdir():创建一个空文件夹
    listdir(): 显示指定目录下的所有文件和文件夹
    removedirs():删除指定的文件夹
    getcwd():获取当前文件的路径。
    os.path :
        exists():判断指定的文件或文件夹是否存在
    
'''
import os
# os.mkdir('testdir')
print(os.listdir('../'))
# os.removedirs('testdir')
print(os.getcwd())
print(os.path.exists('ewr.py'))