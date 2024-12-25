import re

with open('input.txt') as f:
    data = f.read()

example = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279\
"""

# Part 1: 480
# Part 2:
# data = example

ans1 = 0
ans2 = 0

data = data.strip().split('\n\n')

machines = []
for lines in data:
    ax, ay, bx, by, px, py = list(map(int, re.findall(r'\d+', lines)))
    machines.append([ax, ay, bx, by, px, py])


def find_solution(machine, error=0):
    tokens = 0

    ax, ay, bx, by, px, py = machine
    px += error
    py += error

    a = round((py / by - px / bx) / (ay / by - ax / bx))
    b = round((px - a * ax) / bx)

    if a * ax + b * bx == px and a * ay + b * by == py:
        tokens += 3 * a + b

    return tokens


for machine in machines:
    ans1 += find_solution(machine)
    ans2 += find_solution(machine, error=10000000000000)


print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
