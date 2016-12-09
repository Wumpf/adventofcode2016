#!/usr/bin/python3
from collections import Counter

# test
# screensize = (7, 3)
# data = '''rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1''' 

# file input
screensize = (50, 6)
with open('input.txt', 'rt') as f:
    data = f.read()

screen = [['.' for x in range(screensize[0])] for y in range(screensize[1])]

for command in data.splitlines():
    tokens = command.split(' ')
    if tokens[0] == 'rect':
        size_instr_split = tokens[1].split('x')
        size = (int(size_instr_split[0]), int(size_instr_split[1]))
        for x in range(size[0]):
            for y in range(size[1]):
                screen[y][x] = '#'
    if tokens[0] == 'rotate':
        by = int(tokens[-1])
        where = int(tokens[2].split('=')[1])
        if tokens[1] == 'column':
            oldColum = [screen[y][where] for y in range(screensize[1])]
            for y in range(screensize[1]):
                readpos = (y - by) % screensize[1]
                screen[y][where] = oldColum[readpos]
        else:
            oldRow = [screen[where][x] for x in range(screensize[0])]
            for x in range(screensize[0]):
                readpos = (x - by) % screensize[0]
                screen[where][x] = oldRow[readpos]

numactive = 0
for line in screen:
    numactive += line.count('#')
    print(''.join(line))
print(numactive)