#!/usr/bin/evn python3
# -*- coding utf-8 -*-

import time


def deco(func):
    """
    统计方法执行耗时
    :param func: 
    :return: 
    """

    def func_wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print('func() elasped time:%f ms' % msecs)

    return func_wrapper


def myfunc():
    print('start myfunc')
    # 暂停0.6秒
    time.sleep(0.6)
    print('end myfunc')


if __name__ == '__main__':
    """
    Python中一切都是对象，函数也是，所以代码中改变了”myfunc”对应的函数对象
    """
    print('myfunc is :', myfunc.__name__)
    myfunc = deco(myfunc)
    print('myfunc is :', myfunc.__name__)
    print('===========================')
    myfunc()
