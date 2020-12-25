import sys
import copy

seats = []
with open(sys.argv[1], 'r') as file:
    for l in file.readlines():
        row = []
        for c in l.strip():
            row.append(c)
        seats.append(row)


def neighbor_count(x, y, s):
    count = 0
    upper = max(0, y-1)
    lower = min(len(s), y+2)
    left = max(0, x-1)
    right = min(len(s[0]), x+2)
    # print(x, y, upper, lower, left, right)
    for i in range(upper, lower):
        for j in range(left, right):
            # print('\t', i, j)
            if i == y and j == x:
                continue
            if s[i][j] == '#':
                count += 1
    return count


def update(s):
    new_s = []
    for y, row in enumerate(s):
        new_row = []
        for x, seat in enumerate(row):
            new_seat = seat
            if seat == 'L' and neighbor_count(x, y, s) == 0:
                new_seat = '#'
            if seat == '#' and neighbor_count(x, y, s) >= 4:
                new_seat = 'L'
            new_row.append(new_seat)
        new_s.append(new_row)
    return new_s

iterations = 0
running = True
while running:
    new_seats = update(seats)
    if new_seats == seats:
        running = False
    else:
        iterations += 1
        seats = new_seats
        for row in seats:
            print(''.join(row))
        print('')
    #a = input("")
print(iterations)

total_occupied = 0
for row in seats:
    total_occupied += row.count('#')
print(total_occupied)