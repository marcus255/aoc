import aoc
from itertools import product

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 998996, 1001996

# Common
ON, OFF, TOG = 1, 2, 3
subgrids = []
for line in lines:
    if 'turn on' in line:
        op = ON
    elif 'turn off' in line:
        op = OFF
    elif 'toggle' in line:
        op = TOG
    coords = [x for x in line.split(' ') if ',' in x]
    nums = tuple(map(int, coords[0].split(',') + coords[1].split(',')))
    subgrids.append((op, nums))

# Part 1
aoc.mark_task_start()
lit_cells = set()
for op, (x1, y1, x2, y2) in subgrids:
    turnoff = op in [OFF, TOG]
    turnon = op in [ON, TOG]
    for x, y in product(range(x1, x2 + 1), range(y1, y2 + 1)):
        item = (x, y)
        if item in lit_cells and turnoff:
            lit_cells.remove(item)
        elif turnon:
            lit_cells.add(item)
result1 = len(lit_cells)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
lit_cells = {}
for x, y in product(range(1001), range(1001)):
    lit_cells[(x, y)] = 0
for op, (x1, y1, x2, y2) in subgrids:
    brighten = op in [ON, TOG]
    inc = 1 if op == ON else 2
    dimm = op == OFF
    for x, y in product(range(x1, x2 + 1), range(y1, y2 + 1)):
        item = (x, y)
        if brighten:
            lit_cells[item] += inc
        elif dimm and lit_cells[item] > 0:
            lit_cells[item] -= 1
result2 = sum(lit_cells.values())
aoc.print_result(2, result2, exp2)
