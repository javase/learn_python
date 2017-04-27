#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pinyin


def to_pinyin(var_str):
    """
    汉字[钓鱼岛是中国的]=>拼音[diaoyudaoshizhongguode]
    汉字[我是shui]=>拼音[woshishui]
    汉字[AreYou好]=>拼音[AreYouhao]
    汉字[None]=>拼音[]
    汉字[]=>拼音[]
    :param var_str:  str 类型的字符串
    :return: 汉字转小写拼音
    """
    if isinstance(var_str, str):
        if var_str == 'None':
            return ""
        else:
            return pinyin.get(var_str, format='strip', delimiter="")
    else:
        return '类型不对'


if __name__ == '__main__':
    list = ['钓鱼岛是中国的', '我是shui', 'AreYou好', None, '']
    for i in list:
        print('汉字[%s]=>拼音[%s]' % (i, to_pinyin(str(i))))
