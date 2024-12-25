with open('input.txt') as f:
    data = f.read()

example = """\
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj\
"""

# Part 1: 2024
# Part 2:
# data = example

ans1 = 0
ans2 = 0

section1, section2 = data.split('\n\n')

wires = {}
for line in section1.splitlines():
    wire, value = line.split(': ')
    wires[wire] = int(value)

gates = []
for line in section2.splitlines():
    inputs, out = line.split(' -> ')
    in1, op, in2 = inputs.split()
    gates.append((in1, op, in2, out))


def part1(wires, gates):
    queue = gates.copy()
    while queue:
        in1, op, in2, out = queue.pop(0)
        if in1 in wires and in2 in wires:
            if op == 'AND':
                wires[out] = wires[in1] & wires[in2]
            elif op == 'OR':
                wires[out] = wires[in1] | wires[in2]
            elif op == 'XOR':
                wires[out] = wires[in1] ^ wires[in2]
        else:
            queue.append((in1, op, in2, out))

    new_wires = sorted([wire for wire in wires if wire.startswith('z')], reverse=True)
    bits = ''.join(str(wires[wire]) for wire in new_wires)

    return int(bits, 2)


ans1 = part1(wires.copy(), gates)

def part2(gates):
    wrongs = set()
    for gate in gates:
        in1, op, in2, out = gate

        if op != 'XOR':
            if out.startswith('z') and out != 'z45':
                wrongs.add(out)

        if op == 'XOR':
            if all(not item.startswith(('x', 'y', 'z')) for item in (out, in1, in2)):
                wrongs.add(out)

        if op == 'AND':
            if 'x00' not in (in1, in2):
                for new_gate in gates:
                    new_in1, new_op, new_in2, new_out = new_gate
                    if out == new_in1 or out == new_in2:
                        if new_op == 'XOR':
                            wrongs.add(out)

        if op == 'XOR':
            if 'x00' not in (in1, in2):
                for new_gate in gates:
                    new_in1, new_op, new_in2, new_out = new_gate
                    if out == new_in1 or out == new_in2:
                        if new_op == 'OR':
                            wrongs.add(out)

    return ','.join(sorted(wrongs))



ans2 = part2(gates)

print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
