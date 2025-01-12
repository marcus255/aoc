import aoc
from heapq import heappop, heappush

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 40, 315

# Common
coords = {}
for y, line in enumerate(lines):
    for x, item in enumerate(line):
        coords[(x, y)] = int(item)
W, H = len(lines[0]), len(lines)
START, END = (0, 0), (W - 1, H - 1)

def find_lowest_cost(coords, end):
    w, h = end
    visited = set([START])
    queue = [(0, START)]
    while queue:
        cost, coord = heappop(queue)
        if coord == end:
            return cost
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = next = coord[0] + dx, coord[1] + dy
            if not (0 <= nx <= w and 0 <= ny <= h):
                continue
            if next in visited:
                continue
            visited.add(next)
            heappush(queue, (cost + coords[next], next))

# Part 1
aoc.mark_task_start()
result1 = find_lowest_cost(coords, END)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
# Expand 5x horizontally
h_coords = coords.copy()
for (x, y), v in coords.items():
    for i in range(1, 5):
        h_coords[(x + W * i, y)] = v + i if (v + i) <= 9 else (v + i + 1) % 10 
# Expand 5x vertically
hv_coords = h_coords.copy()
for (x, y), v in h_coords.items():
    for i in range(1, 5):
        hv_coords[(x, y + H * i)] = v + i if (v + i) <= 9 else (v + i + 1) % 10 
result2 = find_lowest_cost(hv_coords, (5 * W - 1, 5 * H - 1))
aoc.print_result(2, result2, exp2)
