#!/usr/bin/python3

# invalid variable name
# pylint: disable=C0103
# Missing function docstring
# pylint: disable=C0111
# Line too long
# pylint: disable=C0301

# Example
# data = """swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d"""
# password = list('abcde')

# puzzle input
with open('input.txt', 'rt') as f:
   data = f.read()
password = list('abcdefgh')

def execute_command(password, command, reverse):
    parts = command.split()
    if parts[0] == 'swap':
        if parts[1] == 'position':
            pos0 = int(parts[2])
            pos1 = int(parts[-1])
            if reverse:
                pos0, pos1 = pos1, pos0
            password[pos1], password[pos0] = password[pos0], password[pos1]
        else: # letter
            letter0 = parts[2]
            letter1 = parts[-1]
            if reverse:
                letter0, letter1 = letter1, letter0
            for i, l in enumerate(password):
                if l == letter0:
                    l = letter1
                elif l == letter1:
                    l = letter0
                password[i] = l
    elif parts[0] == 'reverse':
        pos0 = int(parts[2])
        pos1 = int(parts[-1]) + 1
        password[pos0:pos1] = reversed(password[pos0:pos1])
    elif parts[0] == 'rotate':
        if parts[-1] == 'step' or parts[-1] == 'steps':
            num = int(parts[2])
            left = parts[1] == 'left'
        else:
            letter = parts[-1]
            num = password.index(letter)
            if num >= 4:
                num += 1
            num += 1
            left = False

        if reverse:
            left = not left

        if reverse and parts[-2] == 'letter':
            poslettercurrent = password.index(letter)
            hypothetical_start = 0
            while True:
                hypothetical_shiftnum = hypothetical_start
                if hypothetical_shiftnum >= 4:
                    hypothetical_shiftnum += 1
                hypothetical_shiftnum += 1

                if (hypothetical_shiftnum + hypothetical_start) % len(password) == poslettercurrent:
                    num = hypothetical_shiftnum
                    break

                hypothetical_start += 1

        num %= len(password)
        if left:
            password[:] = password[num:] + password[:num]
        else:
            password[:] = password[-num:] + password[:-num]
    elif parts[0] == 'move':
        pos0 = int(parts[2])
        pos1 = int(parts[-1])

        if reverse:
            pos0, pos1 = pos1, pos0

        letter0 = password[pos0]
        password.pop(pos0)
        password.insert(pos1, letter0)
    else:
        raise Exception("Unknown command")



# Forward
passlist = []
passlist2 = []

#passlist.append(password.copy())
for command in data.splitlines():
    execute_command(password, command, False)
    #passlist.append(password.copy())
print(''.join(password))

#passlist2.append(password.copy())
for command in reversed(data.splitlines()):
    execute_command(password, command, True)
    #passlist2.append(password.copy())
print(''.join(password))

# passlist2 = reversed(passlist2)
# print([''.join(b) for b in passlist2])
# print([a==b for a,b in zip(passlist, passlist2)])
# print([''.join(a) for a in passlist])
# print()


# Reverse
password = list('fbgdceah')
for command in reversed(data.splitlines()):
    execute_command(password, command, True)
print(''.join(password))
