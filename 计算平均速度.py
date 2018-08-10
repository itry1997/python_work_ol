#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*

import xlrd
#变量初始化
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

v0 = v1 = v2 = v3 = v4 = v5 = v6 = v7 = v8 = v9 = v10 = v11 = v12 = v13 = v14 = v15 = v16 = v17 = v18 = v19 = v20 = v21 = v22 = v23 =0

file_path = 'F:\\QQ文件\\605&606.xlsx'
xlrd.Book.encoding = "utf-8"

file  = xlrd.open_workbook(file_path) #打开文件
table = file.sheet_by_index(6) #取第x张工作簿
rows_count = table.nrows  #总行数
cols_count = table.ncols  #总列数

for row in range(0,rows_count):
    Row = table.row_values(row) #读取某行数据，返回值为列表形式
    if Row[0] == '00':
        hour_00 += 1
        v0 += Row[4]
    elif Row[0] == '01':
        hour_01 += 1
        v1 += Row[4]
    elif Row[0] == '02':
        hour_02 += 1
        v2 += Row[4]
    elif Row[0] == '03':
        hour_03 += 1
        v3 += Row[4]
    elif Row[0] == '04':
        hour_04 += 1
        v4 += Row[4]
    elif Row[0] == '05':
        hour_05 += 1
        v5 += Row[4]
    elif Row[0] == '06':
        hour_06 += 1
        v6 += Row[4]
    elif Row[0] == '07':
        hour_07 += 1
        v7 += Row[4]
    elif Row[0] == '08':
        hour_08 += 1
        v8 += Row[4]
    elif Row[0] == '09':
        hour_09 += 1
        v9 += Row[4]
    elif Row[0] == '10':
        hour_10 += 1
        v10 += Row[4]
    elif Row[0] == '11':
        hour_11 += 1
        v11 += Row[4]
    elif Row[0] == '12':
        hour_12 += 1
        v12 += Row[4]
    elif Row[0] == '13':
        hour_13 += 1
        v13 += Row[4]
    elif Row[0] == '14':
        hour_14 += 1
        v14 += Row[4]
    elif Row[0] == '15':
        hour_15 += 1
        v15 += Row[4]
    elif Row[0] == '16':
        hour_16 += 1
        v16 += Row[4]
    elif Row[0] == '17':
        hour_17 += 1
        v17 += Row[4]
    elif Row[0] == '18':
        hour_18 += 1
        v18 += Row[4]
    elif Row[0] == '19':
        hour_19 += 1
        v19 += Row[4]
    elif Row[0] == '20':
        hour_20 += 1
        v20 += Row[4]
    elif Row[0] == '21':
        hour_21 += 1
        v21 += Row[4]
    elif Row[0] == '22':
        hour_22 += 1
        v22 += Row[4]
    elif Row[0] == '23':
        hour_23 += 1
        v23 += Row[4]
#判断
if v0 == 0:
    average_00 = 0
else:
    average_00 = v0/hour_00
if v1 == 0:
    average_01 = 0
else:
    average_01 = v1/hour_01
if v2 == 0:
    average_02 = 0
else:
    average_02 = v2/hour_02
if v3 == 0:
    average_03 = 0
else:
    average_03 = v3/hour_03
if v4 == 0:
    average_04 = 0
else:
    average_04 = v4/hour_04
if v5 == 0:
    average_05 = 0
else:
    average_05 = v5/hour_05
if v6 == 0:
    average_06 = 0
else:
    average_06 = v6/hour_06
if v7 == 0:
    average_07 = 0
else:
    average_07 = v7/hour_07
if v8 == 0:
    average_08 = 0
else:
    average_08 = v8/hour_08
if v9 == 0:
    average_09 = 0
else:
    average_09 = v9/hour_09
if v10 == 0:
    average_10 = 0
else:
    average_10 = v10/hour_10
if v11 == 0:
    average_11 = 0
else:
    average_11 = v11/hour_11
if v12 == 0:
    average_12 = 0
else:
    average_12 = v12/hour_12
if v13 == 0:
    average_13 = 0
else:
    average_13 = v13/hour_13
if v14 == 0:
    average_14 = 0
else:
    average_14 = v14/hour_14
if v15 == 0:
    average_15 = 0
else:
    average_15 = v15/hour_15
if v16 == 0:
    average_16 = 0
else:
    average_16 = v16/hour_16
if v17 == 0:
    average_17 = 0
else:
    average_17 = v17/hour_17
if v18 == 0:
    average_18 = 0
else:
    average_18 = v18/hour_18
if v19 == 0:
    average_19 = 0
else:
    average_19 = v19/hour_19
if v20 == 0:
    average_20 = 0
else:
    average_20 = v20/hour_20
if v21 == 0:
    average_21 = 0
else:
    average_21 = v21/hour_21
if v22 == 0:
    average_22 = 0
else:
    average_22 = v22/hour_22
if v23 == 0:
    average_23 = 0
else:
    average_23 = v23/hour_23

#打印结果
print(average_00)
print(average_01)
print(average_02)
print(average_03)
print(average_04)
print(average_05)
print(average_06)
print(average_07)
print(average_08)
print(average_09)
print(average_10)
print(average_11)
print(average_12)
print(average_13)
print(average_14)
print(average_15)
print(average_16)
print(average_17)
print(average_18)
print(average_19)
print(average_20)
print(average_21)
print(average_22)
print(average_23)