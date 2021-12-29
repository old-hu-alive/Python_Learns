# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/21 23:27
@Auth ： 小胡
@File ：test_fixure.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    执行测试用例时，有的用例需要登录，有的不需要登录，setup和teardown无法满足，可以用fixture
    步骤：
        1、导入pytest
        2、在登录函数上面加上@pytest.fixture()
        3、在要使用的测试方法中传入 --登录函数的名称，就可以执行登录
    conftest.py是一个公共文件，可以进行数据共享，将带@pytest.fixture()的函数放在这个文件中
    ，其他文件需要调用带fixture的函数时，直接在函数中传入带fixture的函数名即可。
    如：
'''
import pytest
def test_login_01(login):
    print('这个函数需要登录')
def test_login_02():
    print('这个函数不需要登录')
def test_login_03(login):
    print('这个函数需要登录')
if __name__ == '__main__':
    pytest.main(['-v',__file__])