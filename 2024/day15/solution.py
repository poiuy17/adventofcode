with open('input.txt') as f:
    data = f.read()

example = """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<\
"""
example2 = """\
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^\
"""

# Part 1: 2028
# Part 2:
# data = example2

ans1 = 0
ans2 = 0

warehouse, moves = data.split('\n\n')
moves = moves.replace('\n', '')


def plot_grid(grid):
    for p in grid:
        print(grid[p], end='')
        if p.imag == max(p.imag for p in grid):
            print()


def sokuban(warehouse, moves):
    grid = {(i + j * 1j): c for i, r in enumerate(warehouse.splitlines()) for j, c in enumerate(r)}
    direc = {'^': -1, 'v': +1, '<': -1j, '>': +1j}

    for p, c in grid.items():
        if c == '@':
            robot = p
            break

    # plot_grid(grid)

    for move in moves:
        # print(f'move: {move}')
        d = direc[move]
        new_p = robot + d

        if grid[new_p] == '#':
            continue

        if grid[new_p] not in 'O[]':
            grid[robot], grid[new_p] = grid[new_p], grid[robot]
            robot = new_p

        else:
            box1 = new_p
            to_push = []
            checked = set()
            queue = []
            # queue.append(new_p)

            def insert_box(pos):
                queue.append(pos)
                if grid[pos] == '[' and pos + 1j not in checked:
                    queue.append(pos + 1j)
                elif grid[pos] == ']' and pos - 1j not in checked:
                    queue.append(pos - 1j)

            insert_box(new_p)

            while queue:
                pos = queue.pop(0)

                if pos in checked:
                    continue

                checked.add(pos)
                to_push.append(pos)
                new_pos = pos + d

                if grid[new_pos] == '#':
                    to_push = []
                    break

                if grid[new_pos] in 'O[]':
                    # queue.append(new_pos)
                    insert_box(new_pos)

            if to_push:
                to_push.sort(key=lambda x: (x.real * d.real + x.imag * d.imag), reverse=True)
                for p in to_push:
                    grid[p], grid[p + d] = grid[p + d], grid[p]

                grid[robot], grid[box1] = grid[box1], grid[robot]
                robot = box1

        # plot_grid(grid)

    gps_sum = int(sum(p.real * 100 + p.imag for p in grid if grid[p] in 'O['))

    return gps_sum


ans1 = sokuban(warehouse, moves)

new_map = {'#': '##', '.': '..', 'O': '[]', '@': '@.'}
new_warehouse = '\n'.join(''.join(new_map[c] for c in r) for r in warehouse.splitlines())

ans2 = sokuban(new_warehouse, moves)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
