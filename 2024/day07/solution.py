from itertools import product

with open('input.txt') as f:
    data = f.read()

example = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20\
"""

# part 1: 3749
# part 2: 11387
# data = example

ans1 = 0
ans2 = 0

data = data.splitlines()
equations = []
for line in data:
    lhs, rhs = line.strip().split(':')
    lhs = int(lhs)
    nums = list(map(int, rhs.split()))
    equations.append((lhs, nums))


def evaluate_equation(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i - 1] == '+':
            result += numbers[i]
        elif operators[i - 1] == '*':
            result *= numbers[i]
        elif operators[i - 1] == '||':
            result = int(str(result) + str(numbers[i]))
    return result


def calibration(equations, concat=False):
    total = 0
    for equation in equations:
        v, nums = equation
        n = len(nums)

        if not concat:
            operators = product(['+', '*'], repeat=n - 1)
        else:
            operators = product(['+', '*', '||'], repeat=n - 1)

        for operator in operators:
            if evaluate_equation(nums, operator) == v:
                total += v
                break

    return total

ans1 = calibration(equations)
ans2 = calibration(equations, True)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
