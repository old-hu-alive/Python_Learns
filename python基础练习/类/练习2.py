# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/18 19:56
@Auth ： 小胡
@File ：练习2.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f'餐馆名字：{self.restaurant_name}')
        print(f'营业状态：{self.cuisine_type}')
    def open_restaurant(self):
        print(f'{self.restaurant_name}{self.cuisine_type}')
    def set_number_served(self,num):
        self.number_served = num
        print(f'当前餐馆的就餐人数为：{self.number_served}人')
    def increment_number_served(self,add_num):
        self.number_served += add_num
        print(f'餐馆每天接待的最大用餐人数为：{self.number_served}人')
restaurant = Restaurant('永兴餐馆','营业中')
restaurant.open_restaurant()
restaurant.set_number_served(30)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)