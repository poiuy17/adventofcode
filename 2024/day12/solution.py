with open('input.txt') as f:
    data = f.read()

example = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE\
"""

# Part 1: 1930
# Part 2: 1206
# data = example

ans1 = 0
ans2 = 0


grid = {(i + j * 1j): c for i, r in enumerate(data.splitlines()) for j, c in enumerate(r)}
direc = (-1, +1, -1j, +1j)


sets = {p: {p} for p in grid}

for p in grid:
    for d in direc:
        if p + d in grid and grid[p + d] == grid[p]:
            sets[p] |= sets[p + d]
            for x in sets[p]:
                sets[x] = sets[p]

regions = {}
seen_values = set()

for k, v in sets.items():
    frezen = frozenset(v)
    if frezen not in seen_values:
        regions[k] = v
        seen_values.add(frezen)


def find_region_edges(region):
    edges = set()
    boundary = set()

    for p in region:
        for d in direc:
            if p + d not in region:
                edges.add((p, d))
                boundary.add(((p + d * 1j), d))

    sides = edges - boundary
    return edges, sides


for s in regions.values():
    edges, sides = find_region_edges(s)
    print(f'area: {len(s)} \tperimeter: {len(edges)} \tside(corner): {len(sides)}')
    ans1 += len(s) * len(edges)
    ans2 += len(s) * len(sides)


print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')