adaptors = []
with open('input', 'r') as file:
    for l in file.readlines():
        adaptors.append(int(l))

adaptors = sorted(adaptors)

differences = []
for i, x in enumerate(adaptors):
    if i == 0:
        differences.append(x)
    else:
        differences.append(x - adaptors[i-1])
# Add the built in adaptor
differences.append(3)
print(differences)
print(differences.count(1) * differences.count(3))

def collapse(l):
    total = 0
    for i, x in enumerate(l[:-1]):
        y = l[i+1]
        left = l[0:i]
        right = l[i + 2:]
        if x == 1 and y == 1:
            total += collapse(left + [2] + right)
        if x == 2 and y == 1:
            total += collapse(left + [3] + right)
    return total + 1

differences.reverse()
print(collapse(differences))
