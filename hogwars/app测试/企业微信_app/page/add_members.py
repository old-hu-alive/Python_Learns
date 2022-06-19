# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-19 19:07
@Auth ： 小胡
@File ：add_members.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from hogwars.app测试.企业微信_app.page.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC

from hogwars.app测试.企业微信_app.page.input_members import InputMembers


class AddMembers(BasePage):
    def goto1_input_members(self):
        self.find(By.XPATH,'//*[@text="手动输入添加"]').click()
        return InputMembers(self.driver)
    def verify_code(self):
        # res = WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((By.XPATH,'//*[@text="添加成功"]')))

        locator = (By.XPATH,'//*[@text="添加成功"]')
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(locator))
        res = self.driver.find_element(*locator).text
        print(f'-----------d{res}')
        return res