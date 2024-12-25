import re

with open('input.txt') as f:
    data = f.read()

example = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0\
"""

example2 = """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0\
"""

# Part 1: 4,6,3,5,6,3,5,2,1,0
# Part 2: 117440
# data = example2

ans1 = 0
ans2 = 0

reg, prog = data.split('\n\n')
reg = list(map(int, re.findall(r'\d+', reg)))
prog = list(map(int, re.findall(r'\d+', prog)))


def run(prog, reg):
    a, b, c = reg
    ip = 0
    output = []

    while ip < len(prog) - 1:
        opcode = prog[ip]
        operand = prog[ip + 1]

        combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}

        match opcode:
            case 0:
                a = a >> combo[operand]
            case 1:
                b = b ^ operand
            case 2:
                b = combo[operand] % 8
            case 3:
                if a != 0:
                    ip = operand
                    continue
            case 4:
                b = b ^ c
            case 5:
                output.append(combo[operand] % 8)
            case 6:
                b = a >> combo[operand]
            case 7:
                c = a >> combo[operand]

        ip += 2
    return output


ans1 = run(prog, reg)


def part2():
    queue = [(1, 0)]
    a_list = []
    while queue:
        level, a = queue.pop(0)
        for i in range(8):
            reg = [a + i, 0, 0]
            if run(prog, reg) == prog[-level:]:
                if level == len(prog):
                    a_list.append(a + i)
                else:
                    queue.append((level + 1, (a + i) << 3))

    return min(a_list)


ans2 = part2()


print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
