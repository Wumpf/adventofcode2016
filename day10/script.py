#!/usr/bin/python3

# test
# data = '''value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2'''
# values_of_interest = (2, 5)

# file input
with open('input.txt', 'rt') as f:
    data = f.read()
values_of_interest = (17, 61)


class BotList:
    bots = {}

    def get(self, target_name):
        if target_name not in self.bots:
            self.bots[target_name] = Bot(target_name)
        return self.bots[target_name]


class Bot:
    bot_list = BotList()

    def __init__(self, name):
        self.chips = []
        self.name = name
        self.target_low = None
        self.target_high = None

    def set_targets(self, target_low, target_high):
        self.target_low = target_low
        self.target_high = target_high
        self.try_to_pass_on()

    def give(self, value):
        self.chips.append(value)
        self.try_to_pass_on()

    def try_to_pass_on(self):
        if len(self.chips) == 2 and self.target_low != None and self.target_high != None:
            low = min(self.chips)
            high = max(self.chips)
            self.chips.clear()

            #print('comparing', low, high)

            if values_of_interest[0] == low and values_of_interest[1] == high:
                print(self.name)

            low_bot = self.bot_list.get(self.target_low).give(low)
            high_bot = self.bot_list.get(self.target_high).give(high)

# extract instruction and "value x goes to" (inits)

for instr in data.splitlines():
    parts = instr.split()
    if 'goes to bot' in instr:
        value = int(parts[1])
        bot = Bot.bot_list.get(' '.join([parts[-2], parts[-1]]))
        bot.give(value)
    else:
        origin = ' '.join([parts[0], parts[1]])
        target_low = ' '.join([parts[5], parts[6]])
        target_high = ' '.join([parts[-2], parts[-1]])
        bot = Bot.bot_list.get(origin)
        bot.set_targets(target_low, target_high)

#print('\n'.join(['{} {}'.format(bot.name, bot.chips) for key, bot in Bot.bot_list.bots.items()]))
print(Bot.bot_list.bots['output 0'].chips)
print(Bot.bot_list.bots['output 1'].chips)
print(Bot.bot_list.bots['output 2'].chips)