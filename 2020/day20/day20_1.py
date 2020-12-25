import sys
import re
import numpy as np

class Tile(object):
    def __init__(self, tile_id, arr):
        self.tile_id = tile_id
        self.arr = arr


tiles = {}
with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        line = line.strip()
        match = re.match(r'Tile (\d+):', line)
        if match:
            tile_id = int(match.group(1))
            tiles.setdefault(tile_id, np.zeros(shape=(10, 10), dtype=np.uin))
            row = 0
        match = re.match(r'([\.#]+)', line)
        if match:
            print(tile_id)
            print(tiles[tile_id])
            print(match.group(1))
            for i, c in enumerate(match.group(1)):
                tiles[tile_id][row][i] = 0 if c == '.' else 1
            row += 1

for tile in tiles:


print(tiles)