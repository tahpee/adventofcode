import sys
import re
import math

def rotate_point(point, direction):
    direction = math.radians(direction)
    x = point[0] * math.cos(direction) - point[1] * math.sin(direction)
    y = point[1] * math.cos(direction) + point[0] * math.sin(direction)
    return [x, y]


waypoint = [10, 1]
position = [0, 0]
with open(sys.argv[1], 'r') as file:
    for l in file.readlines():
        match = re.match(r'^([RLNSEWF])(\d+)$', l)
        if match:
            command = match.group(1)
            value = int(match.group(2))
            print(l.strip())
            if command == 'N':
                waypoint[1] += value
            if command == 'S':
                waypoint[1] -= value
            if command == 'E':
                waypoint[0] += value
            if command == 'W':
                waypoint[0] -= value
            if command == 'F':
                position = [waypoint[0] * value + position[0], waypoint[1] * value + position[1]]
            if command == 'L':
                assert value % 90 == 0, "non cartesian rotation"
                waypoint = rotate_point(waypoint, value)
            if command == 'R':
                assert value % 90 == 0, "non cartesian rotation"
                waypoint = rotate_point(waypoint, value * -1)
        print(position, waypoint)
print(abs(position[0]) + abs(position[1]))