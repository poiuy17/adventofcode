with open('input.txt') as f:
    data = f.read()

example = """\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn\
"""

# Part 1: 7
# Part 2: co,de,ka,ta
# data = example

ans1 = 0
ans2 = 0

conns = {}
lines = data.splitlines()
for line in lines:
    a, b = line.split('-')
    if a not in conns:
        conns[a] = set()
    if b not in conns:
        conns[b] = set()
    conns[a].add(b)
    conns[b].add(a)

computers = sorted(conns.keys())

triplets = []
for a in conns:
    for b in conns[a]:
        if a > b:
            continue
        for c in computers[computers.index(b) + 1 :]:
            if c in conns[a] and c in conns[b]:
                if any(x.startswith('t') for x in (a, b, c)):
                    triplets.append((a, b, c))

ans1 = len(triplets)

partys = [{c} for c in computers]
for party in partys:
    for c in computers:
        if all(c in conns[p] for p in party):
            party.add(c)

largest = max(partys, key=len)
ans2 = ','.join(sorted(largest))


print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
