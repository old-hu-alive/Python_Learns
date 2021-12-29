# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/22 0:05
@Auth ： 小胡
@File ：test_mark_paramertrize.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    参数化：
        装饰器：@pytest.mark.parametrize('参数1,参数2,.......',值)
        参数，与被装饰的函数或者方法的形参相同，如果有多个参数写在一个字符串中即可
        值，传递给参数的值，通常使用列表传参，如果需要给多个参数传参则将这些值封包到元组中
    eval : 将字符串转化为表达式，如 字符串'3+5'，可以转化为 3+5 --eval('3+5')
'''
import pytest,os
import yaml
# import allure_pytest
@pytest.mark.parametrize('num1,num2,exp',[(1,2,3),(3,5,8),(4,2,6)])
def test_add(num1,num2,exp):
    sum = num1 + num2
    assert sum == exp
#使用yaml文件参数化
with open('num.yml',encoding='utf8') as f:
    res = yaml.load(f,Loader=yaml.FullLoader)
    print(res)
@pytest.mark.parametrize('num1,num2,exp',res)
def test_multiplication(num1,num2,exp):
    sum = num1 * num2
    assert sum == exp
if __name__ == '__main__':
     # pytest.main(['-v','--html=./report77s444666.html',__file__])
     pytest.main(['-v', '--alluredir=./myreports', __file__])  # --alluredir <测试结果存放目录>  这个时候文件里边的数据只是测试结果（json.txt文件），还不是测试报告
     os.popen('allure generate ./myreports -o ./reporters --clean') #allure generate <allure测试结果目录> -o <存放测试报告目录> --clean(清空旧数据）
     # os.system('allure generate myreports/xml -o reporters --clean')
     os.popen('allure open ./reporters') #allure open <存放测试报告的目录> 自动打开测试报告的html文件(运行后会启动一个web服务用语展示报告)
     # os.system('allure open reporters')
     # os.popen('allure serve ./re') #在线查看测试报告
     '''
        如果allure生成的测试报告打开为404，记得检查 <测试结果存放目录> 的文件名是否一致。
        
        也可以在终端运行：
            1、点击pycharm下方的Terminal
            2、使用cd 进入测试文件所在的目录
            3、输入pytest -v  测试文件名 --alluredir <测试结果存放目录>  test_mark_paramertrize.py ./myrepors
            4、输入allure generate <测试结果存放目录> -o <存放测试报告的目录>  --clean
            5、输入allure open <存放测试报告的目录> （可选）
     '''
# pytest -v  test_mark_paramertrize.py --alluredir ./myreports
# allure generate ./myreports -o ./reporters --clean
# allure open ./reporters