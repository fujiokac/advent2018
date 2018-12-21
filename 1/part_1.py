def sum_lines():
    try:
        with open('input.txt','r') as file:
            return sum([int(line) for line in file])
    finally:
        file.close()

print(sum_lines())