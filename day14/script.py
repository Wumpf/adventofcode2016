#!/usr/bin/python3
from hashlib import md5

# invalid variable name
# pylint: disable=C0103
# lines too long
# pylint: disable=C0301

#salt = 'abc'
salt = 'ihaygndm'

def has_same_char_seq(hash, num):
    prev_letter = None
    times_in_row = 1
    for l in hash:
        if l == prev_letter:
            times_in_row += 1
            if times_in_row == num:
                return prev_letter
        else:
            prev_letter = l
            times_in_row = 1
    return None

def has_specific_char_seq(hash, num, letter):
    times_in_row = 0
    for l in hash:
        if l == letter:
            times_in_row += 1
            if times_in_row == num:
                return True
        else:
            times_in_row = 0
    return False


def keygen(stretchcount = 1):
    idx = 0
    checkingkeys = {} # keys currently be checked
    realkeys = []
    MAX_INDEX_START = 99999999
    maxindex = MAX_INDEX_START

    while idx < maxindex:
        md5string = salt + str(idx)
        for _ in range(stretchcount + 1):
            md5string = md5(md5string.encode()).hexdigest()

        # remove now invalid checkingkeys
        try:
            checkingkeys.pop(idx - 1000)
        except:
            pass

        # relevant for checkingkeys?
        newrealkeys = []
        for checkidx, letter in checkingkeys.items():
            if has_specific_char_seq(md5string, 5, letter):
                newrealkeys.append(checkidx)
                realkeys.append(checkidx)
                # shutdown phase?
                if len(realkeys) >= 64 and maxindex == MAX_INDEX_START:
                    maxindex = idx + 1000
                    print("shutting down key search ...")
        for remidx in newrealkeys:
            checkingkeys.pop(remidx)

        # key candidate?
        letter = has_same_char_seq(md5string, 3)
        if letter is not None:
            checkingkeys[idx] = letter
        idx += 1
    return realkeys


#keys = keygen()
keys = keygen(2016)
keys = sorted(keys)
print(keys)
print(keys[63])