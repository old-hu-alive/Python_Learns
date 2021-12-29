# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/18 22:35
@Auth ： 小胡
@File ：将实例用作属性.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    当 类1 中的属性和方法越来越多，可以将类的一部分提出来，作为一个独立的类。
    然后，将这个独立的类（实例）作为 类1 的属性。
'''


# 创建Car类，指定制造商、型号、生产年份
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '返回车子的描述信息'
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        '打印一条指出汽车历程的消息'
        print(f'This car has {self.odometer_reading} miles on it')
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
    def increment_odometer(self,miles):
        self.odometer_reading += miles
#创建一个独立的类，将关于电瓶的属性都放到这个类中来
class Battery:
    '一次模拟电动汽车电瓶的简单尝试'
    def __init__(self,battery_size = 75):
         self.battery_size = battery_size
    def describe_battery(self):
        '打印一条描述电瓶容量的消息'
        print(f'This car has a {self.battery_size} -kwh battery')


# 创建一个电动车类，继承上面的Car的所有属性
class ElectricCar(Car):
    def __init__(self, make, model, year):
        '初始化父类的属性'
        super().__init__(make, model, year)

        #然后将 独立的类 Battery 进行实例化，当做 电动车类 的一个属性。
        self.battery = Battery()

elec = ElectricCar('宝马', 'x3', '2020')
print(elec.get_descriptive_name())
elec.battery.describe_battery()