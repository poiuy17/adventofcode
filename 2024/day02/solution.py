with open('input.txt') as f:
    data = f.read()

example = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9\
"""

# Part 1: 2
# Part 2: 4
# data = example

ans1 = 0
ans2 = 0

data = data.splitlines()

def safe(line):
    diff = [1, 2, 3] if int(line[0]) < int(line[1]) else [-1, -2, -3]
    for i in range(len(line) - 1):
        if int(line[i + 1]) - int(line[i]) not in diff:
            return False
    return True

for line in data:
    line = line.strip().split()

    if safe(line):
        ans1 += 1
        ans2 += 1
        continue

    for i in range(len(line)):
        newline = line[:i] + line[i + 1 :]
        if safe(newline):
            ans2 += 1
            break

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')