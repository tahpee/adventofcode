import sys
adaptors = []
with open(sys.argv[1], 'r') as file:
    for l in file.readlines():
        adaptors.append(int(l))


adaptors.append(0)
adaptors.append(max(adaptors)+3)
adaptors.sort()

paths = [0] * (max(adaptors) + 1)
paths[0] = 1

for index in range(1, max(adaptors) + 1):
    for x in range(1, 4):
        if (index - x) in adaptors:
            paths[index] += paths[index - x]
print(paths)
print(paths[-1])

