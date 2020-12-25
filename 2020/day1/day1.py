s = set()
with open("input", 'r') as f:
    for l in f.readlines():
        s.add(int(l))

for n in s:
    for m in (s - set([n])):
    	if (2020 - n - m) in s:
        	print(n * m * (2020 - (n + m)))

