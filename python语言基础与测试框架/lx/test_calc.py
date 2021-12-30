# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/30 23:22
@Auth ： 小胡
@File ：test_calc.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pytest,allure,os
from python语言基础与测试框架.calc_lx.calc import Calc
calc = Calc()
add_data = [(1,2,3),(1.5,2.5,4),('aaa',2,'fail'),('@',2,'fail'),('哈哈哈',3,'fail'),(2,-1,1)]
division_data = [(2,1,2),(2.4,1.2,2),(4,0,'fail'),(2,-1,-2),('aaa',2,'fail'),('@',2,'fail'),('哈哈哈',3,'fail'),
                 (2,'aaa','fail'),(2,'@','fail'),(3,'哈哈哈','fail')]
@allure.feature('加减乘除运算器')
class TestCalc:
    @allure.story('测试加法运算')
    @pytest.mark.parametrize('a,b,exp',add_data)
    def test_add(self,a,b,exp):
        res = calc.add(a,b)
        assert res == exp

    @allure.story('测试除法运算')
    @pytest.mark.parametrize('a,b,exp', division_data)
    def test_division(self, a, b, exp):
        res = calc.division(a, b)
        assert res == exp
if __name__ == '__main__':
    pytest.main(['-v','--alluredir=./reports/myreport',__file__])
    os.popen('allure generate ./reports/myreport -o ./reports/report --clean')
    os.popen('allure open ./reports/report')
