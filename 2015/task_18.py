import aoc
from itertools import product
from functools import cache
from copy import deepcopy

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 4, 17

# Common
W, H = len(lines[0]), len(lines)
input_grid = [[False for _ in range(W)] for _ in range(H)]
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '#':
            input_grid[y][x] = True

def print_grid(grid):
    if not aoc.is_test_mode():
        # will flood the output in task mode
        return
    for line in grid:
        for c in line:
            print('#' if c else '.', end='')
        print()
    print()

@cache
def get_neighbors(x, y):
    neighbors = []
    for xx, yy in product(range(x - 1, x + 2), range(y - 1, y + 2)):
        if (xx, yy) != (x, y) and (0 <= xx < W) and (0 <= yy < H):
            neighbors.append((xx, yy))
    return tuple(neighbors)

# Rules for this Game of life:
# A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
def apply_rules(grid, excludes=None):
    new_grid = deepcopy(grid)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if excludes and (x, y) in excludes:
                continue
            neighbors = get_neighbors(x, y)
            live = sum([grid[y][x] for x, y in neighbors])
            if c and live not in [2, 3]:
                new_grid[y][x] = False
            elif not c and live == 3:
                new_grid[y][x] = True
    return new_grid

# Part 1
aoc.mark_task_start()
STEPS = 4 if aoc.is_test_mode() else 100
grid = deepcopy(input_grid)
for _ in range(STEPS):
    grid = apply_rules(grid)
    # print_grid(grid)
result1 = sum([sum(x) for x in grid])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
STEPS = 5 if aoc.is_test_mode() else 100
grid = deepcopy(input_grid)
corners = [(0, 0), (0, H - 1), (W - 1, 0), (W - 1, H - 1)]
for x, y in corners:
    grid[y][x] = True
for _ in range(STEPS):
    grid = apply_rules(grid, excludes=corners)
    # print_grid(grid)
result2 = sum([sum(x) for x in grid])
aoc.print_result(2, result2, exp2)
