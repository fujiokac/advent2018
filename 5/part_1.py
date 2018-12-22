from collections import deque
import string

FILE = 'input.txt'

def read_file():
    try:
        with open(FILE,'r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def react_polymer(raw):
    polymer = deque('')
    for unit in raw:
        scan(polymer, unit)

    return ''.join(polymer)

def scan(polymer, unit):
    if len(polymer) > 0 and polymer[-1] == unit.swapcase():
        polymer.pop()
    else:
        polymer.append(unit)

print(len(react_polymer(read_file()[0])))