#!/usr/bin/python3

# test
# data = 'ADVENT'
# data = 'A(1x5)BC'
# data = '(3x3)XYZ'
# data = 'A(2x2)BCD(2x2)EFG'
# data = 'X(8x2)(3x3)ABCY'
data = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

# file input
with open('input.txt', 'rt') as f:
    data = f.read()

def decompress(data, version2 = True):
    uncompr_len = 0
    i = 0
    while i < len(data):
        next_paranthesis_open = data.find('(', i)
        if next_paranthesis_open == -1:
            uncompr_len += len(data) - i
            break
        else:
            uncompr_len += next_paranthesis_open - i
            next_paranthesis_close = data.find(')', next_paranthesis_open) # assume there is one
            instructions = data[next_paranthesis_open+1 : next_paranthesis_close].split('x')
            numchars = int(instructions[0])
            times = int(instructions[1])
            i = next_paranthesis_close + 1 + numchars

            string_to_be_repeated = data[next_paranthesis_close + 1 : i]
            if version2:
                uncompr_len_inner = decompress(string_to_be_repeated, True)
                uncompr_len += uncompr_len_inner * times
            else:
                uncompr_len += len(string_to_be_repeated) * times
    return uncompr_len


print(decompress(data))