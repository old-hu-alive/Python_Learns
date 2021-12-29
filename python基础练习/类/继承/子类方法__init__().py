# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/18 21:43
@Auth ： 小胡
@File ：子类方法__init__.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    一个类继承另一个类时，自动获得另一个类的所有 属性和方法。原有的类称为（父类），新类被称为（子类）。
    子类继承了父类的所有属性和方法，同时还可以定义自己的 属性 和 方法。

    子类的方法：__init__()
        在现有类的基础上编写新类时，通常要调用父类的方法 __init__().----(这将初始化 父类__init__()方法中定义的所有属性，从而让子类也包含这些属性)
        在创建子类时，父类必须包含在当前文件中，并且位于子类的前面。
        定义子类时，圆括号内指定父类的名称。
        super()是一个特殊函数，能够调用父类的方法。
            super().__init__(父类属性1，父类属性2) --- super()调用父类方法__init__()，让子类实例包含这个方法中定义的所有属性。
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

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# my_new_car = Car('Audi','A4',2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# 创建一个电动车类，继承上面的Car的所有属性
class ElectricCar(Car):
    def __init__(self, make, model, year):
        '初始化父类的属性'
        super().__init__(make, model, year)


elec = ElectricCar('宝马', 'x3', '2020')
print(elec.get_descriptive_name())
