import csv

def databary(f1, f2, bary, count):
    reader1 = csv.reader(f1)
    header1 = next(reader1)
    reader2 = csv.reader(f2)
    header2 = next(reader2)
    
    judge = next(reader1)
    row2 = next(reader2)
    
    judge[3] = judge[3].replace('.00','')
    judge[6] = judge[6].replace('.00','')
    row2[6] = row2[6].replace('.00','')
    
    if (float(judge[6]) - float(judge[3])) > 0:
        print judge[6]
        print row2[6]
        if 0.05 < (float(row2[6]) - float(judge[6])):
            bary.extend([1,1])
        else:
            bary.extend([0,1])
    else:
        if 0.05 < (float(row2[6]) - float(judge[6])):
            bary.extend([1,0])
        else:
            bary.extend([0,0])
            
            for row1 in reader1:
                row2 = next(reader2)
                if row1[2] == judge[2]:
                    count+=1
                    row1[3] = row1[3].replace('.00','')
                    row1[6] = row1[6].replace('.00','')
                    row2[6] = row2[6].replace('.00','')
                    if (float(row1[6]) - float(row1[3])) > 0:
                        if 0.05 < ((float(row2[6]) - float(row1[3])) / float(row1[6])):
                            bary.extend([1,1])
                            print "T,T"
                        else:
                            bary.extend([1,0])
                            print "T,F"
                    else:
                        if 0.05 < ((float(row2[6]) - float(row1[3])) / float(row1[6])):
                            bary.extend([0,1])
                            print "F,T"
                        else:
                            bary.extend([0,0])
                            print "F,F"
    return count
def printdata(a):
    print a
                            
count = 1

file1 = open('stocks_2016-11-01.csv','rb')
file2 = open('stocks_2016-11-02.csv','rb')
fout = open ('data.tsei','wb')

b_ary = bytearray(['t','s','e','i'])
b_ary.extend([0x7,0xC2])
b_ary.extend([0,2])

databary(file1, file2, b_ary, count)

printdata(count)
fout.write(b_ary)
file1.close()
file2.close()
fout.close()
