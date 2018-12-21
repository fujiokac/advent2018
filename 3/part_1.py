import collections
import re

REGEX = re.compile(r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)')

def readFile():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def markCloth(cloth, claim):
    left = int(claim.group(2))
    top = int(claim.group(3))
    right = left + int(claim.group(4))
    bottom = top + int(claim.group(5))

    marked = 0
    for row in range(top,bottom):
        for col in range(left,right):
            if (col,row) in cloth:
                # Cell claimed before
                if cloth[col,row]:
                    # Count only once
                    marked += 1
                    cloth[col,row] = False
            else:
                cloth[col,row] = True
    return marked

def processClaims(claims):
    cloth = {}
    overlap = 0
    for line in claims:
        claim = REGEX.search(line)
        if claim:
            overlap += markCloth(cloth, claim)
    return overlap


print(processClaims(readFile()))
