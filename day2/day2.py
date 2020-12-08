from collections import Counter
import re

valid = 0
with open("input", 'r') as f:
    for l in f.readlines():
        match = re.match("(\d+)-(\d+) (\w): (\w+)", l)
        if match is not None:
            l = match.group(4)[int(match.group(1))-1] == match.group(3)
            r = match.group(4)[int(match.group(2))-1] == match.group(3)
            if l != r:
                valid += 1
print(valid)