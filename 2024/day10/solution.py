with open('input.txt') as f:
    data = f.read()

example = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732\
"""

# Part 1: 36
# Part 2: 81
# data = example

ans1 = 0
ans2 = 0

map = {(i, j): int(c) for i, line in enumerate(data.splitlines()) for j, c in enumerate(line)}
direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
neighbors = {(i, j): {(i + di, j + dj) for di, dj in direc if (i + di, j + dj) in map} for i, j in map}


def find_paths(map, neighbors, start):
    paths = []
    if map[start] == 9:
        return [start]

    for neighbor in neighbors[start]:
        if map[neighbor] == map[start] + 1:
            paths.extend(find_paths(map, neighbors, neighbor))
    return paths


for s in map:
    if map[s] == 0:
        paths = find_paths(map, neighbors, s)
        ans1 += len(set(paths))
        ans2 += len(paths)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')