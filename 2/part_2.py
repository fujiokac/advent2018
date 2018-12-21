import itertools as it

def readFile():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def pairwise(iterable):
    #itertools recipe
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)

def diffExpected(id1, id2, expected = 1):
    diff = 0
    for a, b in zip(id1, id2):
        if a != b:
            if diff < expected:
                diff += 1
            else:
                return False
    return diff == expected

def commonLetters(id1, id2):
    return ''.join([a for a, b in zip(id1, id2) if a == b])

def findCommonId():
    ids = readFile()
    for id1, id2 in pairwise(sorted(ids)):
        if diffExpected(id1, id2):
            return commonLetters(id1, id2)
    return None

print(findCommonId())