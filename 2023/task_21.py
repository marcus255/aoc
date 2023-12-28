import aoc
from collections import deque

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
def fill(start_r, start_c, steps):
    ans = set()
    seen = {start_r, start_c}
    queue = deque([(start_r, start_c, steps)])

    while queue:
        r, c, c_steps = queue.popleft()
        if c_steps % 2 == 0:
            ans.add((r, c))
        if c_steps == 0:
            continue

        for next_r, next_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if not 0 <= next_r < H or not 0 <= next_c < W:
                continue
            if lines[next_r][next_c] == "#" or (next_r, next_c) in seen:
                continue
            seen.add((next_r, next_c))
            queue.append((next_r, next_c, c_steps - 1))

    return len(ans)

aoc.mark_task_start()
# Algorithm proposed by HyperNeutrino:
#  - compute largest part first, then add missing tiles for corners and edges

STEPS, SIZE = 26501365, W
big_grid_width = STEPS // SIZE - 1

num_odd_grids = (big_grid_width // 2 * 2 + 1)**2
num_even_grids = ((big_grid_width + 1) // 2 * 2)**2

odd_points = fill(start[0], start[1], SIZE * 2 + 1)
even_points = fill(start[0], start[1], SIZE * 2)

num_steps = SIZE - 1
c_top = fill(SIZE - 1, start[1], num_steps)
c_right = fill(start[0], 0, num_steps)
c_bot = fill(0, start[1], num_steps)
c_left = fill(start[0], SIZE - 1, num_steps)

num_steps = SIZE // 2 - 1
small_tr = fill(SIZE - 1, 0, num_steps)
small_br = fill(0, 0, num_steps)
small_bl = fill(0, SIZE - 1, num_steps)
small_tl = fill(SIZE - 1, SIZE - 1, num_steps)

num_steps = 3 * SIZE // 2 - 1
big_tr = fill(SIZE - 1, 0, num_steps)
big_br = fill(0, 0, num_steps)
big_bl = fill(0, SIZE - 1, num_steps)
big_tl = fill(SIZE - 1, SIZE - 1, num_steps)

num_small_corners = big_grid_width + 1
num_big_corners = big_grid_width

result2 = num_odd_grids * odd_points
result2 += num_even_grids * even_points
result2 += c_top + c_right + c_bot + c_left
result2 += num_small_corners * (small_tr + small_br + small_bl + small_tl)
result2 += num_big_corners * (big_tr + big_br + big_bl + big_tl)

if not aoc.is_test_mode():
    aoc.print_result(1, result2, exp2)
