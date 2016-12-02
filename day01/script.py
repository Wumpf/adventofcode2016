#!/usr/bin/python3

# test input
#data = 'R2, L3'
#data = 'R2, R2, R2'
#data = 'R5, L5, R5, R3'
#data = 'R10, R0, R10, R0'
# file input
data = open('input.txt').read()

dir = (0, 1)
pos = [0, 0]

for instr in data.split(','):
    instr = instr.strip()
    if instr[0] == 'R':
        dir = (dir[1], -dir[0]) 
    else:
        dir = (-dir[1], dir[0])

    walkDist = int(instr[1:])

    pos[0] += dir[0] * walkDist
    pos[1] += dir[1] * walkDist

print('pos:', pos)
print('dist:', abs(pos[0]) + abs(pos[1]))
