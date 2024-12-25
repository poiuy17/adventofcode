with open('input.txt') as f:
    data = f.read()

example = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...\
"""

# part 1: 41
# part 2: 6
# data = example

ans1 = 0
ans2 = 0

map = data.splitlines()

# up, right, down, left
direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]


for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] == '^':
            start_pos = (row, col)
            break


row, col = start_pos
direction = 0
path = set()


while True:
    dr, dc = direc[direction]
    new_row = row + dr
    new_col = col + dc

    # leave the map
    if not (0 <= new_row < len(map) and 0 <= new_col < len(map[0])):
        break

    # turn right
    if map[new_row][new_col] == '#':
        direction = (direction + 1) % 4
    else:
        row = new_row
        col = new_col
        path.add((row, col))

ans1 = len(path)

for obs in path:
    if obs == start_pos:
        continue

    row, col = start_pos
    direction = 0
    seen = set()

    while True:
        state = (row, col, direction)
        if state in seen:
            ans2 += 1
            print(f'pos({row}, {col}), dir = {direction}')
            break

        seen.add(state)

        dr, dc = direc[direction]
        new_row = row + dr
        new_col = col + dc

        if not (0 <= new_row < len(map) and 0 <= new_col < len(map[0])):
            break

        if map[new_row][new_col] == '#' or (new_row, new_col) == obs:
            direction = (direction + 1) % 4
        else:
            row = new_row
            col = new_col

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
