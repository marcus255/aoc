import aoc
from collections import deque
from functools import cache

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 94, 154

# Common
NO_MOVE, LEFT, RIGHT, UP, DOWN = (0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)
moves = [UP, DOWN, LEFT, RIGHT]
slopes = {UP: '^', DOWN: 'v', LEFT: '<', RIGHT: '>'}
grid = [[x for x in line] for line in lines]
H, W = len(grid), len(grid[0])

def find_new_pos(grid, pos, seen, use_slopes=True):
    new_positions = []
    for mr, mc in moves:
        r, c = pos[0] + mr, pos[1] + mc
        if not (0 <= r < H and 0 <= c < W):
            continue
        if grid[r][c] == '#' or (r, c) in seen:
            continue
        if use_slopes and grid[r][c] in '^v<>' and grid[r][c] != slopes[(mr, mc)]:
            continue
        new_positions.append((r, c))
    return new_positions

@cache
def find_shortcut(prev, curr):
    sh_len = 0
    while True:
        next_pos = find_new_pos(grid, curr, [prev], False)
        if len(next_pos) != 1:
            break
        prev = curr
        curr = next_pos[0]
        sh_len += 1
    # print(f'{prev} -> {curr}: {sh_len}')
    return prev, curr, sh_len

def find_max_len_path(grid, use_slopes=True):
    START_POS, PREV_POS, PATH_LEN = (0, 1), (-1, 1), 0
    END_POS = (H - 1, W - 2)
    q = deque()
    q.append((START_POS, [PREV_POS], PATH_LEN))
    longest_path = 0

    while len(q):
        start, seen, path_len = q.popleft()
        prev, curr, sh_len = find_shortcut(seen[-1], start)
        if sh_len:
            if curr in seen:
                continue
            # print(f'{seen[-1]}, {initial_pos} -> {prev}, {curr}: {sh_len}')
            seen = seen + [prev]
            start = curr
        next = [curr] if curr == END_POS else find_new_pos(grid, start, seen, use_slopes)

        for n in next:
            cur_len = path_len + 1 + sh_len
            # print(f'Len: {path_len + 1}')
            if n == END_POS:
                if cur_len > longest_path:
                    longest_path = cur_len
                    # print(f'Longest: {longest_path}')
                continue
            q.appendleft((n, seen + [start], cur_len))
    return longest_path - 1

# Part 1
aoc.mark_task_start()
result1 = find_max_len_path(grid, use_slopes=True)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = find_max_len_path(grid, use_slopes=False)
aoc.print_result(2, result2, exp2)
