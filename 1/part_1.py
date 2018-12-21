def sumLines():
    try:
        with open('input.txt','r') as file:
            return sum([int(line) for line in file])
    finally:
        file.close()

print(sumLines())