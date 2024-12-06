import aoc
from copy import deepcopy

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 41, 6

# Common
def find_guard_pos(area):
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] in ['v', '^', '<', '>']:
                return (i, j)
    raise Exception("Guard not found")

def find_routes(area, guard_pos, find_loops=False):
    visited = set()
    (i, j) = guard_pos
    rotation = area[i][j]
    while True:
        area[i][j] = 'X'
        while True:
            dir = dirs[rotation]
            ni, nj = i + dir[0], j + dir[1]
            if any([ni < 0, nj < 0, ni >= len(area), nj >= len(area[0])]):
                if find_loops:
                    return None, False
                return sum(row.count('X') for row in area), None
            if area[ni][nj] != '#':
                break
            rotation = rotations[rotation]
        i, j = ni, nj
        if find_loops and (i, j, dir) in visited:
            return None, True
        else:
            visited.add((i, j, dir))

dirs = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }
rotations = { '^': '>', 'v': '<', '<': '^', '>': 'v' }
orig_area = []
for line in lines:
    orig_area.append(list(line))
guard_pos = find_guard_pos(orig_area)


# Part 1
aoc.mark_task_start()
visited, _ = find_routes([x[:] for x in orig_area], guard_pos)
result1 = visited
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
looping_positions = 0
global cache
cache = {}
for i in range(len(orig_area)):
    for j in range(len(orig_area[0])):
        area = [x[:] for x in orig_area]
        curr = area[i][j]
        if curr == '.':
            area[i][j] = '#'
            _, looped = find_routes(area, guard_pos, find_loops=True)
            looping_positions += (1 if looped else 0)

result2 = looping_positions
aoc.print_result(2, result2, exp2)
