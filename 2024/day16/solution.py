with open('input.txt') as f:
    data = f.read()

example = """\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############\
"""

# Part 1: 7036
# Part 2: 45
# data = example

ans1 = 0
ans2 = 0

grid = {(i + j * 1j): c for i, r in enumerate(data.splitlines()) for j, c in enumerate(r)}

for p, c in grid.items():
    if c == 'S':
        start = p
    elif c == 'E':
        end = p


def insert_by_score(queue, item):
    i, j = 0, len(queue) - 1

    while i <= j:
        m = (i + j) // 2
        if queue[m][2] < item[2]:
            i = m + 1
        else:
            j = m - 1
    queue.insert(i, item)


queue = [(start, 1j, 0, [start])]
scores = {}
min_score = float('inf')
tiles = set()

while queue:
    pos, direc, score, path = queue.pop(0)

    if (pos, direc) in scores and scores[(pos, direc)] < score:
        continue

    scores[(pos, direc)] = score

    if pos == end:
        if score <= min_score:
            min_score = score
            tiles.update(path)
        continue

    for r, pts in [(1, 1), (+1j, 1001), (-1j, 1001)]:
        new_pos = pos + r * direc
        if new_pos in grid and grid[new_pos] != '#':
            # queue.append((new_pos, r * direc, score + pts, path + [new_pos]))
            insert_by_score(queue, (new_pos, r * direc, score + pts, path + [new_pos]))


ans1 = min_score
ans2 = len(tiles)

# with open('output.txt', 'w') as f:
#     n = max(p.imag for p in grid)
#     output = []

#     for p in grid:
#         output.append('O' if p in tiles else grid[p])
#         if p.imag == n:
#             output.append('\n')

#     f.write(''.join(output))


print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
