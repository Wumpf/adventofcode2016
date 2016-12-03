#!/usr/bin/python3

# file input
data = open('input.txt').read()
numbers = [[int(n) for n in tri.split()] for tri in data.splitlines()]

def isTri(a, b, c):
    return a + b > c and \
           b + c > a and \
           a + c > b

numTris = len([tri for tri in numbers if isTri(tri[0], tri[1], tri[2])])
print("part one:", numTris)

numTris = 0
for column in range(len(numbers[0])):
    for row in range(0, len(numbers), 3):
        if isTri(numbers[row][column], numbers[row+1][column], numbers[row+2][column]):
            numTris += 1
print("part two:", numTris)
