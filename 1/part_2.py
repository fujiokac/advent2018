def get_num_list():
    try:
        with open('input.txt','r') as file:
            return [int(line) for line in file]

    finally:
        file.close()

def find_twice_frequency():
    num_list = get_num_list()
    freqs = {}
    freq = 0
    while(True):
        for num in num_list:
            freq += num
            if freq in freqs:
                return freq
            freqs[freq] = 1

print(find_twice_frequency())