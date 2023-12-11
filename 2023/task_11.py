import aoc
import functools
import operator

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 374, 8410

# Common
HEIGHT = len(lines)
WIDTH = len(lines[0])
same_rows, same_cols, coords = [], [], []
space = [[x for x in line] for line in lines]

for i, row in enumerate(space):
    empty_elems = 0
    for col in row:
        if col == '.':
            empty_elems += 1
    if empty_elems == WIDTH:
        same_rows.append(i)

for i in range(WIDTH):
    empty_elems = 0
    for j in range(HEIGHT):
        if space[j][i] == '.':
            empty_elems += 1
        if space[j][i] == '#':
            coords.append((j, i))
    if empty_elems == HEIGHT:
        same_cols.append(i)

def get_extra_steps_count(same_items, A, B):
    same_item_count = 0
    for item in same_items:
        a, b = sorted([A, B])
        if item in range(a, b):
            same_item_count += 1
    return same_item_count

def get_distances_sum(empty_space):
    distances = []
    for i, x in enumerate(coords):
        for j, y in enumerate(coords):
            if i == j:
                continue
            same_row_count = get_extra_steps_count(same_rows, x[0], y[0])
            same_col_count = get_extra_steps_count(same_cols, x[1], y[1])
            extra_x_steps = same_row_count * (empty_space - 1)
            extra_y_steps = same_col_count * (empty_space - 1)
            d = abs(x[0] - y[0]) + abs(x[1] - y[1]) + extra_x_steps + extra_y_steps
            # print(f'{i+1}=>{j+1}: {d}')
            distances.append(d)
    return functools.reduce(operator.add, distances) // 2

# Part 1
result1 = get_distances_sum(2)
aoc.print_result(1, result1, exp1)

# Part 2
EMTPY_SPACE = 100 if aoc.is_test_mode() else 1000_000
result2 = get_distances_sum(EMTPY_SPACE)
aoc.print_result(2, result2, exp2)
