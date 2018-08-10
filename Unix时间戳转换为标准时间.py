#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

import time
import xlrd
import math

xlrd.Book.encoding = "utf-8"
file_path = 'D:\\数学建模\\2018年D题-基于多源监测数据的道路交通流状态重构研究\\浮动车数据\\date=20180325\\f_20180325.xlsx'

def read_file():
    data = xlrd.open_workbook(file_path)  # 打开文件
    table = data.sheet_by_index(0)  # 取第一张工作簿
    rows_count = table.nrows  # 总行数
    cols_count = table.ncols  # 总列数
    #print(rows_count)

    for row in range(0,rows_count):
        unix_time = math.floor(table.cell(row,0).value)
        time_local = time.gmtime(unix_time)
        # 转换成新的时间格式(2018-03-25 20:28:54)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        print(dt)

read_file()