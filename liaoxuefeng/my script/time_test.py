#!/usr/bin/evn python3
# -*- coding utf-8 -*-

import time


def getExportFileName(name):
    ISOTIMEFORMAT = '%Y%m%d%H%M'
    time_str = time.strftime(ISOTIMEFORMAT, time.localtime())
    result = name + '-' + time_str + '.xlsx'
    return result


print(getExportFileName('未命名表格'))
