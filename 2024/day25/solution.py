with open('input.txt') as f:
    data = f.read()

example = """\
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####\
"""

# Part 1: 3
# Part 2:
# data = example

ans1 = 0
ans2 = 0

data = data.split('\n\n')
locks = []
keys = []


def count_pins(grid):
    return [sum(row[i] == '#' for row in grid) for i in range(len(grid[0]))]


for grid in data:
    lines = grid.split('\n')
    pins = lines[1:-1]
    heights = count_pins(pins)

    if '#' in lines[0]:
        locks.append(heights)
    else:
        keys.append(heights)

for lock in locks:
    for key in keys:
        if all(lock[i] + key[i] <= 5 for i in range(5)):
            ans1 += 1

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
