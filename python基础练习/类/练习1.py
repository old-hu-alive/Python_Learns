# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/18 19:32
@Auth ： 小胡
@File ：练习1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'餐馆名字：{self.restaurant_name}')
        print(f'营业状态：{self.cuisine_type}')
    def open_restaurant(self):
        print(f'{self.restaurant_name}{self.cuisine_type}')
# rest = Restaurant('永兴餐馆','营业中')
# rest.describe_restaurant()
# rest.open_restaurant()
restaurant = Restaurant('永兴餐馆','营业中')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant1 = Restaurant('胡记餐厅','未营业')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('杨氏餐馆','营业中')
restaurant2.describe_restaurant()

