import sys
import re

def cartesian_move(x, y, direction, distance):
    if direction == 90:
        x += distance
    if direction == 270:
        x -= distance
    if direction == 0:
        y += distance
    if direction == 180:
        y -= distance
    return x, y

x = 0
y = 0
direction = 90
with open(sys.argv[1], 'r') as file:
    for l in file.readlines():
        match = re.match(r'^([RLNSEWF])(\d+)$', l)
        if match:
            command = match.group(1)
            value = int(match.group(2))
            print(l.strip())
            if command == 'N':
                y += value
            if command == 'S':
                y -= value
            if command == 'E':
                x += value
            if command == 'W':
                x -= value
            if command == 'F':
                x, y = cartesian_move(x, y, direction, value)
            if command == 'L':
                assert value % 90 == 0, "non cartesian rotation"
                direction = (direction - value) % 360
            if command == 'R':
                assert value % 90 == 0, "non cartesian rotation"
                direction = (direction + value) % 360
        print(x, y, direction)
print(abs(x) + abs(y))