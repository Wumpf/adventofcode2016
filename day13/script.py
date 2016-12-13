#!/usr/bin/python3

# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=W0702

# test input
# input_number = 10
# startpos = (1, 1)
# goalpos = (7, 4)

# puzzle input
# test input
input_number = 1352
startpos = (1, 1)
goalpos = (31, 39)


def is_wall(pos):
    x, y = pos
    fieldnum = x*x + 3*x + 2*x*y + y + y*y + input_number
    numones = bin(fieldnum).count("1")
    return (numones % 2) != 0

def get_way_length():
    num_steps = 0
    visited = {startpos}
    queue = [startpos]
    newqueue = []
    while True:
        newqueue.clear()
        num_steps += 1
        for pos in queue:
            newpos = [(pos[0], pos[1]+1), (pos[0]+1, pos[1])]
            if pos[0] != 0:
                newpos.append((pos[0]-1, pos[1]))
            if pos[1] != 0:
                newpos.append((pos[0], pos[1]-1))

            for p in newpos:
                if p not in visited and not is_wall(p):
                    if p == goalpos:
                        return num_steps
                    visited.add(p)
                    newqueue.append(p)
        queue, newqueue = newqueue, queue

        # For part 2
        if num_steps == 50:
            print('visisted', len(visited), 'after 50 steps')


# Just for fun
def gen_maze(size):
    maze = [None] * size[1]
    for y in range(size[1]):
        maze[y] = ['.'] * size[0]
        for x in range(size[0]):
            if is_wall((x, y)):
                maze[y][x] = '#'
    return maze


#maze = gen_maze((100,100))
#maze_txt = '\n'.join(''.join(line) for line in maze) 
#print(maze_txt)

print(get_way_length())
