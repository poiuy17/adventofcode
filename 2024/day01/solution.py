with open('input.txt') as f:
    data = f.read()

example = """\
3   4
4   3
2   5
1   3
3   9
3   3\
"""

# Part 1: 11
# Part 2: 31
# data = example

data = data.splitlines()

ans1 = 0
ans2 = 0

left = []
right = []

for line in data:
    a, b = map(int, line.split())
    left.append(a)
    right.append(b)

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    ans1 += abs(left[i] - right[i])
    ans2 += left[i] * right.count(left[i])

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')