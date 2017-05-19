# -*- coding: utf-8 -*-
import xlrd


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'py.xlsx')
    # 获取所有sheet
    print('打印所有sheet:', workbook.sheet_names())

    sheet2 = workbook.sheet_by_index(0)  # sheet索引从0开始
    rows_num = sheet2.nrows
    cols_num = sheet2.ncols

    for r in range(rows_num):
        print('-------------------------------------')
        entity = []
        entity_str = ''
        for c in range(cols_num):
            cell_value = sheet2.row_values(r)[c]
            print('第%d行第%d列的值：[%s]' % (r, c, sheet2.row_values(r)[c]))
            if (cell_value is None or cell_value == ''):
                cell_value = (get_merged_cells_value(sheet2, r, c))
            # 构建Entity
            the_key = 'column' + str(c + 1);
            entity.append({the_key: cell_value})
            entity_str = entity_str + ',' + str(cell_value)
            print('entity:[%s]' % entity)
            print(entity_str)


def get_merged_cells(sheet):
    return sheet.merged_cells


def get_merged_cells_value(sheet, row_index, col_index):
    """
    先判断给定的单元格，是否属于合并单元格；
    如果是合并单元格，就返回合并单元格的内容
    :return:
    """
    merged = get_merged_cells(sheet)
    # [(1, 14, 0, 1), (14, 27, 0, 1), (27, 40, 0, 1), (40, 53, 0, 1), (1, 14, 3, 4), (14, 27, 3, 4), (27, 40, 3, 4),
    # (40, 51, 3, 4), (1, 13, 6, 7), (14, 26, 6, 7), (27, 39, 6, 7), (40, 52, 6, 7)]
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                # print('该单元格[%d,%d]属于合并单元格，值为[%s]' % (row_index, col_index, cell_value))
                return cell_value
                break
    return None


if __name__ == "__main__":
    read_excel()
