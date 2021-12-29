# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/18 22:49
@Auth ： 小胡
@File ：练习1.py
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
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def see_stand(self):
        print(f'{self.restaurant_name}的冰淇淋有很多口味，分别是：')
        for i in self.flavors:
            print(i)
res = ['香草味','巧克力味','蓝莓味']
ice = IceCreamStand('冰淇淋小店','营业中',res)
ice.see_stand()


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

    # 添加一个upgrade_battery()方法，用于检查电瓶容量，如果不是100，将其设置为100
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(self.battery_size)

    def get_range(self):
        #调用upgrade_battery()方法
        self.upgrade_battery()
        '打印一条消息，指出电瓶的续航里程'
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'电动车的续航是：{range}里')


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
elec.battery.get_range()