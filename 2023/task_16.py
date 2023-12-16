import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 46, 51

# Common
grid = lines
H, W = len(grid), len(grid[0])
m = {
    'U': lambda r, c: (r - 1, c,     -1,  0),
    'D': lambda r, c: (r + 1, c,      1,  0),
    'L': lambda r, c: (r,     c - 1,  0, -1),
    'R': lambda r, c: (r,     c + 1,  0,  1),
}
m['LR'] = [m['L'], m['R']]
m['UD'] = [m['U'], m['D']]
LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)
transition_map = {
# from-to:  left -> right   right -> left  up -> down     down -> up
    '/':  { RIGHT: m['U'],  LEFT: m['D'],  DOWN: m['L'],  UP: m['R']  },
    '\\': { RIGHT: m['D'],  LEFT: m['U'],  DOWN: m['R'],  UP: m['L']  },
    '|':  { RIGHT: m['UD'], LEFT: m['UD'], DOWN: m['D'],  UP: m['U']  },
    '-':  { RIGHT: m['R'],  LEFT: m['L'],  DOWN: m['LR'], UP: m['LR'] },
    '.':  { RIGHT: m['R'],  LEFT: m['L'],  DOWN: m['D'],  UP: m['U']  },
}

def get_energized_tiles(start_pos_dir, positions_dirs=None):
    if not positions_dirs:
        positions_dirs = set()
    new_pos_dirs = []
    new_pos_dir = start_pos_dir

    while not new_pos_dir in positions_dirs:
        r, c, rdir, cdir = new_pos_dir
        if r >= H or r < 0 or c >= W or c < 0:
            # print(f'Outside the grid: ({r}, {c})')
            break
        positions_dirs.add(new_pos_dir)
        tile_char = grid[r][c]
        transitions = transition_map[tile_char][(rdir, cdir)]
        if not isinstance(transitions, list):
            new_pos_dir = transitions(r, c)
        else:
            new_pos_dir = transitions[0](r, c)
            new_pos_dirs.append(transitions[1](r, c))

    # print(f'({r}, {c}, {rdir}, {cdir}) already in path')
    for new_pos_dir in new_pos_dirs:
        if not new_pos_dir in positions_dirs:
            get_energized_tiles(new_pos_dir, positions_dirs)

    return positions_dirs

# Part 1
aoc.mark_task_start()
tiles = get_energized_tiles((0, 0, 0, 1))
coords = set([(r, c) for r, c, *_ in tiles])
result1 = len(coords)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
# get all starting position with respective light directions
start_dirs = []
for r in range(H):
    start_dirs.append((r, 0, 0, 1))
    start_dirs.append((r, H - 1, 0, -1))
for c in range(W):
    start_dirs.append((0, c, 1, 0))
    start_dirs.append((W - 1, c, -1, 0))

results = []
for start in start_dirs:
    tiles = get_energized_tiles(start)
    coords = set([(r, c) for r, c, *_ in tiles])
    results.append(len(coords))
    # print(f'start: {start}, len: {len(coords)}')

result2 = sorted(results)[-1]
aoc.print_result(2, result2, exp2)









