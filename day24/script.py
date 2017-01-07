#!/usr/bin/python3
from itertools import permutations

# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=W0702

# test input
# data = '''###########
# #0.1.....2#
# #.#######.#
# #4.......3#
# ###########'''
# file input
with open('input.txt', 'r') as f:
    data = f.read()

terrain = [[field for field in line] for line in data.splitlines()]

# get number of locations
positions = {}
for y, row in enumerate(terrain):
    for x, field in enumerate(row):
        try:
            locindex = int(field)
            positions[locindex] = (x, y)
        except:
            pass
print("Finding paths for", positions)

# find shortest routes via depth first
routes = {}
for locindex, startpos in positions.items():
    queue = [startpos]
    newqueue = []
    visited = set()
    num_found = 1
    steps = 0
    while num_found != len(positions) - locindex:
        for pos in queue:
            if pos in visited or terrain[pos[1]][pos[0]] == '#':
                continue

            visited.add(pos)
            try:
                targetlocindex = int(terrain[pos[1]][pos[0]])
                if targetlocindex > locindex:
                    routes[(locindex, targetlocindex)] = steps
                    num_found += 1
            except:
                pass

            # up
            if pos[1] > 0:
                newqueue.append((pos[0], pos[1] - 1))
            # down
            if pos[1] < len(terrain)-1:
                newqueue.append((pos[0], pos[1] + 1))
            # left
            if pos[0] > 0:
                newqueue.append((pos[0]-1, pos[1]))
            # right
            if pos[0] < len(terrain[0])-1:
                newqueue.append((pos[0]+1, pos[1]))

        queue, newqueue = newqueue, queue
        newqueue.clear()
        steps += 1


print("shortest routes:", routes)

# find best combination when starting with 0 by trying all permutations (travling salesman, there is asymptotically no better solution)
bestpathlen = 999999
bestpath = ""
bestpathlen_wret = 999999
for perm in permutations(range(1, len(positions))):
    currentLoc = 0
    pathlen = 0
    for stop in perm:
        pathlen += routes[(min(currentLoc, stop), max(currentLoc, stop))]
        currentLoc = stop
    if pathlen < bestpathlen:
        bestpathlen = pathlen
        bestpath = perm
    pathlen += routes[(0, currentLoc)]
    if pathlen < bestpathlen_wret:
        bestpathlen_wret = pathlen

print("best path is", bestpath, "which is", bestpathlen, "long")
print("best path len with return is", bestpathlen_wret)