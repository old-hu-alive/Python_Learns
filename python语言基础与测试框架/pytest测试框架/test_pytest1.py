# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/21 22:44
@Auth ： 小胡
@File ：pytest1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    File | Settings | Tools | Python Integrated Tools中设置默认以pytest运行
    pip install pytest-assume :即使有多条断言失败，也都全部运行完
        pytest-assume[1=2]
        pytest-assume[2>3]
'''
import pytest
def test_01():
    assert 2 == 2

if __name__ == '__main__':
    # pytest.main(['-v',__file__])
    pytest.main(['-v', '--html=./report999777.html', __file__])
