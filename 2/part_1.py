from collections import Counter

def read_file():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def checksum(file):
    twos = 0
    threes = 0
    for id in file:
        counts = Counter(id).values()
        twos += 2 in counts
        threes += 3 in counts

    return twos * threes

print(checksum(read_file()))