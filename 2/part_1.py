def readFile():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def parseId(boxId):
    dct = {}
    for letter in boxId:
        if letter in dct:
            dct[letter] += 1
        else:
            dct[letter] = 1
    return dct

def containsNum(parsedId, num):
    for letter in parsedId:
        if parsedId[letter] == num:
            return True
    return False

def checksum():
    twos = 0
    threes = 0
    parsedIds = [parseId(boxId) for boxId in readFile()]
    for pid in parsedIds:
        if containsNum(pid, 2):
            twos += 1
        if containsNum(pid, 3):
            threes += 1
    return twos * threes

print(checksum())