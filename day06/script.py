#!/usr/bin/python3
from collections import Counter

# test input
data = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''
# file input
with open('input.txt', 'r') as f:
    data = f.read()

lines = data.splitlines()
columns = [[line[c] for line in lines] for c in range(len(lines[0]))]

message1 = ''.join([Counter(c).most_common(1)[0][0] for c in columns])
print(message1)
message1 = ''.join([Counter(c).most_common()[-1][0] for c in columns])
print(message1)