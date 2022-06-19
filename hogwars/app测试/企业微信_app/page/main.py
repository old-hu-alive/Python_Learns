# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-19 19:06
@Auth ： 小胡
@File ：main.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium.webdriver.common.by import By

from hogwars.app测试.企业微信_app.page.address_book import AddressBook
from hogwars.app测试.企业微信_app.page.basepage import BasePage


class Main(BasePage):
    def goto_address_book(self):
        self.find(By.XPATH,'//*[@text="通讯录"]').click()
        return AddressBook(self.driver)