with open('input.txt') as f:
    data = f.read()

example = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............\
"""

# Part 1: 14
# Part 2: 34
# data = example

ans1 = 0
ans2 = 0

data = data.splitlines()

N = len(data)
M = len(data[0])

antennas = {}
for row, line in enumerate(data):
    for col, char in enumerate(line):
        if char != '.':
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((row, col))

antinodes = set()
antinodes2 = set()

for _, positions in antennas.items():
    n = len(positions)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            dx = x2 - x1
            dy = y2 - y1

            if 0 <= x1 - dx < N and 0 <= y1 - dy < M:
                antinodes.add((x1 - dx, y1 - dy))
            if 0 <= x2 + dx < N and 0 <= y2 + dy < M:
                antinodes.add((x2 + dx, y2 + dy))

            while 0 <= x1 < N and 0 <= y1 < M:
                antinodes2.add((x1, y1))
                x1 -= dx
                y1 -= dy

            while 0 <= x2 < N and 0 <= y2 < M:
                antinodes2.add((x2, y2))
                x2 += dx
                y2 += dy

ans1 = len(antinodes)
ans2 = len(antinodes2)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')