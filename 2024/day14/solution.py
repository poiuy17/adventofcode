import re

with open('input.txt') as f:
    data = f.read()

example = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3\
"""

# Part 1: 12
# Part 2:
# data = example

ans1 = 0
ans2 = 0

robots = []
for line in data.splitlines():
    px,py,vx,vy = map(int, re.findall(r'-?\d+', line))
    robots.append([px, py, vx, vy])

W = 101
H = 103

def robots_pos(robots, t):
    return [((px + t * vx) % W, (py + t * vy) % H) for px, py, vx, vy in robots]

def safety_factor(robots, t):
    a = b = c = d = 0
    grid = robots_pos(robots, t)
    for (x, y) in grid:
        a += x > W // 2 and y > H // 2
        b += x > W // 2 and y < H // 2
        c += x < W // 2 and y > H // 2
        d += x < W // 2 and y < H // 2

    # print([a, b, c, d])
    return a * b * c * d


ans1 = safety_factor(robots, 100)
a = []
for t in range(W * H):
    a.append(safety_factor(robots, t))
    ans2 = a.index(min(a))

# plot the Easter egg
grid = robots_pos(robots, ans2)
for y in range(H):
    for x in range(W):
        print('#' if (x, y) in grid else '.', end='')
    print()

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
