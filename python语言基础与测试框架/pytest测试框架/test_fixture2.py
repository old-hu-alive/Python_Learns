# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/21 23:57
@Auth ： 小胡
@File ：test_fixture2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    yield:相当于一个return,但他没有返回值
        第一次执行会执行 yield 之前的语句，然后执行测试用例
        第二次执行会执行 yield 之后的语句
'''
import pytest
# 下面将作用域提升至整个模块
@pytest.fixture(scope='module')
def open():
    print('打开浏览器')
    yield
    print('teardown---------')
    print('结束~~~~~~~~')
def test_login_01(open):
    print('这个函数需要登录')
def test_login_02(open):
    print('这个函数需要登录')
def test_login_03(open):
    print('这个函数需要登录')
if __name__ == '__main__':
    pytest.main(['-v',__file__])