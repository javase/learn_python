#!/usr/bin/evn python3
# -*- coding utf-8 -*-

import time


def deco(arg=True):
    """
    统计方法执行耗时
    :param func: 
    :return: 
    """
    if arg:
        def _deco(func):
            def func_wrapper(*args, **kwargs):
                startTime = time.time()
                func(*args, **kwargs)
                endTime = time.time()
                msecs = (endTime - startTime) * 1000
                print('func() elasped time:%f ms' % msecs)

            return func_wrapper
    else:
        def _deco(func):
            return func
    return _deco


@deco(False)
def myFunc():
    print('start myfunc')
    # 暂停0.6秒
    time.sleep(0.6)
    print('end myfunc')


@deco(True)
def addFunc(a, b):
    print('start addFunc')
    # 暂停0.6秒
    time.sleep(0.6)
    print('result is %d' % (a + b))
    print('end addFunc')


@deco(True)
def otherFunc(a, b, c):
    print('start otherFunc')
    # 暂停0.6秒
    time.sleep(0.6)
    print('result is %d' % (a + b + c))
    print('end otherFunc')


if __name__ == '__main__':
    print('myFunc is', myFunc.__name__)
    myFunc()
    print("===============")
    print('addFunc is', addFunc.__name__)
    addFunc(3, 8)
    print("===============")
    print('otherFunc is', otherFunc.__name__)
    otherFunc(3, 8, 9)
