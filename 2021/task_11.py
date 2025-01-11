import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1656, 195

# Common
W, H = len(lines[0]), len(lines)
input_grid = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        input_grid[(x, y)] = int(c)

def neighbors(x, y):
    neighbors = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
    neighbors = filter(lambda n: 0 <= n[0] < W and 0 <= n[1] < H, neighbors)
    return list(neighbors)

def process_grid(grid, coords, flashed_cells):
    triggered_cells = []
    for coord in coords:
        if coord in flashed_cells:
            continue
        if grid[coord] == 9:
            flashed_cells.add(coord)
            triggered_cells.extend(neighbors(coord[0], coord[1]))
        else:
            grid[coord] += 1
    return triggered_cells

def perform_step(grid):
    flashed_cells = set()
    active_cells = process_grid(grid, grid.keys(), flashed_cells)
    while active_cells:
        active_cells = process_grid(grid, active_cells, flashed_cells)
    for coord in flashed_cells:
        grid[coord] = 0
    return len(flashed_cells)

# Part 1
aoc.mark_task_start()
grid = input_grid.copy()
for i in range(100):
    result1 += perform_step(grid)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
grid = input_grid.copy()
flashed = 0
while flashed != len(grid):
    flashed = perform_step(grid)
    result2 += 1
aoc.print_result(2, result2, exp2)
