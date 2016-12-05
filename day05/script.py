#!/usr/bin/python3
from hashlib import md5

#doorId = 'abc'
doorId = 'uqwqemis'

PASS_LEN = 8
password = ''

i = 0
while len(password) != PASS_LEN:
    md5string = md5((doorId +str(i)).encode()).hexdigest()
    i += 1
    if md5string.startswith('00000'):
        password += md5string[5]
        print(password)
