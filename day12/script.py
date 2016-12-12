#!/usr/bin/python3

# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=W0702

# test input
# data = '''cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a'''
# file input
with open('input.txt', 'r') as f:
    data = f.read()


def run(lines):
    register = {'a':0, 'b':0, 'c':1, 'd':0}
    i = 0
    while i < len(lines):
        current = lines[i]
        instr = current[:3]
        if instr == 'cpy':
            left, target = current[3:].split()
            try:
                value = int(left)
            except:
                value = register[left]
            register[target] = value
        elif instr == 'inc':
            register[current[4]] += 1
        elif instr == 'dec':
            register[current[4]] -= 1
        elif instr == 'jnz':
            condition, offset = current[3:].split()
            try:
                condition_result = (int(condition) != 0)
            except:
                condition_result = (register[condition] != 0)
            if condition_result:
                i += int(offset)
                continue
        else:
            raise ValueError("Unknown instruction", instr)
        i += 1
    return register

print(run(data.splitlines()))
