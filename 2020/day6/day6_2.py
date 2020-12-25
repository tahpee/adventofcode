total = 0
with open("input", 'r') as f:
    for group in f.read().split('\n\n'):
        s = set()
        for i, l in enumerate(group.split('\n')):
            l.strip()
            if i == 0:
                s = set(l)
            s = s.intersection(set(l))
        total = total + len(s)
print(total)
