from collections import defaultdict
import re

REGEX = re.compile(r'\d+')

def read_file():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def mark_cloth(cloth, id, left, top, width, height):
    right = left + width
    bottom = top + height

    for row in range(top, bottom):
        for col in range(left, right):
            cloth[(row,col)].add(id)

def process_claims(claims):
    good_ids = set()
    bad_ids = set()
    cloth = defaultdict(set)
    for line in claims:
        id, left, top, width, height = map(int,REGEX.findall(line))
        mark_cloth(cloth, id, left, top, width, height)
    for ids in cloth.values():
        good_ids |= ids
        if len(ids) > 1:
            bad_ids |= ids
    return good_ids.difference(bad_ids)


print(process_claims(read_file()))