#!/bin/python

## https://www.hackerrank.com/challenges/finding-the-percentage

NStudents = int(raw_input())
record = {}
for i in range(0,NStudents):
    student_info = raw_input()
    name = student_info.split()
    record[name[0]] = [float(name[1]),float(name[2]),float(name[3])]
find_name = raw_input()
if record.has_key(find_name):
    print "{0:.2f}".format(sum(record[find_name])/3.0)
