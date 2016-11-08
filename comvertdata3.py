import csv
import datetime
import os.path

def databary(f1, f2, f3, bary):
    debug = 0
    reader1 = csv.reader(f1)
    header1 = next(reader1)
    reader2 = csv.reader(f2)
    header2 = next(reader2)
    reader3 = csv.reader(f3)
    header3 = next(reader3)
    
    judge = next(reader1)
    row2 = next(reader2)
    row3 = next(reader3)
    
    judge[6] = judge[6].replace('.00','')
    row2[6] = row2[6].replace('.00','')
    row3[6] = row3[6].replace('.00','')
    print judge[6], row2[6], row3[6]
    
    if (float(row2[6]) - float(judge[6])) > 0:
        if 0.05 < (float(row3[6]) - float(row2[6])/float(row2[6])):
            bary.extend([1,1])
        else:
            bary.extend([1,0])
    else:
        if 0.05 < (float(row3[6]) - float(row2[6])/float(row2[6])):
            bary.extend([0,1])
        else:
            bary.extend([0,0])
            
    for row1 in reader1:
        row2 = next(reader2)
        row3 = next(reader3)
        debug+=1
        print debug
        print row1[6], row2[6], row3[6]
        if row2[2] == judge[2]:
            row1[6] = row1[6].replace('.00','')
            row2[6] = row2[6].replace('.00','')
            row3[6] = row3[6].replace('.00','')
            print row1[6], row2[6], row3[6]
            if (float(row2[6]) - float(row1[6])) > 0:
                if 0.05 < ((float(row3[6]) - float(row2[6])) / float(row2[6])):
                    bary.extend([1,1])
                    #print "T,T"
                else:
                    bary.extend([1,0])
                    #print "T,F"
            else:
                if 0.05 < ((float(row3[6]) - float(row2[6])) / float(row2[6])):
                    bary.extend([0,1])
                    #print "F,T"
                else:
                    bary.extend([0,0])
                    #print "F,F"

#def fcheck(fname, day):


count = 10
fout = open ('data.tsei','wb')

day = datetime.date(2016, 11, 2)
one_day = datetime.timedelta(days=1)

print day

fname3 = day.strftime("stocks_%Y-%m-%d.csv")

file3 = open(fname3, 'rb')

while 1:
    day = day - one_day
    fname2 = day.strftime("stocks_%Y-%m-%d.csv")
    if os.path.isfile(fname2):
        break
    else:
        continue
file2 = open(fname2, 'rb')
while 1:
    day = day - one_day
    fname1 = day.strftime("stocks_%Y-%m-%d.csv")
    if os.path.isfile(fname1):
        break
    else:
        continue

file1 = open(fname1, 'rb')

b_ary = bytearray(['t','s','e','i'])
b_ary.extend([0x7,0xC2])
b_ary.extend([0,2])
#import pdb; pdb.set_trace()


for num in range(0, count):
    databary(file1, file2, file3, b_ary)
    file1.close()
    file2.close()
    file3.close()
    fname2 = fname1
    fname3 = fname2
    file2 = open(fname2, 'rb')
    file3 = open(fname3, 'rb')
    while 1:
        day = day - one_day
        fname1 = day.strftime("stocks_%Y-%m-%d.csv")
        if os.path.isfile(fname1):
            break
        else:
            continue
    print fname1, fname2, fname3
    file1 = open(fname1, 'rb')

print count
fout.write(b_ary)
file1.close()
file2.close()
file3.close()
fout.close()
