import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 2024, 1

# Common
registers, instructions = {}, []
for line in lines:
    if ':' in line:
        k, v = line.split(': ')
        registers[k] = int(v)
    elif '->' in line:
        instructions.append(line.split(' -> '))

ops = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'XOR': lambda a, b: a ^ b,
}

def process_instructions(registers, instructions):
    regs = registers.copy()
    while instructions:
        operation, result = instructions.pop(0)
        a, op, b = operation.split(' ')
        if a not in regs or b not in regs:
            instructions.append((operation, result))
            continue
        regs[result] = ops[op](regs[a], regs[b])
    return regs

# Part 1
aoc.mark_task_start()
regs = process_instructions(registers, instructions)
z_regs = [(k, v) for k, v in regs.items() if k.startswith('z')]
z_regs = sorted(z_regs, key=lambda x: x[0])
result1 = sum([v * (2 ** i) for i, (_, v) in enumerate(z_regs)])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()



aoc.print_result(2, result2, exp2)
