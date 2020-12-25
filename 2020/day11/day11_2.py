import sys

seats = []
with open(sys.argv[1], 'r') as file:
    for l in file.readlines():
        row = []
        for c in l.strip():
            row.append(c)
        seats.append(row)


def neighbor_count(x, y, s):
    count = 0
    directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    # print(x, y)
    for direction in directions:
        nx, ny = x, y
        done = False
        while not done:
            nx = nx + direction[0]
            ny = ny + direction[1]
            if nx < 0 or nx >= len(s[0]) or ny < 0 or ny >= len(s):
                done = True
            else:
                if s[ny][nx] != '.':
                    done = True
                    if s[ny][nx] == '#':
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
            if seat == '#' and neighbor_count(x, y, s) >= 5:
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

print(iterations)
total_occupied = 0
for row in seats:
    total_occupied += row.count('#')
print(total_occupied)