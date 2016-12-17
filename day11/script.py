#!/usr/bin/python3
from queue import Queue

# invalid variable name
# pylint: disable=C0103
# lines too long
# pylint: disable=C0301
# pylint: disable=C0111
# pylint: disable=W0702


class State:
    def __init__(self):
        self.elevator = 0
        self.chips = None
        self.generators = None
        self._hash = None

    def init_from_example(self):
        self.chips = [0, 0]
        self.generators = [1, 2]

    def init_from_puzzle(self, part2=False):
        # No point in writing a parser.
        # We just manually parse in the style of the example

        #The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
        #The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
        #The third floor contains nothing relevant.
        #The fourth floor contains nothing relevant.
        if part2:
            self.chips = [1, 0, 1, 0, 0, 0, 0]
            self.generators = [0, 0, 0, 0, 0, 0, 0]
        else:
            self.chips = [1, 0, 1, 0, 0]
            self.generators = [0, 0, 0, 0, 0]


    def init_goal_example(self):
        self.elevator = 3
        self.chips = [3, 3]
        self.generators = [3, 3]

    def init_goal_puzzle(self, part2=False):
        self.elevator = 3
        if part2:
            self.chips = [3, 3, 3, 3, 3, 3, 3]
            self.generators = [3, 3, 3, 3, 3, 3, 3]
        else:
            self.chips = [3, 3, 3, 3, 3]
            self.generators = [3, 3, 3, 3, 3]

    def get_stuff_on_floor(self, floor):
        return ([i for i, c in enumerate(self.chips) if c == floor], [i for i, g in enumerate(self.generators) if g == floor])

    def move_elevator(self, target_floor, chipchange, generatorchange):
        newstate = State()
        newstate.elevator = target_floor

        if chipchange != None:
            newstate.chips = self.chips.copy()
            for c in chipchange:
                newstate.chips[c] = target_floor
        else:
            newstate.chips = self.chips

        if generatorchange != None:
            newstate.generators = self.generators.copy()
            for g in generatorchange:
                newstate.generators[g] = target_floor
        else:
            newstate.generators = self.generators

        return newstate

    def pack(self):
        packed = self.elevator
        shift = 2
        for c in self.chips:
            packed ^= c << shift
            shift += 2
        for g in self.generators:
            packed ^= g << shift
            shift += 2
        return packed


def bfs(start, end):
    endpacked = end.pack()
    num_steps = 0
    queue = [start]
    newqueue = []

    visited = {start.pack()}

    # Misuse of an exception as flow control construct.
    # Some people say this is pythonic...
    class Done(Exception):
        pass

    def try_add_state(state, target_floor, chipchange, generatorchange):
        newstate = state.move_elevator(target_floor, chipchange, generatorchange)
        packed = newstate.pack()
        if packed not in visited:
            if packed == endpacked:
                raise Done()
            newqueue.append(newstate)
            visited.add(packed)

    def try_target_floor(state, chips, generators, target_floor, target_floorstuff):
        target_chips, target_generators = target_floorstuff

        # Try moving chips.
        for i, chip in enumerate(chips):
            if chip in target_generators or len(target_generators) == 0:
                try_add_state(state, target_floor, (chip,), None)
                # second chip
                for chip2 in chips[i+1:]:
                    if chip2 in target_generators or len(target_generators) == 0:
                        try_add_state(state, target_floor, (chip, chip2), None)

        # Try moving generators
        unprotected_chips = [chip for chip in target_chips if chip not in target_generators]

        for i, generator in enumerate(generators):
            protectschip = generator in unprotected_chips
            if len(unprotected_chips) == 0 or (len(unprotected_chips) == 1 and protectschip):
                try_add_state(state, target_floor, None, (generator,))
                # generator + fitting chip
                if generator in chips:
                    try_add_state(state, target_floor, (generator, ), (generator, ))
            # Second generator
            for generator2 in generators[i+1:]:
                protectschip2 = generator2 in unprotected_chips
                if len(unprotected_chips) == 0 or \
                  (len(unprotected_chips) == 1 and (protectschip or protectschip2)) or \
                  (len(unprotected_chips) == 2 and  protectschip and protectschip2):
                    try_add_state(state, target_floor, None, (generator, generator2))

    while len(queue) > 0:
        num_steps += 1
        print(num_steps)
        for state in queue:
            chips, generators = state.get_stuff_on_floor(state.elevator)

            try:
                # try moving up
                target_floor = state.elevator + 1
                if target_floor < 4:
                    try_target_floor(state, chips, generators, target_floor, state.get_stuff_on_floor(target_floor))
                # try moving down
                target_floor = state.elevator - 1
                if target_floor >= 0:
                    # No point in moving down if floor below is empty
                    targetfloorstuff = state.get_stuff_on_floor(target_floor)
                    if len(targetfloorstuff[0]) != 0 or len(targetfloorstuff[1]) != 0:
                        try_target_floor(state, chips, generators, target_floor, targetfloorstuff)
            except Done:
                print("num checked states", len(visited))
                return num_steps

        queue, newqueue = newqueue, queue
        newqueue.clear()

    print("num checked states", len(visited))
    return None





goal = State()
#goal.init_goal_example()
goal.init_goal_puzzle(True)

start_state = State()
#start_state.init_from_example()
start_state.init_from_puzzle(True)


#print(State.shortest_path)
import time
before = time.clock()
pathlen = bfs(start_state, goal)
after = time.clock()

print("min path len to goal:", pathlen, "-", after - before, " seconds")
