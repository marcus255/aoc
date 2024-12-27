import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 2, 4

# Common
containing_sets, overlapping_sets = 0, 0
for line in lines:
    elf1, elf2 = line.split(',')
    e1 = list(map(int, elf1.split('-')))
    e2 = list(map(int, elf2.split('-')))
    s1 = set(range(e1[0], e1[1] + 1))
    s2 = set(range(e2[0], e2[1] + 1))
    if s1 <= s2 or s2 <= s1:
        containing_sets += 1
    if s1 & s2:
        overlapping_sets += 1

# Part 1
aoc.mark_task_start()
result1 = containing_sets
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = overlapping_sets
aoc.print_result(2, result2, exp2)
