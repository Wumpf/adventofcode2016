#!/usr/bin/python3

# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=W0702

# test input
# data = '''cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a'''
# file input
with open('input_mul.txt', 'r') as f:
    data = f.read()


def run(lines):
    register = {'a':12, 'b':0, 'c':0, 'd':0}
    i = 0
    while i < len(lines):
        current = lines[i]
        instr = current[0]

        if len(current) == 3:
            try:
                arg1val = int(current[2])
                arg1reg = None
            except:
                arg1val = register[current[2]]
                arg1reg = current[2]

        if len(current) > 1:
            try:
                arg0val = int(current[1])
                arg0reg = None
            except:
                arg0val = register[current[1]]
                arg0reg = current[1]

        try:
            if instr == 'cpy' and arg1reg is not None:
                register[arg1reg] = arg0val
            elif instr == 'inc' and arg0reg is not None:
                register[arg0reg] += 1
            elif instr == 'dec' and arg0reg is not None:
                register[arg0reg] -= 1
            elif instr == 'jnz':
                condition_result = arg0val != 0
                if condition_result:
                    i += arg1val
                    continue
            elif instr == 'tgl':
                targetline = lines[i + arg0val]
                if len(targetline) == 2:
                    if targetline[0] == 'inc':
                        targetline[0] = 'dec'
                    else:
                        targetline[0] = 'inc'
                else:
                    if targetline[0] == 'jnz':
                        targetline[0] = 'cpy'
                    else:
                        targetline[0] = 'jnz'
            elif instr == 'nop':
                pass
            elif instr == 'mul':
                register[arg0reg] = register[arg1reg] * register[current[3]]

            else:
                raise ValueError("Unknown instruction", instr)
        except:
            pass # skip everything that didn't work
        i += 1
    return register


registerstate = run([[arg for arg in line.split()] for line in data.splitlines()])
print(registerstate)
