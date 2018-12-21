def getNumList():
    try:
        with open('input.txt','r') as file:
            return [int(line) for line in file]

    finally:
        file.close()

def findTwiceFrequency():
    numList = getNumList()
    freqs = {}
    freq = 0
    while(True):
        for num in numList:
            freq += num
            if freq in freqs:
                return freq
            freqs[freq] = 1

print(findTwiceFrequency())