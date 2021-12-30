# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/30 23:19
@Auth ： 小胡
@File ：calc.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
class Calc:
    #加法
    def add(self,a,b):
        try:
            res = a + b
            return res
        except Exception:
            res = 'fail'
            return res
    #除法
    def division(self,a,b):
        try:
            res = a / b
            return res
        except Exception:
            res = 'fail'
            return res
# calc = Calc()
# print(calc.chu(1, 0))