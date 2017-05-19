# -*- coding: utf-8 -*-
import xlrd
from datetime import date, datetime


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'py.xlsx')
    # 获取所有sheet
    print(workbook.sheet_names())
    # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('Sheet1')

    # sheet的名称，行数，列数
    print('sheet名称:[%s],行数：[%d]，列数：[%d]' % (sheet2.name, sheet2.nrows, sheet2.ncols))

    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(2)  # 获取第三列内容
    print('获取第四行内容:', rows)

    print("获取第三列内容:", cols)

    # 获取单元格内容
    print('获取单元格内容')
    print(sheet2.cell(1, 0).value.encode('utf-8'))

    print(sheet2.cell_value(1, 0).encode('utf-8'))

    print(sheet2.row(1)[0].value.encode('utf-8'))

    # 获取单元格内容的数据类型  ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    print('获取单元格内容的数据类型:', sheet2.cell(1, 0).ctype)

    col0 = sheet2.col_values(0)
    print('读取第一列内容：', col0)  # 我们发现，读取的列中，存在空白格
    # print('type(range(col0)):',type(range(col0)))
    for c in range(sheet2.nrows):
        print('', sheet2.col_values(0)[c])

    print('接下来，读取合并单元格的内容')
    #workbook = xlrd.open_workbook(r'py.xlsx', formatting_info=True)
    print('merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),其中[row,row_range)包括row,不包括row_range,col也是一样，即(1, 3, 4, 5)的含义是：第1到2行（不包括3）合并，(7, 8, 2, 5)的含义是：第2到4列合并')
    print('合并单元格有：',sheet2.merged_cells)
    merge = []
    for (rlow, rhigh, clow, chigh) in sheet2.merged_cells:
        merge.append([rlow, clow])
    for index in merge:
        print('合并单元格的值有：' ,sheet2.cell_value(index[0],index[1]))


if __name__ == '__main__':
    read_excel()
