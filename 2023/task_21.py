import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 16, 1

# Common
grid = []
start = None
for r, line in enumerate(lines):
    if 'S' in line:
        start = (r, line.index('S'))
    grid.append([x for x in line])
grid[start[0]][start[1]] = '.'
H, W = len(grid), len(grid[0])

def find_neighbors(grid, position):
    r, c = position
    neighbors = []
    for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if rr == r and cc == c:
            continue
        if grid[rr % W][cc % H] == '.':
            neighbors.append((rr, cc))
    return neighbors

def print_grid(grid, selected):
    print()
    tmp_grid = [x[:] for x in grid]
    for r, c in selected:
        tmp_grid[r][c] = 'O'
    for line in tmp_grid:
        print(f'{"".join(line)}')

def find_num_fields(grid, steps, start):
    neighbors = [start]
    for _ in range(steps):
        next_neighbors = set()
        for n in neighbors:
            n = find_neighbors(grid, n)
            next_neighbors.update(n)
        neighbors = list(next_neighbors)
    # print_grid(grid, neighbors)

    return len(neighbors)

# Part 1
aoc.mark_task_start()
steps = 6 if aoc.is_test_mode() else 64
result1 = find_num_fields(grid, steps, start)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
aoc.print_result(1, result2, exp2)
