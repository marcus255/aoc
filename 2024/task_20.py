import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 44, 285

grid = [list(line) for line in lines]
W, H = len(grid[0]), len(grid)

START_POS, END_POS = (0, 0), (0, 0)
for y in range(H):
    for x in range(W):
        if grid[y][x] == 'S':
            START_POS = (x, y)
        elif grid[y][x] == 'E':
            END_POS = (x, y)

def get_path_coords():
    path_coords = {START_POS: 0}
    x, y = START_POS
    i = 1
    while (x, y) != END_POS:
        for nx, ny in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                continue
            if grid[ny][nx] == '#':
                continue
            if (nx, ny) in path_coords:
                continue
            path_coords[(nx, ny)] = i
            x, y = nx, ny
            i += 1
            break
    return path_coords

def find_in_range(path_coords, pos, dist):
    x, y = pos
    in_range = set()
    for nx in range(x - dist, x + dist + 1):
        for ny in range(y - dist, y + dist + 1):
            new_pos = (nx, ny)
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                continue
            if new_pos not in path_coords:
                continue
            d = abs(nx - x) + abs(ny - y)
            if d > dist:
                continue
            in_range.add(new_pos)
    return in_range

def find_num_shortcuts(path_coords, max_len, req_shortcut):
    shortcuts = set()
    for (x, y), value in path_coords.items():
        in_range = find_in_range(path_coords, (x, y), max_len)
        for x2, y2 in in_range:
            # Avoid duplicates. (x, y, x2, y2) will be always added first
            if (x2, y2, x, y) in shortcuts:
                continue
            shortcut_len = abs(x - x2) + abs(y - y2)
            orig_len = abs(value - path_coords[(x2, y2)])
            if shortcut_len >= orig_len:
                continue
            shortened_by = orig_len - shortcut_len
            if shortened_by >= req_shortcut:
                shortcuts.add((x, y, x2, y2))
    return len(shortcuts)

# Part 1
aoc.mark_task_start()
SHORTCUT_LEN = 1 if aoc.is_test_mode() else 100
REQ_LEN = 2
path_coords = get_path_coords()
result1 = find_num_shortcuts(path_coords, REQ_LEN, SHORTCUT_LEN)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
SHORTCUT_LEN = 50 if aoc.is_test_mode() else 100
REQ_LEN = 20
result2 = find_num_shortcuts(path_coords, REQ_LEN, SHORTCUT_LEN)
aoc.print_result(2, result2, exp2)
