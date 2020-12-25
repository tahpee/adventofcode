numbers = []
with open('input', 'r') as file:
    for l in file.readlines():
        numbers.append(int(l))

def find_pair(slice, target):
    for i, x in enumerate(slice):
        for y in slice[i+1:]:
            if x + y == target:
                return True
    return False


def find_sequence(slice, target):
    for i, x in enumerate(slice):
        for j, y in enumerate(slice[i+1:]):
            total = sum(slice[i:j])
            if total == target:
                return min(slice[i:j]) + max(slice[i:j])
            if total > target:
                break
    return False

window = 25
for i, n in enumerate(numbers[window:], window):
    left = i - window
    right = i - 1
    if not find_pair(numbers[left:right+1], numbers[i]):
        print(n)
        break
target = n

for i, n in enumerate(numbers[window:], window):
    left = i - window
    right = i - 1
    weakness = find_sequence(numbers[left:right+1], target)
    if weakness is not False:
        print(weakness)
        break