import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 150, 900

# Common
instructions = []
for line in lines:
    instr, value = line.split(' ')
    instructions.append((instr, int(value)))

# Part 1
aoc.mark_task_start()
x, y = 0, 0
for instr, value in instructions:
    if instr == 'forward':
        x += value
    else:
        y += value if instr == 'down' else -value
result1 = x * y
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
x, y = 0, 0
aim = 0
for instr, value in instructions:
    if instr == 'forward':
        x += value
        y += value * aim
    else:
        aim += value if instr == 'down' else -value
result2 = x * y
aoc.print_result(2, result2, exp2)
