import aoc
import re

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 12, 19

# Part 1
aoc.mark_task_start()
for line in lines:
    result1 += len(line) - len(eval(line))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
for line in lines:
    escaped = line.replace('\\', '\\\\').replace('"', '\\"')
    result2 += len(escaped) + 2 - len(line)
aoc.print_result(2, result2, exp2)
