# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/21 23:27
@Auth ： 小胡
@File ：conftest.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    conftest.py配置需要注意：
        1、conftest.py文件名不能更换
        2、conftest.py与运行的用例要在同一个package下，并且有__init__文件
        3、不需要import导入conftest.py,pytest用例会自动查找
        4、全局的配置和前期工作都可以卸载这里，放在某个报下，就是这个包数据共享的地方
'''
import pytest
'''
    fixture()中默认参数为scope = function,作用域是函数级别
    scope 还有其他的值：module,class,package,session等等
    
    yield:相当于一个return,但他没有返回值
        第一次执行会执行 yield 之前的语句，然后执行测试用例
        第二次执行会执行 yield 之后的语句
'''
# 下面将作用于提升至整个模块
@pytest.fixture(scope='module')
def login():
    print('这是一个登录函数')
    # yield
    # print('---------------')