#!/usr/bin/python3

# test input
#data = 'R2, L3'
#data = 'R2, R2, R2'
#data = 'R5, L5, R5, R3'
#data = 'R10, R0, R10, R0'
# file input
data = open('input.txt').read()

dir = (0, 1)
pos = (0, 0)
locHist = { pos }
actualBunnyHeadquarterPos = None

for instr in data.split(','):
    instr = instr.strip()
    if instr[0] == 'R':
        dir = (dir[1], -dir[0])
    else:
        dir = (-dir[1], dir[0])

    walkDist = int(instr[1:])

    # Brute force solution: Just save every single position instead of doing tedious line intersection tests
    if actualBunnyHeadquarterPos is None:
        for i in range(walkDist):
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            if pos in locHist:
                actualBunnyHeadquarterPos = pos
            locHist.add(pos)
    else:
        pos = (pos[0] + dir[0] * walkDist, pos[1] + dir[1] * walkDist)

print('current pos:', pos)
print('distance to start:', abs(pos[0]) + abs(pos[1]))

print('hq pos:', actualBunnyHeadquarterPos)
print('distance to hq:', abs(actualBunnyHeadquarterPos[0]) + abs(actualBunnyHeadquarterPos[1]))
