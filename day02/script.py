#!/usr/bin/python3

# test input
#data = '''ULL
#RRDDD
#LURDL
#UUUUD'''
# file input
data = open('input.txt').read()

partTwo = True

keypad = ()
pos = []
if partTwo:
    keypad = (('x', 'x', '1', 'x', 'x'),
              ('x', '2', '3', '4', 'x'),
              ('5', '6', '7', '8', '9'),
              ('x', 'A', 'B', 'C', 'x'),
              ('x', 'x', 'D', 'x', 'x'))
    pos = [3, 0] # y, x
else:
    keypad = (('1', '2', '3'),
              ('4', '5', '6'),
              ('7', '8', '9'))
    pos = [1, 1] # y, x

solution = ''

for instr in data.splitlines():
    for d in instr:
        posBefore = pos.copy()
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
        # invalid moves
        if pos[0] < 0 or pos[0] >= len(keypad) or \
           pos[1] < 0 or pos[1] >= len(keypad[0]) or \
           keypad[pos[0]][pos[1]] == 'x':
            pos = posBefore
    # write to output
    print(pos)
    solution += keypad[pos[0]][pos[1]]

print('solution:', solution)
