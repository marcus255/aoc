import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 10092, 9021

# Common
dirs = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
original_grid = []
moves = ''
grid_lines = True
for line in lines:
    if not line:
        grid_lines = False
        continue
    if grid_lines:
        original_grid.append(list(line))
    else:
        moves += line

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def get_position(grid, cell):
    for y, row in enumerate(grid):
        if cell in row:
            return (row.index(cell), y)

def find_walls(line):
    return set([i for i, c in enumerate(line) if c == '#'])

def try_move(grid, move, pos, part2=False):
    x, y = pos
    i, j = dirs[move]
    new_x, new_y = x + i, y + j
    obstacle = grid[new_y][new_x]

    if obstacle == '#':
        return False

    if obstacle in ['[', ']', 'O']:
        if move in ['<', '>']:
            if not try_move(grid, move, (x + i, y), part2):
                return False
        elif move in ['^', 'v']:
            pos2 = (x + 1, y + j) if obstacle == '[' else (x - 1, y + j)
            r2 = try_move(grid, move, pos2, part2) if part2 else True
            r1 = try_move(grid, move, (x, y + j), part2)
            if not r1 or not r2:
                return False

    grid[new_y][new_x] = grid[y][x]
    grid[y][x] = '.'
    return True

# Part 1
aoc.mark_task_start()
grid = [x[:] for x in original_grid]

for move in moves:
    pos = get_position(grid, '@')
    tmp_grid = [x[:] for x in grid]
    status = try_move(tmp_grid, move, pos, part2=False)
    if status:
        grid = tmp_grid

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == 'O':
            result1 += 100 * y + x

aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
grid = []
expansion = {'#': ['#', '#'], 'O': ['[', ']'], '.': ['.', '.'], '@': ['@', '.']}
for line in original_grid:
    new_line = []
    for c in line:
        new_line += expansion[c]
    grid.append(new_line)

for move in moves:
    pos = get_position(grid, '@')
    tmp_grid = [x[:] for x in grid]
    status = try_move(tmp_grid, move, pos, part2=True)
    if status:
        grid = tmp_grid

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == '[':
            result2 += 100 * y + x

aoc.print_result(2, result2, exp2)
