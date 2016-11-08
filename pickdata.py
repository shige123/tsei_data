import csv
import sys

args = sys.argv

for fname in args:
    if fname == "pickdata.py":
        continue
    fin = open(fname,'r')
    fout = open('pick_' + fname,'w')

    reader = csv.reader(fin)
    writer = csv.writer(fout)
    
    header = next(reader)
    judge = next(reader)
    tmp = []

    tmp.append(header[1])
    tmp.append(header[6])
    writer.writerow(tmp)
    del tmp[:]
    
    tmp.append(judge[1])
    tmp.append(judge[6])
    writer.writerow(tmp)
    del tmp[:]

    count = 0
    for row in reader:
        if row[2] == judge[2]:
            tmp.append(row[1])
            tmp.append(row[6])
            writer.writerow(tmp)
            del tmp[:]
            count += 1
    print count
            
    fin.close()
    fout.close()
