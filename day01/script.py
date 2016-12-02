#!/usr/bin/python3

# test input
#data = 'R2, L3'
#data = 'R2, R2, R2'
#data = 'R5, L5, R5, R3'
#data = 'R10, R0, R10, R0'
# file input
data = open('input.txt').read()

orientation = 0
pos = [0,0]

for instr in data.split(','):
    instr = instr.strip()
    orientation += 1 if instr[0] == 'R' else -1

    if orientation == 3:
        orientation = -1
    elif orientation == -3:
        orientation = 1

    walkDist = int(instr[1:])

    if abs(orientation) == 1: # Moving left/right
        pos[0] += walkDist * orientation
    elif orientation == 0: # Moving up
        pos[1] += walkDist
    else: # Moving down (two possible values for orientation)
        pos[1] -= walkDist

print('pos:', pos)
print('dist:', abs(pos[0]) + abs(pos[1]))
