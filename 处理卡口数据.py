#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

def file_name(file_dir):
    L = []
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root,file)) #root为路径，file为文件名
    #print(L)
    return L

def Print():
    print( str(hour_00))
    print( str(hour_01))
    print( str(hour_02))
    print( str(hour_03))
    print( str(hour_04))
    print( str(hour_05))
    print( str(hour_06))
    print( str(hour_07))
    print( str(hour_08))
    print( str(hour_09))
    print( str(hour_10))
    print( str(hour_11))
    print( str(hour_12))
    print( str(hour_13))
    print( str(hour_14))
    print( str(hour_15))
    print( str(hour_16))
    print( str(hour_17))
    print( str(hour_18))
    print( str(hour_19))
    print( str(hour_20))
    print( str(hour_21))
    print( str(hour_22))
    print( str(hour_23))

hour_00 = 0
hour_01 = 0
hour_02 = 0
hour_03 = 0
hour_04 = 0
hour_05 = 0
hour_06 = 0
hour_07 = 0
hour_08 = 0
hour_09 = 0
hour_10 = 0
hour_11 = 0
hour_12 = 0
hour_13 = 0
hour_14 = 0
hour_15 = 0
hour_16 = 0
hour_17 = 0
hour_18 = 0
hour_19 = 0
hour_20 = 0
hour_21 = 0
hour_22 = 0
hour_23 = 0

import xlrd
import re
import os

file_names = file_name('D:\\数学建模\\卡口数据\\02010137\\02010137-2018-3-30') #列表file_name中有文件夹中所有文件名称
for file_name in file_names:
    #name_split = re.split(r'[\\-]',file_name)
    #print(file_name)

    file_path = file_name
    xlrd.Book.encoding = "utf-8"
    data = xlrd.open_workbook(file_path) #打开文件

    table = data.sheet_by_index(0) #取第一张工作簿
    rows_count = table.nrows  #总行数
    cols_count = table.ncols  #总列数

    #print(rows_count)
    #print(cols_count)
    for row in range(0,rows_count):
        time_data = table.cell(row,2).value #读取时间列数据
        #print(time_data)
        m = re.split('\W+' , time_data)
        hours =(m[3:4]) #切片取数据hour
        #print(hours)

        if hours == ['00'] or hours == ['0']:
            hour_00 += 1
        elif hours == ['01'] or hours == ['1']:
            hour_01 += 1
        elif hours == ['02'] or hours == ['2']:
            hour_02 += 1
        elif hours == ['03'] or hours == ['3']:
            hour_03 += 1
        elif hours == ['04'] or hours == ['4']:
            hour_04 += 1
        elif hours == ['05'] or hours == ['5']:
            hour_05 += 1
        elif hours == ['06'] or hours == ['6']:
            hour_06 += 1
        elif hours == ['07'] or hours == ['7']:
            hour_07 += 1
        elif hours == ['08'] or hours == ['8']:
            hour_08 += 1
        elif hours == ['09'] or hours == ['9']:
            hour_09 += 1
        elif hours == ['10']:
            hour_10 += 1
        elif hours == ['11']:
            hour_11 += 1
        elif hours == ['12']:
            hour_12 += 1
        elif hours == ['13']:
            hour_13 += 1
        elif hours == ['14']:
            hour_14 += 1
        elif hours == ['15']:
            hour_15 += 1
        elif hours == ['16']:
            hour_16 += 1
        elif hours == ['17']:
            hour_17 += 1
        elif hours == ['18']:
            hour_18 += 1
        elif hours == ['19']:
            hour_19 += 1
        elif hours == ['20']:
            hour_20 += 1
        elif hours == ['21']:
            hour_21 += 1
        elif hours == ['22']:
            hour_22 += 1
        elif hours == ['23']:
            hour_23 += 1

Print()
