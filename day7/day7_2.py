import re

tree = {}

def travel(bag, level=0):
    total = 0
    for innerbag in tree[bag]:
        total += tree[bag][innerbag] + tree[bag][innerbag] * travel(innerbag, level+1)
    return total

with open("input", 'r') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        match = re.match(r'^(\w+ \w+) bags contain (.*)', l)
        if match:
            tree.setdefault(match.group(1), {})
            for part in match.group(2).split(','):
                inner_match = re.match(r'\s*(\d+) (\w+ \w+) bags?', part)
                if inner_match:
                    tree[match.group(1)][inner_match.group(2)] = int(inner_match.group(1))

print(travel('shiny gold'))