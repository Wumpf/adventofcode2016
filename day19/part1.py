#!/usr/bin/python3
import time

# invalid variable name
# pylint: disable=C0103

# Example
#num_elves = 13
# Puzzle input
num_elves = 3018458


happy_elf = 0
step = 1
while num_elves != 1:
    step *= 2
    if num_elves % 2 == 1:
        happy_elf += step
    num_elves = int(num_elves/2)


print(happy_elf + 1)
