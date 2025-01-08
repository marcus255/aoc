import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 7, 5

# Common
values = list(map(int, lines))

# Part 1
aoc.mark_task_start()
for prev, next in zip(values, values[1:]):
    if next > prev:
        result1 += 1
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
for a, b, c, d in zip(values, values[1:], values[2:], values[3:]):
    if sum([b, c, d]) > sum([a, b, c]):
        result2 += 1
aoc.print_result(2, result2, exp2)
