import aoc
from functools import cmp_to_key

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 13, 140

# Common
pair, pairs = [], []
for line in lines:
    if not line:
        pairs.append(pair)
        pair = []
    else:
        pair.append(eval(line))
pairs.append(pair)

#  0: equal
# -1: p1 < p2
#  1: p1 > p2
def compare(p1, p2):
    if p1 == p2 or [p1] == p2 or p1 == [p2]:
        return 0
    if isinstance(p1, list) and not isinstance(p2, list):
        p2 = [p2]
    if not isinstance(p1, list) and isinstance(p2, list):
        p1 = [p1]
    if isinstance(p1, list) and isinstance(p2, list):
        for a, b in zip(p1, p2):
            res = compare(a, b)
            if res != 0:
                return res
        return -1 if len(p1) < len(p2) else 1
    else:
        return -1 if p1 < p2 else 1

# Part 1
aoc.mark_task_start()
result1 = 0
for i, (p1, p2) in enumerate(pairs):
    res = compare(p1, p2)
    if res == -1:
        result1 += (i + 1)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
all_items = [item for sublist in pairs for item in sublist]
all_items.extend([[[2]], [[6]]])
result2 = 1
all_items = sorted(all_items, key=cmp_to_key(compare))
for i, item in enumerate(all_items):
    if item == [[2]] or item == [[6]]:
        result2 *= (i + 1)

aoc.print_result(2, result2, exp2)
