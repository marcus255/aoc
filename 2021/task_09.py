import aoc
from collections import deque
from functools import reduce
import operator

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 15, 1134

# Common
grid = [[int(x) for x in line] for line in lines]
W, H = len(grid[0]), len(grid)

def neighbor_values(grid, x, y):
    values = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H:
            values.append(grid[ny][nx])
    return values

def find_basin_cells(undiscovered : set, nines : set) -> set:
    start = next(iter(undiscovered))
    visited = set()
    queue = deque([start])
    while queue:
        coord = x, y = queue.popleft()
        visited.add(coord)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < W and 0 <= ny < H):
                continue
            if (nx, ny) in nines or (nx, ny) in visited:
                continue
            queue.append((nx, ny))
    return visited

# Part 1
aoc.mark_task_start()
for y, line in enumerate(grid):
    for x, item in enumerate(line):
        if item < min(neighbor_values(grid, x, y)):
            result1 += (1 + item)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
grid_coords = {(x, y) for x in range(W) for y in range(H)}
nines = set(filter(lambda coord: grid[coord[1]][coord[0]] == 9, grid_coords))
undiscovered = grid_coords - nines
basin_lens = []
while undiscovered:
    cells = find_basin_cells(undiscovered, nines)
    basin_lens.append(len(cells))
    undiscovered -= cells
result2 = reduce(operator.mul, sorted(basin_lens, reverse=True)[:3])
aoc.print_result(2, result2, exp2)
