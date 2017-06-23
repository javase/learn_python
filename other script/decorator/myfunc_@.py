#!/usr/bin/evn python3
# -*- coding utf-8 -*-

import time


def deco(func):
    """
    统计方法执行耗时
    :param func: 
    :return: 
    """

    def func_wrapper(a, b):
        startTime = time.time()
        func(a, b)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print('func() elasped time:%f ms' % msecs)

    return func_wrapper


@deco
def addFunc(a, b):
    print('start addFunc')
    # 暂停0.6秒
    time.sleep(0.6)
    print('result is %d' % (a + b))
    print('end addFunc')


if __name__ == '__main__':
    addFunc(5, 7)
