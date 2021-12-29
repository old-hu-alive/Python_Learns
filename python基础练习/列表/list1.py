# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/25 22:38
@Auth ： 小胡
@File ：list1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

names = ['xiao hu', 'xiao lan', 'xiao huang', 'xiang lv']
# for i in names:
#     message = f'Hello,{i.title()}'
#     print(message)

# 列表方法：append(),将元素添加到列表末尾
new_name = 'xiao man'
names.append(new_name)
print(names)

# 列表方法：insert(),在列表的指定位置添加新元素，需要指定添加的元素的索引和值
names.insert(1, 'xiao wang')
print(names)

'''
删除元素：
    1、del 语句：知道要删除的元素在列表中的位置
    2、pop()：删除列表末尾的元素，并让你能接着使用它。 
              也可以使用pop()来删除列表中任意位置的元素，需要在括号中指定要删除元素的索引

    如果要从列表中删除一个元素，并且不再以任何方式使用它，就是用del 语句；
    如果要在删除元素后还能继续使用它，就是用方法 pop().

    3、remove()：只知道要删除的元素的值，可以使用remove()
                remove() 只删除第一个指定的值，如果要删除的值在列表中有多个，需要使用循环来删除。
'''
del names[-2]
print(names)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()  # 将列表末尾的元素删除，并赋值给popped_motorcycles
print(popped_motorcycles)  # 打印刚刚删除的元素

# 使用pop()来删除列表中任意位置的元素
motorcycles.pop(1)
print(motorcycles)

# 使用remove() 来删除列表中的元素
names.remove('xiao huang')
print(names)