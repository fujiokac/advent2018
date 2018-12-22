from collections import deque, Counter
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

def minify(polymer, unit):
    return react_polymer(polymer.replace(unit,'').replace(unit.swapcase(), ''))

def analyze(polymer):
    units = set(polymer.lower())
    return min([len(minify(polymer, unit)) for unit in units])

polymer = react_polymer(read_file()[0])
print(len(polymer))
print(analyze(polymer))