with open('input.txt') as f:
    data = f.read()

example = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX\
"""

# Part 1: 18
# Part 2: 9
# data = example

ans1 = 0
ans2 = 0


data = data.splitlines()
map = {(i, j): c for i, line in enumerate(data) for j, c in enumerate(line)}

direc = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

for (row, col), char in map.items():
    if char == 'X':
        for dx, dy in direc:
            check = True
            for i in range(3):
                x = row + dx * (i + 1)
                y = col + dy * (i + 1)
                if map.get((x, y)) != ['M', 'A', 'S'][i]:
                    check = False
                    break
            if check:
                ans1 += 1


for (row, col), char in map.items():
    if char == 'A':
        a = ''
        b = ''

        a += map.get((row - 1, col - 1), '')
        a += 'A'
        a += map.get((row + 1, col + 1), '')

        b += map.get((row - 1, col + 1), '')
        b += 'A'
        b += map.get((row + 1, col - 1), '')

        if a in ['MAS', 'SAM'] and b in ['MAS', 'SAM']:
            ans2 += 1


print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')