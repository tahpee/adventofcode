import sys

with open(sys.argv[1], 'r') as file:
    timestamp = int(file.readline())
    buses = [int(x) for x in file.readline().strip().split(',') if x != 'x']

modulos = [timestamp % bus_id for bus_id in buses]
next_arrivals = []
for i, bus_id in enumerate(buses):
    next_arrivals.append(bus_id - modulos[i])
print(buses)
print(modulos)
print(next_arrivals)
print(min(next_arrivals))
print(next_arrivals.index(min(next_arrivals)))
next_bus_id = buses[next_arrivals.index(min(next_arrivals))]
print(next_bus_id, min(next_arrivals), next_bus_id * min(next_arrivals))
