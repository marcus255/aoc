import aoc
from heapq import heappop, heappush

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 31, 29

# Common
W, H = len(lines[0]), len(lines)
grid = [[] for _ in range(H)]
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x, y)
            grid[y].append(0)
        elif c == 'E':
            end = (x, y)
            grid[y].append(ord('z') - ord('a'))
        else:
            grid[y].append(ord(c) - ord('a'))

def shortest_path(start):
    queue = [(0, start)]
    visited = {}
    while queue:
        d, (x, y) = heappop(queue)
        elev = grid[y][x]
        if (x, y) == end:
            return d
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= W or ny >= H:
                continue
            new_elev = grid[ny][nx]
            if new_elev > elev + 1:
                continue
            if (nx, ny) in visited:
                continue
            new_d = d + 1
            visited[(nx, ny)] = new_d
            heappush(queue, (new_d, (x+dx, y+dy)))
    return None

# Part 1
aoc.mark_task_start()
result1 = shortest_path(start)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
starting_points = [(x, y) for y in range(H) for x in range(W) if grid[y][x] == 0]
result2 = min(filter(lambda x: x is not None, [shortest_path(start) for start in starting_points]))
aoc.print_result(2, result2, exp2)
