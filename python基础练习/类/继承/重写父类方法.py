# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/18 22:27
@Auth ： 小胡
@File ：重写父类方法.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    对于父类方法，如果它不符合 子类 模拟的实物的行为，可以进行重写。
    可以在子类中定义一个与要重写的 父类方法 同名的方法；这样，Python将不会考虑这个父类方法，只关注子类中定义的方法
    继承时，可让子类保留从父类哪里继承而来的精华，去掉不需要的糟粕。
'''
#创建Car类，指定制造商、型号、生产年份
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        #指定默认值
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '返回车子的描述信息'
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    def read_odometer(self):
        '打印一条指出汽车历程的消息'
        print(f'This car has {self.odometer_reading} miles on it')
    def fill_gas_tank(self):
        print('传统汽车都有油箱。')

#创建一个电动车类，继承上面的Car的所有属性
class ElectricCar(Car):
    def __init__(self,make,model,year):
        '初始化父类的属性'
        super().__init__(make,model,year)

    #重写上面的父类方法：fill_gas_tank()
    def fill_gas_tank(self):
        print('电动车只有电瓶，没有油箱。')
elec = ElectricCar('宝马','x3','2020')
print(elec.get_descriptive_name())
elec.fill_gas_tank()