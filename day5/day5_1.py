def seat_to_bcd(seat):
    row = 0
    col = 0
    for i, c in enumerate(seat[0:7]):
        row = row | (1 if c == 'B' else 0) << (6 - i)
    for i, c in enumerate(seat[7:]):
        col = col | (1 if c == 'R' else 0) << (2 - i)
    seat_id = row * 8 + col
    return row, col, seat_id

max_id = 0
with open("input", 'r') as f:
    for i, l in enumerate(f.readlines()):
        col, row, seat_id = seat_to_bcd(l.strip())
        max_id = max(max_id, seat_id)
print(max_id)