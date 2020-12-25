import math

trees = []
with open("input", 'r') as f:
    for i, l in enumerate(f.readlines()):
        # l.strip()
        trees.append([])
        for c in l:
            trees[i].append(c == "#")
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
# slopes = [[1, 1], [3, 1]]
# slopes = [[3, 1]]
tree_count = []
width = len(trees[0]) - 1
for i, slope in enumerate(slopes):
    column = 0
    right, down = slope
    print(slope)
    tree_count.append(0)
    print(tree_count)
    for row in range(0, len(trees), down):
        # print(row+1, column+1, column % width + 1, "Tree" if trees[row][column % width] else "")
        if trees[row][column % width]:
            tree_count[i] += 1
        column = column + right
print(tree_count)
print(math.prod(tree_count))
