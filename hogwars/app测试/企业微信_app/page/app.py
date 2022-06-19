# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-19 19:06
@Auth ： 小胡
@File ：app.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from appium import webdriver

from hogwars.app测试.企业微信_app.page.basepage import BasePage
from hogwars.app测试.企业微信_app.page.main import Main


class App(BasePage):
    _package = 'com.tencent.wework'
    _activity = '.launch.WwMainActivity'
    def start_app(self):
        if self.driver == None:
            print('driver为空，创建driver')
            caps = {
                'platformName':'Android',
                'platformVersion':'7.1.2',
                'deviceName':'127.0.0.1:62001',
                'appPackage':self._package,
                'appActivity':self._activity,
                'noReset':'true',
                'unicodeKeyBoard': 'true',
                'resetKeyBoard': 'true'
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
            self.driver.implicitly_wait(10)
        else:
            print('复用driver')
            self.restart()
        return self
    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
    def stop(self):
        self.driver.quit()

    def main(self) -> Main:
        return Main(self.driver)