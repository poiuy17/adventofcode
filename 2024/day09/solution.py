with open('input.txt') as f:
    data = f.read()

example = '2333133121414131402'

# Part 1: 1928
# Part 2: 2858
# data = example

ans1 = 0
ans2 = 0


def blocks_setup(nums):
    blocks = []
    for i, n in enumerate(nums):
        if i % 2 == 0:
            blocks.extend([i // 2] * n)
        else:
            blocks.extend([None] * n)
    return blocks


def checksum(blocks):
    return sum(i * v for i, v in enumerate(blocks) if v is not None)


def create_free_space(blocks):
    free_space = []
    length = 0
    idx = -1
    for i, v in enumerate(blocks):
        if v is None:
            if length == 0:
                idx = i
            length += 1
        else:
            if length > 0:
                free_space.append((idx, length))
            length = 0
    if length > 0:
        free_space.append((idx, length))

    return free_space


def first_fit(free_space, target):
    for idx, length in free_space:
        if length >= target:
            return idx
    return None


nums = list(map(int, data))

blocks = blocks_setup(nums)

n = len(blocks)
right = n - 1
left = 0
while left < right:
    if blocks[left] is not None:
        left += 1
    elif blocks[right] is None:
        right -= 1
    else:
        blocks[left] = blocks[right]
        blocks[right] = None


ans1 = checksum(blocks)


blocks = blocks_setup(nums)
files = [(i, blocks.count(v)) for i, v in enumerate(blocks) if v is not None and v != blocks[i - 1]]


moved = True
for idx, length in reversed(files):
    if moved:
        free_space = create_free_space(blocks)
        moved = False

    dest = first_fit(free_space, length)

    if dest is not None and dest < idx:
        blocks[dest : dest + length] = [blocks[idx]] * length
        blocks[idx : idx + length] = [None] * length
        moved = True


ans2 = checksum(blocks)


print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')