#!/usr/bin/python3
import numpy as np

# invalid variable name
# pylint: disable=C0103
# lines too long
# pylint: disable=C0301

# Example
start_positions = np.array([4, 1], dtype=np.int)
num_positions = np.array([5, 2], dtype=np.int)

# Puzzle input
# Disc #1 has 13 positions; at time=0, it is at position 10.
# Disc #2 has 17 positions; at time=0, it is at position 15.
# Disc #3 has 19 positions; at time=0, it is at position 17.
# Disc #4 has 7 positions; at time=0, it is at position 1.
# Disc #5 has 5 positions; at time=0, it is at position 0.
# Disc #6 has 3 positions; at time=0, it is at position 1.
# Part 1
#start_positions = np.array([10, 15, 17, 1, 0, 1], dtype=np.int)
#num_positions = np.array([13, 17, 19, 7, 5, 3], dtype=np.int)
# Part 2
#start_positions = np.array([10, 15, 17, 1, 0, 1, 0], dtype=np.int)
#num_positions = np.array([13, 17, 19, 7, 5, 3, 11], dtype=np.int)


num_disks = len(start_positions)
drop_time = 0
while True:
    offsets = np.arange(1 + drop_time, num_disks + 1 + drop_time, dtype=np.int)
    drop_positions = np.remainder(start_positions + offsets, num_positions)
    if np.count_nonzero(drop_positions) == 0:
        break
    drop_time += 1

print(drop_time)
