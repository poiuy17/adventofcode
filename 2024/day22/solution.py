with open('input.txt') as f:
    data = f.read()

example = """\
1
10
100
2024\
"""

example2 = """\
1
2
3
2024\
"""


# Part 1: 37327623
# Part 2:
# data = example2

ans1 = 0
ans2 = 0

buyers = list(map(int, data.splitlines()))


def mix(s, v):
    return s ^ v


def prune(s):
    return s % 16777216


def next_secret(s):
    ns = mix(s, s * 64)
    ns = prune(ns)
    ns = mix(ns, ns // 32)
    ns = prune(ns)
    ns = mix(ns, ns * 2048)
    ns = prune(ns)
    return ns


def secrets_price_change(secret, n=2000):
    s = secret
    secrets = [s]
    prices = [s % 10]
    changes = []

    last = s % 10
    for _ in range(n):
        s = next_secret(s)
        secrets.append(s)

        new = s % 10
        prices.append(new)
        changes.append(new - last)
        last = new

    return secrets, prices, changes


all_seqs = {}
for buyer in buyers:
    secrets, prices, changes = secrets_price_change(buyer)

    ans1 += secrets[-1]

    seen = set()
    for i in range(len(secrets) - 4):
        seq = tuple(changes[i : i + 4])

        if seq not in seen:
            if seq not in all_seqs:
                all_seqs[seq] = 0
            all_seqs[seq] += prices[i + 4]
            seen.add(seq)

ans2 = max(all_seqs.values())

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
