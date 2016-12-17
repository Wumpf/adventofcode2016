#!/usr/bin/python3
from hashlib import md5

# invalid variable name
# pylint: disable=C0103
# Missing function docstring
# pylint: disable=C0111

GOAL = (3, 3)

def is_open(letter):
    return letter >= 'b' and letter <= 'f'

def find(code):
    queue = [(code, (0, 0))]
    nextqueue = []
    while True:

        for bytestring, pos in queue:
            hash = md5(bytestring).hexdigest()

            # Up?
            if pos[1] != 0 and is_open(hash[0]):
                newpos = (pos[0], pos[1] - 1)
                nextqueue.append(((bytestring + b'U'), newpos))

            # Down?
            if pos[1] != 3 and is_open(hash[1]):
                newpos = (pos[0], pos[1] + 1)
                if newpos == GOAL:
                    return (bytestring + b'D')[len(code):]
                nextqueue.append(((bytestring + b'D'), newpos))

            # Left?
            if pos[0] != 0 and is_open(hash[2]):
                newpos = (pos[0] - 1, pos[1])
                nextqueue.append(((bytestring + b'L'), newpos))

            # right?
            if pos[0] != 3 and is_open(hash[3]):
                newpos = (pos[0] + 1, pos[1])
                if newpos == GOAL:
                    return (bytestring + b'R')[len(code):]
                nextqueue.append(((bytestring + b'R'), newpos))
        queue, nextqueue = nextqueue, queue
        nextqueue.clear()


def longestpath(code):
    queue = [(code, (0, 0))]
    nextqueue = []
    maxpathlen = 0
    currentlen = 1

    while len(queue) > 0:
        for bytestring, pos in queue:
            hash = md5(bytestring).hexdigest()

            # Up?
            if pos[1] != 0 and is_open(hash[0]):
                newpos = (pos[0], pos[1] - 1)
                nextqueue.append(((bytestring + b'U'), newpos))

            # Down?
            if pos[1] != 3 and is_open(hash[1]):
                newpos = (pos[0], pos[1] + 1)
                if newpos != GOAL:
                    nextqueue.append(((bytestring + b'D'), newpos))
                elif maxpathlen != currentlen:
                    maxpathlen = currentlen

            # Left?
            if pos[0] != 0 and is_open(hash[2]):
                newpos = (pos[0] - 1, pos[1])
                nextqueue.append(((bytestring + b'L'), newpos))

            # right?
            if pos[0] != 3 and is_open(hash[3]):
                newpos = (pos[0] + 1, pos[1])
                if newpos != GOAL:
                    nextqueue.append(((bytestring + b'R'), newpos))
                elif maxpathlen != currentlen:
                    maxpathlen = currentlen
        queue, nextqueue = nextqueue, queue
        nextqueue.clear()
        currentlen += 1
        print(currentlen)

    return maxpathlen


#print(find('ihgpwlah'.encode()))
#print(find('kglvqrro'.encode()))
#print(find('ulqzkmiv'.encode()))
#print(find('qtetzkpl'.encode()))

# Okay. This is just too slow and takes too much memory I'm running out of ideas here.
# So.. let's just try to do the whole thing in C instead. 
print(longestpath('qtetzkpl'.encode()))


