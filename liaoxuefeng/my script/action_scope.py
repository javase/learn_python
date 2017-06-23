#!/usr/bin/evn python3
# -*- coding utf-8 -*-

a_string = "This is a global variable"


def foo():
    print('locals():', locals())


print('globals():', globals())
foo()
