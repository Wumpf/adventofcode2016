#!/usr/bin/python3
from hashlib import md5

#doorId = 'abc'
doorId = 'uqwqemis'

PASS_LEN = 8
passwordP1 = ''
passwordP2 = ['_'] * PASS_LEN

i = 0
while any([c == '_' for c in passwordP2]):
    md5string = md5((doorId +str(i)).encode()).hexdigest()
    i += 1
    if md5string.startswith('00000'):
        if len(passwordP1) != PASS_LEN:
            passwordP1 += md5string[5]

        try:
            pos = int(md5string[5])
        except:
            continue
        if pos < PASS_LEN and passwordP2[pos] == '_':
            passwordP2[pos] = md5string[6]
            print(passwordP2)


print("part one:", passwordP1)
print("part two:", ''.join(passwordP2))
