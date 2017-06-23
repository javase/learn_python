#!/usr/bin/evn python3
# -*- coding utf-8 -*-

import time


def deco_1(func):
    """
    统计方法执行耗时
    :param func: 
    :return: 
    """
    print('enter into deco_1')

    def wrapper(a, b):
        print('enter into deco_1_wrapper')
        func(a, b)

    return wrapper


def deco_2(func):
    """
    统计方法执行耗时
    :param func: 
    :return: 
    """
    print('enter into deco_2')

    def wrapper(a, b):
        print('enter into deco_2_wrapper')
        func(a, b)

    return wrapper


@deco_1
@deco_2
def addFunc(a, b):
    """
    对于Python中的”@”语法糖，装饰器的调用顺序与使用 @ 语法糖声明的顺序相反
    :param a: 
    :param b: 
    :return: 
    """
    print('result is %d' % (a + b))


if __name__ == '__main__':
    addFunc(2, 3)
