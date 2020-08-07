#!/usr/bin/env python3
'''
Filename: payroll.py
Author: Nahia Akter
Student no.: 301106956
Description: Dispaly the data.txt file in a tabular manner
'''

from tabulate import tabulate

print (tabulate([], headers=['Employee No.','Employee Name', 'Hours Worked']))
with open("data.txt", "r") as data:
    for line in data:
        currentline = line.strip().split(',')
        table = (currentline[0]) + (currentline[1]) + (currentline[2])
        print (table)

