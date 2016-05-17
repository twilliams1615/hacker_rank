#!/bin/python

## https://www.hackerrank.com/challenges/python-time-delta

from datetime import datetime

FMT = "%a %d %b %Y %H:%M:%S %z"
for i in range(int(input())) :
    t1 = datetime.strptime(input(), FMT)
    t2 = datetime.strptime(input(), FMT)
    print(abs(int((t1-t2).total_seconds())))

