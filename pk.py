# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/19 21:38
@Auth ： 小胡
@File ：pk.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
class Role_1():
    def __init__(self,hp_1,power_1):
        self.hp_1 = hp_1
        self.power_1 = power_1
    def fight(self,hp_2,power_2):
        sum = 0
        while True:
            self.hp_1 = self.hp_1 - power_2
            hp_2 = hp_2 - self.power_1
            sum = sum + 1
            print(f"第{sum}回合结束，我的血量为：{self.hp_1}，对手的血量为：{hp_2}")
            if self.hp_1 <= 0 and hp_2 > self.hp_1:
                print("我输了")
                break
            elif hp_2 <= 0 and self.hp_1 > hp_2:
                print("我赢了")
                break
role_1 = Role_1(1000,200)
role_1.fight(1000,200)