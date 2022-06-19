# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-19 19:07
@Auth ： 小胡
@File ：input_members.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium.webdriver.common.by import By

from hogwars.app测试.企业微信_app.page.basepage import BasePage


class InputMembers(BasePage):
    def add1_members(self,value):
        # self.find(By.XPATH,'//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        # self.find(By.XPATH,'//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(phone)
        # self.find(By.XPATH,'//*[@text="保存"]').click()
        self.test_steps('../data/add_meenbrs.yaml','add_members',value)

        from hogwars.app测试.企业微信_app.page.add_members import AddMembers
        return AddMembers(self.driver)