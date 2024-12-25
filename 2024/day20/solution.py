with open('input.txt') as f:
    data = f.read()

example = """\
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############\
"""

# Part 1:
# Part 2:
# data = example

ans1 = 0
ans2 = 0

grid = {(i + j * 1j): c for i, r in enumerate(data.splitlines()) for j, c in enumerate(r)}

for p, c in grid.items():
    if c == 'S':
        start = p
    elif c == 'E':
        end = p


def count_path(grid, start):
    queue = [start]
    dists = {start: 0}

    while queue:
        pos = queue.pop(0)

        for d in [1, -1, 1j, -1j]:
            np = pos + d
            if np in grid and grid[np] != '#' and np not in dists:
                dists[np] = dists[pos] + 1
                queue.append(np)

    return dists


def solve(n, t=100):
    start_dists = count_path(grid, start)
    end_dists = count_path(grid, end)
    regular_time = start_dists[end]
    count = 0

    moves = [(di, dj) for di in range(-n, n + 1) for dj in range(-(n - abs(di)), n - abs(di) + 1)]

    for ps in start_dists:
        for di, dj in moves:
            pe = ps + di + dj * 1j
            if pe in end_dists:
                saving = regular_time - (start_dists[ps] + abs(di) + abs(dj) + end_dists[pe])
                if saving >= t:
                    count += 1

    return count


ans1 = solve(2)
ans2 = solve(20)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
