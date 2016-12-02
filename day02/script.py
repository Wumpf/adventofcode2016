#!/usr/bin/python3

# test input
#data = '''ULL
#RRDDD
#LURDL
#UUUUD'''
# file input
data = open('input.txt').read()

keypad = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'))
pos = [1, 1] # y, x
solution = ''

for instr in data.splitlines():
    for d in instr:
        # parse
        if d is 'R': # right
            pos[1] += 1
        elif d is 'L': # left
            pos[1] -= 1
        elif d is 'U': # up
            pos[0] -= 1
        elif d is 'D': # down
            pos[0] += 1
        else:
            raise RuntimeError('Unknown direction letter! ' + d)
        # clamp
        pos[0] = max(min(pos[0], 2), 0)
        pos[1] = max(min(pos[1], 2), 0)
    # write to output
    print(pos)
    solution += keypad[pos[0]][pos[1]]

print('solution:', solution)
