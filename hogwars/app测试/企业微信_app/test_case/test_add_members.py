# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-19 19:08
@Auth ： 小胡
@File ：test_add_members.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest

from hogwars.app测试.企业微信_app.page.app import App
from hogwars.app测试.企业微信_app.page.basepage import BasePage


class TestAddMembers():
    #setup设置为类级别的，才能复用driver
    def setup_class(self):
        self.app = App()
    # 用例参数化，将每一组值 传给 变量 value
    @pytest.mark.parametrize('value',BasePage.read_file('../data/test_add_members'))
    def test_add_members(self,value):
        exp = self.app.start_app().main().goto_address_book().goto1_add_members().goto1_input_members().add1_members(value).verify_code()
        print(f'-----{exp}')
        assert exp == '添加成功'
    def teardown_class(self):
        self.app.stop()
if __name__ == '__main__':
    pytest.main(['-s','-v',__file__])