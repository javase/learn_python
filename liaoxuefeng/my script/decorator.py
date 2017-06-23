# -*- coding: utf-8 -*-
import functools


def now():
    print('2017.01.16')


f = now
print('调用函数 f():', f())
print('函数的名字，注意下划线是两根，f.__name__：', f.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


print('\n\n---------------------------------')


@log
def now2():
    print('2017年1月16日 16:51:02')


now2()

print('\n\n---------------------------------')


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log3('excute log3')
def now3():
    print('2017年1月16日 16:53:32')


now3()
