with open('input.txt') as f:
    data = f.read()

example = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47\
"""

# Part 1: 143
# Part 2: 123
# data = example


ans1 = 0
ans2 = 0

rules_data, pages_data = data.split('\n\n')
rules_data = rules_data.splitlines()
pages_data = pages_data.splitlines()


rules = {}
for line in rules_data:
    a, b = map(int, line.split('|'))
    if a not in rules:
        rules[a] = []
    rules[a].append(b)


for line in pages_data:
    pages = list(map(int, line.split(',')))

    check = True
    correct = []
    for page in pages:
        for i, p in enumerate(correct):
            if p in rules.get(page, []):
                check = False
                correct.insert(i, page)
                break
        else:
            correct.append(page)

    middle = len(pages) // 2
    if check:
        ans1 += pages[middle]

    else:
        ans2 += correct[middle]


print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')