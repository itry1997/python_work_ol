#encoding='utf-8'
import csv
import os
with open("C:\\Users\\lenovo\\Desktop\\2010","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "date", "time","path"])
path='D:/1分钟数据/Stk_1F_2010/'
for filename in os.listdir(r'D:/1分钟数据/Stk_1F_2010'):
    count = len(open(path+filename, 'rU').readlines())
    a = -1
    while a < count / 240:
        a += 1
        with open(path+filename, 'U') as csvfile:
            reader = csv.reader(csvfile)
            # 收盘价一行
            for i, rows in enumerate(reader):
                if i == 239 + a * 240:
                    row_i = rows #前一天收盘价一行
                    # print((i + 1), "行最后一分钟：", [row_i]
            # 收盘价
            for row in row_i:
                close = row_i[5]
            #print(filename,row_i[0], "收盘价:", close)

        # 每一天的最高价与前一天收盘价比较
        with open(path+filename, 'U') as csvfile:
            reader = csv.reader(csvfile)
            # 最高价数据
            for j, row in enumerate(reader):
                if j >= 240 + a * 240 and j <= 479 + a * 240:
                    highest = row[3]
                    date=row[0]
                    time=row[1]
                    #print(reader.line_num,highest)
                    if float(highest) >= ( 1.0994*float(close)):
                        #print(filename,date,time,highest)
                        with open("C:\\Users\\lenovo\\Desktop\\2010", "a") as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([filename,date,time,path])
                        break
                    j+=1

with open('C:\\Users\\lenovo\\Desktop\\2010', 'rt')as fin:  # 读有空行的csv文件，舍弃空行
    lines = ''
    for line in fin:
        if line != '\n':
            lines += line
with open('C:\\Users\\lenovo\\Desktop\\2010', 'wt')as fout:  # 再次文本方式写入，不含空行
    fout.write(lines)