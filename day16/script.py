#!/usr/bin/python3
from bitarray import bitarray

# invalid variable name
# pylint: disable=C0103
# Missing function docstring
# pylint: disable=C0111

# Example
#data = bitarray('1')
#data = bitarray('0')
#data = bitarray('111100001010')
#data = bitarray('10000')
#targetlen = 20

# Puzzle input
data = bitarray('11110010111001001')
#targetlen = 272
targetlen = 35651584

def gen_iteration(a):
    b = a.copy()
    b.reverse()
    a.append(False)
    for bit in b:
        a.append(not bit)

def gen(bits):
    while len(bits) < targetlen:
        gen_iteration(bits)
        #print(bits.to01())

def chk(bits):
    while len(bits) % 2 == 0:
        chksum = bitarray()
        for b0, b1 in zip(bits[::2], bits[1::2]):
            chksum.append(b0 == b1)
        bits = chksum
    return chksum


gen(data)
check = chk(data[:targetlen])
print(check.to01())

