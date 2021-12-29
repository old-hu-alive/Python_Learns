# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/28 22:47
@Auth ： 小胡
@File ：test_allure_attach.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    场景：前端自动化测试经常需要附加图片或者html
    解决：
        allure.attach 显示许多不同类型的附件，可以补充测试，步骤或测试结果
    步骤：
        在测试报告中附加网页：
            allure.attach(body(内容),name,attachment_type,extension)
            allure.attach(<body>这是一个body块</body>,name='这是一个名字',attachment_type=allure.attachment_type.HTML)
        在测试报告中附加图片：
            allure.attach.file(source,name,attachment_type,extension):
            allure.attach.file('图片的地址',name='名称',attachment_type=allure.attachment_type.PNG) --这里跟图片的后缀，也可以JPG等等
        
'''
import allure,pytest,os,time
def test_attach_html():
    allure.attach('<body>这是一个网页body</body>', '这是一个html网页',attachment_type=allure.attachment_type.HTML)
def test_attach_photo():
    allure.attach.file('E:\Python_Learns\python语言基础与测试框架\pytest测试框架\img\阿卡丽.jpg', name='这是测试图片',
                        attachment_type=allure.attachment_type.JPG)
    print('这里附加测试图片')
if __name__ == '__main__':
    pytest.main(['-v','--alluredir=./reporter/myreport1',__file__])
    time.sleep(0.5)
    os.popen('allure generate ./reporter/myreport1 -o ./reporter/report1 --clean')
    time.sleep(0.5)
    os.popen('allure open ./reporter/report1')