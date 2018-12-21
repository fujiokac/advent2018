import re

REGEX = re.compile(r'\d+')

def read_file():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def mark_cloth(cloth, left, top, width, height):
    right = left + width
    bottom = top + height

    count = 0
    for row in range(top, bottom):
        for col in range(left, right):
            if (row,col) not in cloth:
                cloth[(row,col)] = True
            elif cloth[(row,col)]:
                count += 1
                cloth[(row,col)] = False
    return count

def process_claims(claims):
    cloth = {}
    total = 0
    for line in claims:
        id, left, top, width, height = map(int,REGEX.findall(line))
        total += mark_cloth(cloth, left, top, width, height)
    return total


print(process_claims(read_file()))