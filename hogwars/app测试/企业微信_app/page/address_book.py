# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-19 19:07
@Auth ： 小胡
@File ：address_book.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium.webdriver.common.by import By

from hogwars.app测试.企业微信_app.page.basepage import BasePage


class AddressBook(BasePage):
    def goto1_add_members(self):
        self.find(By.XPATH,'//*[@text="添加成员"]').click()
        from hogwars.app测试.企业微信_app.page.add_members import AddMembers
        return AddMembers(self.driver)