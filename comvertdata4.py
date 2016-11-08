import csv
import datetime
import os.path
import sys

def get_file_name(fname, day):
    one_day = datetime.timedelta(days=1)
    while 1:
        day = day - one_day
        fname = day.strftime("pick_stocks_%Y-%m-%d.csv")
        if os.path.isfile(fname):
            break
        else:
            continue
    return fname

day = datetime.date(2016, 11, 2)

fname1 = ""

fname1 = get_file_name(fname1, day)

print fname1
print day
fname1 = get_file_name(fname1, day)

print fname1
