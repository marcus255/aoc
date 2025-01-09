import aoc
from collections import Counter

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 5, 12

# Common
vents = []
for line in lines:
    a, b = line.split(' -> ')
    (ax, ay), (bx, by) = map(int, a.split(',')), map(int, b.split(','))
    vents.append((ax, ay, bx, by))

def count_overlaps(vents, diagonal=False):
    occupied = []
    for ax, ay, bx, by in vents:
        xrange = range(ax, bx + 1) if bx > ax else range(ax, bx - 1, -1)
        yrange = range(ay, by + 1) if by > ay else range(ay, by - 1, -1)
        new = []
        if ax == bx:
            new = [(ax, y) for y in yrange]
        elif ay == by:
            new = [(x, ay) for x in xrange]
        elif diagonal:
            new = [(x, y) for x, y, in zip(xrange, yrange)]
        occupied.extend(new)
    counter = Counter(occupied)
    return sum(1 for x in counter.values() if x >= 2)

# Part 1
aoc.mark_task_start()
result1 = count_overlaps(vents)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = count_overlaps(vents, diagonal=True)
aoc.print_result(2, result2, exp2)
