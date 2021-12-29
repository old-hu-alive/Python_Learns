# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/28 21:54
@Auth ： 小胡
@File ：test_allure特性.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    alllure特性：
        @allure.feature('登录模块')   ---  标注一个大的功能模块
        @allure.story('登录成功')  --- 标注功能模块下的 子功能
        
        @allure.testcase('ip地址')  --- 链接到测试用例管理地址
'''
import pytest,os,allure
@allure.feature('登录模块')
class TestLogin():
    @allure.story('登录成功')
    def test_login_success(self):
        print('这是登录测试用例：登录成功')
    @allure.story('登录失败')
    def test_login_fail_1(self):
        print('登录失败，用户名缺失')
    @allure.story('登陆失败')
    def test_login_fail_2(self):
        with allure.step('点击用户名'):
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        print('点击登录')
        with allure.step('点击登录后失败：'):
            assert '1' == 1
            print('登录失败，密码错误')
    @allure.link('http://www.baidu.com',name='测试用例的链接')
    def test_with_link(self):
        print('这是一个添加了链接的测试用例')
if __name__ == '__main__':
    pytest.main(['-v','--alluredir=./reporter/myreport',__file__])
    os.popen('allure generate ./reporter/myreport -o ./reporter/report --clean')
    os.popen('allure open ./reporter/report')