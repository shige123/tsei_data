# -*- coding: utf-8 -*-
import codecs
import csv
import datetime
import os.path
import sys

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def get_file_name(day):
    one_day = datetime.timedelta(days=1)
    print one_day
    print day
    while 1:
        day = day - one_day
        fname = day.strftime("pick_stocks_%Y-%m-%d.csv")
        if os.path.isfile(fname):
            break
        else:
            continue
    return fname, day

def check_company(company, data):
    count_num = 0
    for a in data:
        if company == a[0]:
            return count_num
        count_num+=1
    return -1


fout = open('indata.tsei','wb')

day = datetime.date(2016, 11, 2)

fname1,day = get_file_name(day)
f1 = open(fname1,"rb")
reader1 = csv.reader(f1)
header = next(reader1)
com_name = []
count = 0
for row in reader1:
    com_name.append(row[0])
    count+=1
f1.close()

fname2,day = get_file_name(day)
print fname2

fname3,day = get_file_name(day)
print fname3

bary = bytearray(['t','s','e','i'])
bary.extend([0x7,0xC2])
bary.extend([0,0x01])

for date in range(0,1):
    f1 = open(fname1,"rb")
    reader1 = csv.reader(f1)
    header = next(reader1)

    f2 = open(fname2,"rb")
    reader2 = csv.reader(f2)
    header = next(reader2)

    f3 = open(fname3,"rb")
    reader3 = csv.reader(f3)
    header = next(reader3)
    data1 = []
    data2 = []
    data3 = []

    for row in reader1:
        data1.append(row)
    for row in reader2:
        data2.append(row)
    for row in reader3:
        data3.append(row)
        
    for num in range(0,count):
        data1_num = check_company(com_name[num], data1)
        data2_num = check_company(com_name[num], data2)
        data3_num = check_company(com_name[num], data3)
        
        if data2_num != -1 and data3_num != -1:
            #print num, "true"
            if (float(data3[data3_num][1]) - float(data2[data2_num][1])) > 0:
                bary.append(1)
            else:
                bary.append(0)
        else:
            #print num, "false"
            bary.append(0)
               
    f1.close()
    f2.close()
    f3.close()
    fname1 = fname2
    fname2 = fname3

print type(reader1)                
fout.write(bary)
f1.close()
f2.close()
f3.close()
fout.close()
