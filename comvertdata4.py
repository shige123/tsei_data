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

fout = open('data.tsei','wb')

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
bary.extend([0,0x1E])

for date in range(0,30):
    f1 = open(fname1,"rb")
    reader1 = csv.reader(f1)
    header = next(reader1)

    f2 = open(fname2,"rb")
    reader2 = csv.reader(f2)
    header = next(reader2)

    f3 = open(fname3,"rb")
    reader3 = csv.reader(f3)
    header = next(reader3)
    
    row1 = next(reader1)
    row2 = next(reader2)
    row3 = next(reader3)
    
    for num in range(0,count):
        if com_name[num] == row3[0] and com_name[num] == row2[0]:
            print num, "true"
            if (float(row3[1]) - float(row2[1])) > 0:
                bary.append(1)
            else:
                bary.append(0)
        else:
            print num, "false"
            bary.append(0)
            
        if com_name[num] == row1[0]:
            if 0.05 < (float(row1[1]) - float(row2[1])/float(row2[1])):
                bary.append(1)
            else:
                bary.extend(0)
        else:
            bary.append(0)
        if num != count-1:        
            if com_name[num] == row1[0]:
                row1 = next(reader1)
                print "T"
            else:
                print "N"
            if com_name[num] == row2[0]:
                row2 = next(reader2)
            if com_name[num] == row3[0]:
                row3 = next(reader3)
    f1.close()
    f2.close()
    f3.close()
    fname1 = fname2
    fname2 = fname3
    fname3,day = get_file_name(day)
                
fout.write(bary)
f1.close()
f2.close()
f3.close()
fout.close()
