# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-19 19:07
@Auth ： 小胡
@File ：basepage.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import yaml
from appium.webdriver.webdriver import WebDriver

class BasePage:
    def __init__(self,driver: WebDriver = None):
        self.driver = driver
    def find(self,by,locator):
        return self.driver.find_element(by,locator)
    @classmethod
    def read_file(self,file_path):
        with open(file_path,encoding='utf-8') as f:
           test_data =  yaml.safe_load(f)
           return test_data
    # 测试步骤的数据驱动方法
    def test_steps(self,file_path,function_name,value=None):
        with open(file_path,encoding='utf-8') as f:
            #test_steps 的数据格式是：{'hhh': [{'by': 'a', 'locator': 'b', 'click': 'c'}, {'by': 'a1', 'locator': 'b1', 'click': 'c1'},...]}
            # dict.get() 方法：就是获取对应键名的 键值
            test_steps =  yaml.safe_load(f)
            #steps 的数据格式是列表套字典：[{'by': 'a', 'locator': 'b', 'click': 'c'}, {'by': 'a1', 'locator': 'b1', 'click': 'c1'}, ....]
            steps = test_steps.get(function_name)
        element = None
        count = 0
        print(f'c ----- {count}')
        # step 的数据格式是字典：{'by': 'a', 'locator': 'b', 'click': 'c'}
        for step in steps: # 依次循环 读取出来的测试步骤
            if 'click' == step.get('action'):
                self.find(step.get('by'),step.get('locator')).click()
            elif 'send_keys' == step.get('action'):
                send_value = self.test_data(value,count)
                self.find(step.get('by'), step.get('locator')).send_keys(send_value)
                count += 1
    # 将 内容抽离出来，封装一个方法，解析测试数据，用于依次读取
    def test_data(self,value,count):
        # 统计 参数化传过来的每一组数据 value 的长度
        sum = len(value)
        # 如果 count < 长度 sum ,就执行下面的语句
        if count < sum:
            for i in range(1):  # 循环1次 ，每次执行新的测试步骤的时候，就取对应要输入的 参数值
                '''
                    比如：steps第一次for循环的时候，执行输入姓名的步骤，count = 0,读取 value[0] = name,
                    当上面的steps再次循环的时候，执行输入电话号码的步骤，count = 1 了，读取 value[1] = phone
                    依次类推.....  知道读取完所有数据
                '''
                send_value = value[count]
                # self.find(step.get('by'), step.get('locator')).send_keys(send_value)
                # count += 1  # 每次循环完，count + 1
                print(f'count --- {count}')
                return send_value
# steps 循环中，没抽离之前的版本
"""
count = 0
print(f'c ----- {count}')
# step 的数据格式是字典：{'by': 'a', 'locator': 'b', 'click': 'c'}
for step in steps: # 依次循环 读取出来的测试步骤
    if 'click' == step.get('action'):
        self.find(step.get('by'),step.get('locator')).click()
    elif 'send_keys' == step.get('action'):
        # 统计 参数化传过来的每一组数据 value 的长度
        sum = len(value)
        # 如果 count < 长度 sum ,就执行下面的语句
        if count < sum:
            for i in range(1):  # 循环1次 ，每次执行新的测试步骤的时候，就取对应要输入的 参数值
                '''
                    比如：steps第一次for循环的时候，执行输入姓名的步骤，count = 0,读取 value[0] = name,
                    当上面的steps再次循环的时候，执行输入电话号码的步骤，count = 1 了，读取 value[1] = phone
                    依次类推.....  知道读取完所有数据
                '''
                send_value = value[count]
                self.find(step.get('by'), step.get('locator')).send_keys(send_value)
                count += 1  # 每次循环完，count + 1
                print(f'count --- {count}')
"""
