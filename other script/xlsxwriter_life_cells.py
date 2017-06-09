import xlsxwriter
import datetime
import time
from dateutil import rrule


def writeExcel(year_birth, month_birth, life_years):
    """
    根据出生年月、生命总长度，生成Excel
    :param year_birth: 
    :param month_birth: 
    :param life_years: 
    :return: 
    """
    # 一年几个月
    month = 12

    file_path = '/usr/local/dir_samba/files/life_cells/'
    file_name = file_path + str(year_birth) + '.' + str(month_birth) + "-life_cells.xlsx"

    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet('%s.%s-%dyears' % (year_birth, month_birth, life_years))
    column_index = 0

    month_diff = get_birth_to_now_monthdiff(year_birth, month_birth)

    format_passed = workbook.add_format()  # 定义format格式对象
    setFormatPassed(format_passed)
    format_future = workbook.add_format()
    setFormatFuture(format_future)

    # 一共30*30列
    for i in range(month * life_years):
        yu = i % 30

        # 单元格内容
        cell_value = str(month_birth)
        # 设置单元格宽度
        worksheet.set_column(column_index, column_index, 6)
        # 从头开始
        if month_birth == month:
            month_birth = 0
            year_birth += 1
        # 1月份追加年份
        if month_birth == 1:
            # 追加年份
            cell_value = str(year_birth) + '.' + cell_value
            # 设置单元格宽度
            worksheet.set_column(column_index, column_index, 6)

        # 先确认单元格位置 - For Debug
        # print('%s.[%s,%s,%s]' % (i + 1, column_index, yu, cell_value))
        # 已经度过的月份
        if i < month_diff:
            worksheet.write_string(column_index, yu, cell_value, format_passed)
        else:
            worksheet.write_string(column_index, yu, cell_value, format_future)

        # 下一行
        if yu == 29:
            column_index += 1
        month_birth += 1
        # end for
    print('您的进度表格已制作完成，请到[%s]目录查看' % (file_path))
    workbook.close()


def setFormatPassed(format_passed):
    format_passed.set_border(1)  # 定义format对象单元格边框加粗（1个像素）的格式
    format_passed.set_bg_color('#cccccc')  # 定义format_title对象单元格背景颜色为'#cccccc'的格式
    format_passed.set_align('center')  # 定义format_title对象单元格为居中对齐格式
    format_passed.set_bold()  # 定义format_title对象单元格内容加粗的格式


def setFormatFuture(format_future):
    format_future.set_align('center')


def get_birth_to_now_monthdiff(birthY, birthM):
    """
    根据出生年月，计算到当前时间，过去了多少个月（由于出生日(day)不影响计算结果，固不用传递）
    :param birthY: 出生年份
    :param birthM: 出生月份
    :return: 出生年月和当前时间，相差多少个月
    """
    nowY = time.strftime('%Y', time.localtime(time.time()))
    nowM = time.strftime('%m', time.localtime(time.time()))
    nowD = time.strftime('%d', time.localtime(time.time()))
    # print('当前日期为：%s-%s-%s' % (nowY, nowM, nowD))
    month_diff = get_month_diff(birthY, birthM, 1, int(nowY), int(nowM), int(nowD))
    # print(month_diff)
    return month_diff


def get_month_diff(y1, m1, d1, y2, m2, d2):
    """
    获取两个日期的月份差
    :param y1: 起始年
    :param m1: 起始月
    :param d1: 起始日
    :param y2: 要比较的年
    :param m2: 要比较的月
    :param d2: 要比较的日
    :return: 两个日期之间的月份差
    """
    d1 = datetime.date(y1, m1, d1)
    d2 = datetime.date(y2, m2, d2)

    months = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()
    return months


def client():
    """
    接受客户端输入
    :return: void
    """
    if_continue = True
    # 如果输入有误，则重新输入
    while (if_continue):
        try:
            print('请输入出生年份(如1990)：')
            # 出生年份
            year_birth = int(input())
            print('请输入出生月份(如1)：')
            # 出生月份
            month_birth = int(input())
            print('请输入年限(如75)：')
            # 按照多少年的总时长计算
            life_years = int(input())
            if_continue = False
        except ValueError as e:
            print('您的输入有误，只能输入数字，请重试')

    print('您的出生年月为[%s年%s月]，将按照总年数[%s年]计算生命进度表格' % (year_birth, month_birth, life_years))
    writeExcel(year_birth, month_birth, life_years)


if __name__ == "__main__":
    client()
    # writeExcel()
    # get_birth_to_now_monthdiff(1984, 9, 10)
