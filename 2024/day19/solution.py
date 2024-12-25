with open('input.txt') as f:
    data = f.read()

example = """\
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb\
"""

# Part 1: 6
# Part 2: 16
# data = example

ans1 = 0
ans2 = 0

patterns, designs = data.strip().split('\n\n')
patterns = patterns.split(', ')
designs = designs.splitlines()


def count(design, patterns, mem={}):
    if design in mem:
        return mem[design]

    if not design:
        return 1

    total = 0
    for p in patterns:
        if design.startswith(p):
            total += count(design[len(p) :], patterns, mem)

    mem[design] = total
    return total


for design in designs:
    c = count(design, patterns)
    if c > 0:
        ans1 += 1
        ans2 += c

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
