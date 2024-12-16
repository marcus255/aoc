import aoc
from heapq import heappop, heappush

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 11048, 64

# Common
grid = [[x for x in line] for line in lines]
W, H = len(grid[0]), len(grid)
START_POS = (1, H - 2)
END_POS = (W - 2, 1)
START_DIR = (1, 0) # east (right)
WALL = '#'

def get_printed_path(grid, path):
    MAGENTA = '\033[95m'
    END = '\033[0m'
    path_str = '\n'
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            path_str += f'{MAGENTA}+{END}' if (x, y) in path else c
        path_str += '\n'
    return path_str

# Part 1
aoc.mark_task_start()

queue = [(0, START_POS, START_DIR)]
lowest_cost = 0
seen = {(START_POS, START_DIR)}
while queue:
    cost, pos, dir = heappop(queue)
    x, y = pos
    dx, dy = dir
    seen.add((pos, dir))

    if pos == END_POS:
        lowest_cost = cost
        break

    moves = [
        (cost + 1, x + dx, y + dy, dir), # move forward
        (cost + 1000, x, y, (dy, -dx)),  # rotate left
        (cost + 1000, x, y, (-dy, dx))   # rotate right
    ]

    for new_cost, new_x, new_y, new_dir in moves:
        if grid[new_y][new_x] == WALL:
            continue
        if ((new_x, new_y), new_dir) in seen:
            continue
        heappush(queue, (new_cost, (new_x, new_y), new_dir))

result1 = lowest_cost
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
queue = [(0, START_POS, START_DIR, [])]
seen = {(START_POS, START_DIR)}
best_tiles = {START_POS}

while queue:
    cost, pos, dir, path = heappop(queue)
    # Use lowest_cost from part 1 to skip paths with higher cost
    if cost > lowest_cost:
        break

    x, y = pos
    dx, dy = dir
    seen.add((pos, dir))

    if pos == END_POS:
        lowest_cost = cost
        best_tiles = best_tiles.union(set(path))

    moves = [
        (cost + 1, x + dx, y + dy, dir), # move forward
        (cost + 1000, x, y, (dy, -dx)),  # rotate left
        (cost + 1000, x, y, (-dy, dx))   # rotate right
    ]

    for new_cost, new_x, new_y, new_dir in moves:
        if grid[new_y][new_x] == '#':
            continue
        if ((new_x, new_y), new_dir) in seen:
            continue
        heappush(queue, (new_cost, (new_x, new_y), new_dir, path + [(new_x, new_y)]))

# print(get_printed_path(grid, best_tiles))
result2 = len(best_tiles)
aoc.print_result(2, result2, exp2)
