import sys

total = 0
with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        total += int(line) // 3 - 2

print(total)