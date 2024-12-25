with open('input.txt') as f:
    data = f.read()

example = """\
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0\
"""

# Part 1: 22 steps to reach (6, 6) after the first 12 bytes have fallen
# Part 2: (6,1)
# data = example

data = list(map(eval, data.splitlines()))


def reach_exit(a, n=70):
    start = (0, 0)
    queue = [(0, start)]
    visited = set(data[:a])

    while queue:
        level, (x, y) = queue.pop(0)

        if (x, y) == (n, n):
            return level

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and 0 <= nx <= n and 0 <= ny <= n:
                queue.append((level + 1, (nx, ny)))
                visited.add((nx, ny))
    return None


def part2():
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if reach_exit(mid + 1) is not None:
            left = mid + 1
        else:
            right = mid - 1

    return mid


# total1 = reach_exit(12, 6)
ans1 = reach_exit(1024)
ans2 = data[part2()]

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
