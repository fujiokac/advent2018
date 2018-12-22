from collections import deque

FILE = 'input.txt'

def parse_as_read():
    polymer = deque('')
    try:
        with open(FILE,'r') as file:
            unit = file.read(1)
            while(unit):
                scan_polymer(polymer, unit)
                unit = file.read(1)
    finally:
        file.close()

    return polymer

def scan_polymer(polymer, unit):
    if len(polymer) > 0 and polymer[-1] == unit.swapcase():
        polymer.pop()
    else:
        polymer.append(unit)

polymer = ''.join(parse_as_read())
print(len(polymer))