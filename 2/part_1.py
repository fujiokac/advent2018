from collections import Counter

def readFile():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def checksum():
    twos = 0
    threes = 0
    for boxId in readFile():
        counts = Counter(boxId).values()
        twos += 2 in counts
        threes += 3 in counts

    return twos * threes

print(checksum())