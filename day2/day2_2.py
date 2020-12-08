from collections import Counter
import re

valid = 0
with open("input", 'r') as f:
    for l in f.readlines():
        match = re.match("(\d+)-(\d+) (\w): (\w+)", l)
        if match is not None:
            counts = Counter(match.group(4))
            if match.group(3) in counts and int(match.group(1)) <= counts[match.group(3)] <= int(match.group(2)):
                valid += 1
print(valid)