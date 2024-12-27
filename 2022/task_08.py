from functools import reduce
import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 21, 8

# Common
rows = [list(map(int, line)) for line in lines]
cols = list(zip(*rows))
row_maxes = [max(row) for row in rows]
col_maxes = [max(col) for col in cols]

def get_visible(rows, maxes, rotated=False, ltr=True):
    visible = set()
    for y, row in enumerate(rows):
        first_index = 0 if ltr else len(row) - 1
        current_max = row[first_index]
        visible.add((first_index, y))
        iter_range = range(0, len(row)) if ltr else range(len(row) - 1, -1, -1)
        for x in iter_range:
            c = row[x]
            if c == maxes[y]:
                visible.add((x, y))
                break
            if c > current_max:
                visible.add((x, y))
                current_max = c
    return ((x, y) if not rotated else (y, x) for x, y in visible)

def get_largest_dist(row, pos):
    tree = row[pos]
    line = row[pos+1:]
    for i, c in enumerate(line):
        if c >= tree:
            return i + 1
    return len(line)

def fill_distances(distances, rows, rotated=False):
    for y in range(1, len(rows) - 1):
        for x in range(1, len(rows[0]) - 1):
            coord = (x, y) if not rotated else (y, x)
            if coord not in distances:
                distances[coord] = []
            distances[coord].append(get_largest_dist(rows[y], x))
            distances[coord].append(get_largest_dist(rows[y][::-1], len(rows[y]) - x - 1))

# Part 1
aoc.mark_task_start()
visible = set()
visible.update(get_visible(rows, row_maxes))
visible.update(get_visible(rows, row_maxes, ltr=False))
visible.update(get_visible(cols, col_maxes, rotated=True))
visible.update(get_visible(cols, col_maxes, rotated=True, ltr=False))
result1 = len(visible)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
distances = {}
fill_distances(distances, rows)
fill_distances(distances, cols, rotated=True)
result2 = max([reduce(lambda x, y: x * y, dists) for dists in distances.values()])
aoc.print_result(2, result2, exp2)
