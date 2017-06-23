#!/usr/bin/evn python3
# -*- coding utf-8 -*-

class Foo(object):
    def __init__(self, var):
        super(Foo, self).__init__()
        self._var = var

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, var):
        """
        对于Python新式类（new-style class），如果将上面的 “@var.setter” 装饰器所装饰的成员函数去掉，
        则Foo.var 属性为只读属性，使用 “foo.var = ‘var 2′” 进行赋值时会抛出异常
        :param var: 
        :return: 
        """
        self._var = var


if __name__ == '__main__':
    foo = Foo('var 1')
    print(foo.var)
    foo = Foo('var 2')
    print(foo.var)
