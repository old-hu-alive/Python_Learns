# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/13 22:02
@Auth ： 小胡
@File ：dir1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    添加键值对：字典名[键名] = 值  ，如：alien['color'] = 'green'
    修改键值对：字典名[键名] = 新值  ，如：alien['color'] = 'red'
    删除键值对：del 字典名[键名]，如：del alien['color'] ,永远删除键名color和他对应的值。
    使用get()方法来访问：
        使用 方括号内的键（例：字典名[键名]）获取值时，如果：指定的键名不存在，会报错。
        使用方法 get(),指定的键名不存在时，返回一个默认值：
            get()的第一个参数：指定键名 --- 必填
            get()的第二个参数：指定键名不存在时，要返回的值 --- 选填
            例：value = alien.get('points','没有这个键名')
            如果字典alien有'points'这个键名，返回相应的值；如果没有，返回设定的默认值。
        调用get()方法时，如果没有指定第二个参数，并且指定的键名不存在，返回 None
'''
man = {
        'first_name':'云峰',
        'last_name':'胡',
        'age':'24',
        'city':'成都市'
    }
print(man['first_name'])
print(man['last_name'])
print(man['age'])
print(man['city'])