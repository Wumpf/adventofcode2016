#!/usr/bin/python3

# invalid variable name
# pylint: disable=C0103
# Missing function docstring
# pylint: disable=C0111
# Line too long
# pylint: disable=C0301

# Example
# data = """5-8
# 0-2
# 4-7"""
# maxip = 9

# puzzle input
with open('input.txt', 'rt') as f:
   data = f.read()
maxip = 4294967295

intervals = [(int(line.split('-')[0]), int(line.split('-')[1])) for line in data.splitlines()]
intervals.sort()    # sorts by first number

minip = 0

numfree = 0
for begin, end in intervals:
    if minip >= begin:
        minip = max(end+1, minip)
    else:
        numfree += begin - minip
        print(minip)
        minip = end+1

numfree += maxip - minip + 1
print("number of free ips:", numfree)

#print(intervals)