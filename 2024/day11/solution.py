with open('input.txt') as f:
    data = f.read()

example = """\
125 17\
"""

# Part 1: 55312
# Part 2:
# data = example

ans1 = 0
ans2 = 0

data = list(map(int, data.split()))


def blink(s, n, cache={}):
    k = (s, n)
    d = len(str(s))

    if k in cache:
        return cache[k]

    elif n == 0:
        cache[k] = 1

    elif s == 0:
        cache[k] = blink(1, n - 1)

    elif d % 2 == 0:
        m = d // 2
        s1 = s // (10**m)
        s2 = s % (10**m)
        cache[k] = blink(s1, n - 1) + blink(s2, n - 1)
        return cache[k]
    else:
        cache[k] = blink(s * 2024, n - 1)

    return cache[k]


for d in data:
    ans1 += blink(d, 25)
    ans2 += blink(d, 75)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
