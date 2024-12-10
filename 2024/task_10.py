import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 36, 81

# Common
grid = [list(map(int, list(line))) for line in lines]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
all_paths = set()
unique_ends = set()

def get_path_count(grid, path, ends):
    valid_paths = 0
    if len(path) == 10:
        ends.add(path[-1])
        return 1
    i, j = path[-1]
    value = grid[i][j]
    for d in dirs:
        new_i, new_j = i + d[0], j + d[1]
        if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
            continue
        if (new_i, new_j) in path:
            continue
        if grid[new_i][new_j] - value == 1:
            count = get_path_count(grid, path + [(new_i, new_j)], ends)
            valid_paths += count
    return valid_paths

# Part 1
aoc.mark_task_start()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != 0:
            continue
        unique_ends = set()
        result2 += get_path_count(grid, [(i, j)], unique_ends)
        result1 += len(unique_ends)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
aoc.print_result(2, result2, exp2)
