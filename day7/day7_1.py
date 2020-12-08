import re

tree = {}

def travel(bag):
    s = set()
    for color in tree:
        if bag in tree[color]:
            s.add(color)
            s = s.union(travel(color))
    return s

with open("input", 'r') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        match = re.match(r'^(\w+ \w+) bags contain (.*)', l)
        if match:
            tree.setdefault(match.group(1), {})
            for part in match.group(2).split(','):
                inner_match = re.match(r'\s*(\d+) (\w+ \w+) bags?', part)
                if inner_match:
                    tree[match.group(1)][inner_match.group(2)] = inner_match.group(1)

print(len(travel('shiny gold')))