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