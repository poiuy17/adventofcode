import re

with open('input.txt') as f:
    data = f.read()

ans1 = 0
ans2 = 0

enabled = True

for a, b, do, dont in re.findall(
    r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', data
):
    if a and b:
        ans1 += int(a) * int(b)
        if enabled:
            ans2 += int(a) * int(b)
    elif do:
        enabled = True
    elif dont:
        enabled = False

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
