from statistics import mode
import re

MINUTE = re.compile(r':(\d{2})\]')
GUARD = re.compile(r'#(\d+)')

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
                guards[id]['total'] = 0
                guards[id]['minutes'] = []
            guards[id]['total'] += awake - asleep
            guards[id]['minutes'].extend(range(asleep,awake))
    return guards

def sleepiest_guard(guards):
    return max(guards, key=lambda key: guards[key]['total'])

def strategy_1(id, minutes):
    return id * mode(minutes)

guards = parse_log(sorted(read_file()))
id = sleepiest_guard(guards)
print(id, guards[id]['total'], strategy_1(id, guards[id]['minutes']))