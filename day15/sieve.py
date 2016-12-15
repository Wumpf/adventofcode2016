#!/usr/bin/python3

# invalid variable name
# pylint: disable=C0103
# lines too long
# pylint: disable=C0301

# Example
#start_positions = [4, 1]
#num_positions = [5, 2]

# Puzzle input
# Disc #1 has 13 positions; at time=0, it is at position 10.
# Disc #2 has 17 positions; at time=0, it is at position 15.
# Disc #3 has 19 positions; at time=0, it is at position 17.
# Disc #4 has 7 positions; at time=0, it is at position 1.
# Disc #5 has 5 positions; at time=0, it is at position 0.
# Disc #6 has 3 positions; at time=0, it is at position 1.
# Part 1
#start_positions = [10, 15, 17, 1, 0, 1]
#num_positions = [13, 17, 19, 7, 5, 3]
# Part 2
start_positions = [10, 15, 17, 1, 0, 1, 0]
num_positions = [13, 17, 19, 7, 5, 3, 11]   # prime numbers :)


num_disks = len(start_positions)
drop_time = 1
cyclelen = 1

for discidx, (start, num) in enumerate(zip(start_positions, num_positions)):
    # find new drop time
    while True:
        # we droped at drop_time since then discidx+1 time has passed and the disc started at start, where is it now?
        pos = (drop_time + start + discidx + 1) % num
        if pos == 0:
            break
        drop_time += cyclelen
    # new cycle time
    cyclelen *= num # this would be wrong if there were two identical discs (identical start and identical number of positions)

print(drop_time)
