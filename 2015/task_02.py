import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 101, 48

# Common
boxes = []
for line in lines:
    boxes.append(tuple(int(x) for x in line.split('x')))

# Part 1
aoc.mark_task_start()
for w, h, l in boxes:
    sides = [w * h, h * l, l * w]
    result1 += 2 * sum(sides) + min(sides)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
for w, h, l in boxes:
    perims = [2 * (w + h), 2 * (h + l), 2 * (l + w)]
    result2 += min(perims) + w * h * l
aoc.print_result(2, result2, exp2)
