total = 0
with open("input", 'r') as f:
    for group in f.read().split('\n\n'):
        print(group)
        s = set()
        for l in group.split('\n'):
            l.strip()
            s = s.union(set(l))
        total = total + len(s)
print(total)
