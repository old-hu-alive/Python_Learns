# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/20 21:54
@Auth ： 小胡
@File ：多线程.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
    进程是执行中的程序
    拥有独立的地址，内存，数据栈
    操作系统管理
    进程之间并行执行 --- 同时执行
    线程：
        在进程下执行的，一个进程可以包含多个线程，线程间数据共享
        多线程并发执行 --- 交互执行
        多线程数据不同步，需要执行同步原语
'''
import threading

def num1():
    print(1)
def num2():
    print(2)
def main():
    for i in range(3):
        t1 = threading.Thread(target=num1,)
        t2 = threading.Thread(target=num2,)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
if __name__ == '__main__':
    main()