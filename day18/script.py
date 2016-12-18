#!/usr/bin/python3
import time

# invalid variable name
# pylint: disable=C0103
# Missing function docstring
# pylint: disable=C0111
# Line too long
# pylint: disable=C0301

# Example
#startstring = '..^^.'
#target_row_num = 3
#startstring = '.^^.^.^^^^'
#target_row_num = 10
# puzzle input
startstring = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'
target_row_num = 400000

prevrow = [c == '^' for c in startstring]
newrow = prevrow.copy()
num_columns = len(prevrow)
num_safe = sum(0 if f else 1 for f in prevrow)


before = time.clock()

right = False
for i in range(target_row_num-1):
    left = False
    center = prevrow[0]

    for c in range(num_columns-1):
        right = prevrow[c+1]
        newrow[c] = left ^ right  # Yes, this is what the rules boil down to.
        left, center = center, right
    newrow[-1] = left   # right is false.

    num_safe += sum(0 if f else 1 for f in newrow)
    newrow, prevrow = prevrow, newrow

after = time.clock()

print('num safe tiles:', num_safe, '-', after-before, 's')
