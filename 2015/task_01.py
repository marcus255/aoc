import aoc

instructions = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = -3, 1

# Common
instructions = instructions[0]

# Part 1
aoc.mark_task_start()
result1 = instructions.count('(') - instructions.count(')')
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
floor = 0
for i, c in enumerate(instructions):
    floor += 1 if c == '(' else -1
    if floor == -1:
        result2 = i + 1
        break
aoc.print_result(2, result2, exp2)
