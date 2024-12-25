with open('input.txt') as f:
    data = f.read()

example = """\
029A
980A
179A
456A
379A\
"""

# Part 1: 126384
# Part 2:
# data = example

ans1 = 0
ans2 = 0

codes = [line for line in data.splitlines()]
nums = ['789', '456', '123', '#0A']
dirs = ['#^A', '<v>']

num_keypad = {c: i + j * 1j for i, line in enumerate(nums) for j, c in enumerate(line)}
print(num_keypad)

dir_keypad = {c: i + j * 1j for i, line in enumerate(dirs) for j, c in enumerate(line)}
print(dir_keypad)


def move(start, target):
    if start.isdigit() or target.isdigit():
        keypad = num_keypad
    else:
        keypad = dir_keypad

    d = keypad[target] - keypad[start]
    dx, dy = int(d.real), int(d.imag)
    de = keypad['#'] - keypad[start]

    v = '^' * max(0, -dx) + 'v' * max(0, dx)
    h = '<' * max(0, -dy) + '>' * max(0, dy)

    if (dy > 0 or de == dy*1j):
        if de != dx:
            return v + h + 'A'
    return h + v + 'A'


def solve(code, n, cache={}):
    if (code, n) in cache:
        return cache[(code, n)]
    if n == 0:
        return len(code)

    pos = 'A'
    r = 0

    for c in code:
        r += solve(move(pos, c), n - 1, cache)
        pos = c

    cache[(code, n)] = r
    return r


def complexity(n):
    return sum(int(code[:-1]) * solve(code, n + 1) for code in codes)


ans1 = complexity(2)
ans2 = complexity(25)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
