#!/usr/bin/python3
from collections import Counter

def shiftLetter(letter, shift):
    if letter is '-':
        return ' '
    zerostart = ord(letter) - ord('a')
    shifted = (zerostart + shift) % (ord('z') - ord('a') + 1)
    return chr(shifted + ord('a'))

# test input
#data = '''aaaaa-bbb-z-y-x-123[abxyz]
#a-b-c-d-e-f-g-h-987[abcde]
#not-a-real-room-404[oarel]
#totally-real-room-200[decoy]'''
#data = 'qzmt-zixmtkozy-ivhz-343[zimth]'

# file input
data = open('input.txt').read()

sectorSum = 0

for line in data.splitlines():
    # Split in interesting parts
    checksum = line[-6:-1]
    sectorID = int(line[-10:-7])
    roomName = line[:-11]

    # Create checksum by using the amazing collections.Counter
    commonLetters = Counter(roomName.replace('-', '')).most_common()
    # So far only sorted by count, not by letter.
    commonLetters.sort(key=lambda t: (-t[1], t[0]))

    # check checksum
    for ckLetter, (letter, _) in zip(checksum, commonLetters):
        if ckLetter is not letter:
            sectorID = 0 # invalidate sector
            break
    sectorSum += sectorID

    # Print out shifted name and sectorID if checksum was valid
    # Print all of them because they are fun to read.
    if sectorID != 0:
        shiftedRoomName = ''.join([shiftLetter(l, sectorID) for l in roomName])
        print("Room name:", shiftedRoomName)
        print("Sector id:", sectorID)


print(sectorSum)