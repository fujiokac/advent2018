from statistics import mode
from collections import Counter
import re

MINUTE = re.compile(r':(\d{2})\]')
GUARD = re.compile(r'#(\d+)')
TOTAL = 'total'
MINUTES = 'minutes'

def read_file():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def parse_log(log):
    guards = {}
    for line in sorted(log):
        minute = int(MINUTE.search(line).group(1))
        if 'Guard' in line:
            id = int(GUARD.search(line).group(1))
        elif 'asleep' in line:
            asleep = minute
        elif 'wakes' in line:
            awake = minute
            if id not in guards:
                guards[id] = {}
                guards[id][TOTAL] = 0
                guards[id][MINUTES] = []
            guards[id][TOTAL] += awake - asleep
            guards[id][MINUTES].extend(range(asleep,awake))
    return guards

def sleepiest_guard(guards):
    return max(guards, key=lambda key: guards[key][TOTAL])

def strategy_1(id, minutes):
    return id * Counter(minutes).most_common(1)[0][0]

def strategy_2(guards):
    id = max(guards, key=lambda key: Counter(guards[key][MINUTES]).most_common(1)[0][1])
    minute = Counter(guards[id][MINUTES]).most_common(1)[0][0]
    return id, minute


guards = parse_log(sorted(read_file()))
id = sleepiest_guard(guards)
print("strategy 1 -- id:{} total:{} answer:{}".format(id, guards[id][TOTAL], strategy_1(id, guards[id][MINUTES])))
id, minute = strategy_2(guards)
print("strategy 2 -- id:{} minute:{} answer:{}".format(id, minute, id * minute))
