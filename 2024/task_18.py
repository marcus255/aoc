import aoc
from heapq import heappop, heappush

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 22, '6,1'

# Common
W, H, BYTES = (7, 7, 12) if aoc.is_test_mode() else (71, 71, 1024)
START_POS = (0, 0)
END_POS = (W - 1, H - 1)
coords = [tuple(map(int, line.split(','))) for line in lines]

def heuristic(x, y):
    return abs(x - END_POS[0]) + abs(y - END_POS[1])

def find_path(obstacles):
    queue = [(0, START_POS)]
    costs = {START_POS: 0}

    while queue:
        cost, pos = heappop(queue)
        x, y = pos
        if pos == END_POS:
            return cost

        for nx, ny in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                continue
            new_pos = (nx, ny)
            if new_pos in obstacles:
                continue
            new_cost = costs[pos] + 1

            if new_pos not in costs or new_cost < costs[new_pos]:
                costs[new_pos] = new_cost
                heappush(queue, (new_cost + heuristic(nx, ny), (nx, ny)))
    return 0

# Part 1
aoc.mark_task_start()
obstacles = set(coords[:BYTES])
result1 = find_path(obstacles)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
for i in range(BYTES, len(coords)):
    # Keep adding obstacles to the set from Part 1
    obstacles.add(coords[i])
    cost = find_path(obstacles)
    if not cost:
        result2 = f'{coords[i][0]},{coords[i][1]}'
        break
aoc.print_result(2, result2, exp2)
