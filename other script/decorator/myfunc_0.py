#!/usr/bin/evn python3
# -*- coding utf-8 -*-

import time


def deco(func):
    """
    统计方法执行耗时
    :param func: 
    :return: 
    """
    startTime = time.time()
    func()
    endTime = time.time()
    msecs = (endTime - startTime) * 1000
    print('func() elasped time:%f ms' % msecs)


def myfunc():
    print('start myfunc')
    # 暂停0.6秒
    time.sleep(0.6)
    print('end myfunc')


if __name__ == '__main__':
    myfunc()
    print('--------------------')
    deco(myfunc)
