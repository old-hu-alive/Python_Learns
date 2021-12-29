# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/1 22:10
@Auth ： 小胡
@File ：数值列表-练习.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
#1、使用一个for循环打印数1-20
for num in range(1,21):
    print(num)
#2、创建一个包含数 1-1_000_000的列表，使用for循环打印出来
numbers = list(range(1,1_000_001))
# for number in numbers:
#     print(number)
#3、找出1-1_000_000的最大值、最小值、求和
print(max(numbers))
print(min(numbers))
print(sum(numbers))
#4、通过给函数range()指定第三个参数来创建一个列表，其中包含1-20的奇数，使用for打印出来
num = []
for i in range(1,21,2):
    num.append(i)
print(f'1-20的奇数包括：{num}')
#5、创建一个列表，其中包含3-30能被3整除的数，使用for打印出来
numbers = list(range(3,31,3))
for number in numbers:
    print(number)

res = []
for i in range(3,31):
    if i % 3 == 0:
        res.append(i)
print(f'3-30能被3整除的数有：{res}')

#6、创建一个列表，包含1-10的立方，使用for打印出来
num = []
for i in range(1,11):
    num.append(i**3)
print(f'1-10每个数的立方为：{num}')
#7、列表解析
num = [i**3 for i in range(1,11)]
print(f'1-10每个数的立方为：{num}')