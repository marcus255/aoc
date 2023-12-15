import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 80, 10

MOVES = {
    'F': {(0,-1): (1,0), (-1,0): (0,1)},
    '-': {(1,0): (1,0), (-1,0): (-1,0)},
    '7': {(1,0): (0,1), (0,-1): (-1,0)},
    '|': {(0,1): (0,1), (0,-1): (0,-1)},
    'J': {(0,1): (-1,0), (1,0): (0,-1)},
    'L': {(-1,0): (0,-1), (0,1): (1,0)},
}
H_reductions = {'-': '', 'L7': '|', 'FJ': '|'}
V_reductions = {'|': '', '7L': '-', 'FJ': '-'}

#  Algorithm for finding if element is inside the loop:
#    1. Skip positions that are part of the loop
#    2. For each position check if number of loop lines on each of 4 sides is odd
#      - when checking Left-Right neighbors, count number of '|' chars
#      - when checking Up-Down neighbors, count number of '-' chars
#    3. Some sequences can be reduced to '|' or '-' chars, e.g. 'L7' or even 'L---7' is in fact a '|',
#      when checking Left-Right neighbors
#   
#  Other examples of reductions:
#    Horizontal:   F-JFJ|L7|LJFJ  ->  |||||LJ|  => 8 loop lines => position not inside the loop
#    Vertical:     7|LFJ-FJ       ->  ----      => 8 loop lines => position not inside the loop
#    Vertical:     F||J           ->  -         => 1 loop line => position inside the loop
#   
#  Example examinations of points X, Y, Z:
#    .S-------7.
#    .|F-----7|.
#    .||.X...||.  ->  X have '||' on left and '||' on right => X outside the loop
#    .||.....||.
#    .|L-7ZF-J|.  ->  '|L7' can be reduced to '||', 'FJ|' can be reduced to '||' => Z outside the loop
#    .|.Y|.|..|.  ->  Y have '|' on left and '|||' on right => Y inside the loop 
#    .L--J.L--J.

START_MOVES = [(1,0), (-1,0), (0,1), (0,-1)]
WIDTH = len(lines[0])
HEIGHT = len(lines)

def find_start_position() -> ():
    for i, row in enumerate(lines):
        for col, _ in enumerate(row):
            if lines[i][col] == 'S':
                start = (col, i)
                break
    return start

def find_paths():
    steps_per_loop = {m: 1 for m in START_MOVES}
    path_per_loop = {m: [] for m in START_MOVES}

    for start_move in START_MOVES:
        position = (start_position[0] + start_move[0], start_position[1] + start_move[1])
        path_per_loop[start_move].append(position)
        move = start_move
        while position != start_position:
            c, r = position
            next_char = lines[r][c]
            # print(f'Position: {position}, Next char: {next_char}')
            if next_char == 'S':
                break
            try:
                move = MOVES[next_char][move]
            except KeyError:
                # print(f'No more moves for start {start_move}, char {next_char} move {move}')
                break
            position = (c + move[0], r + move[1])
            path_per_loop[start_move].append(position)
            steps_per_loop[start_move] += 1
    return steps_per_loop, path_per_loop

def find_valid_start_char(possible_moves):
    for char, move in MOVES.items():
        if set(possible_moves) == set(move.values()):
            return char

def replace_recursive(text, replacement_map):
    for a, b in replacement_map.items():
        while a in text:
            text = text.replace(a, b)
    return text

def find_H_bounds(row, col, left=True):
    pipes = []
    the_range = range(0, col) if left else range(col, WIDTH)
    for c in the_range:
        if lines[row][c] in MOVES.keys():
            pipes.append(lines[row][c])
    pipe_str = replace_recursive(''.join(pipes), H_reductions)
    # if len(pipes):
    #     print(f'H: {"".join(pipes)}  ->  {pipe_str}')
    return len(pipe_str)

def find_V_bounds(row, col, left=True):
    pipes = []
    the_range = range(0, row) if left else range(row, HEIGHT)
    for r in the_range:
        if lines[r][col] in MOVES.keys():
            pipes.append(lines[r][col])
    pipe_str = replace_recursive(''.join(pipes), V_reductions)
    # if len(pipes):
    #     print(f'V: {"".join(pipes)}  ->  {pipe_str}')
    return len(pipe_str)

def clear_fields_not_in_path(path):
    for row in range(HEIGHT):
        new_row_list = list(lines[row])
        for col in range(WIDTH):
            if (col, row) not in path:
                new_row_list[col] = '.'
        lines[row] = ''.join(new_row_list)

# Common
start_position = find_start_position()
# print(f'Starting at {start_position}')

# Part 1
aoc.mark_task_start()
steps_per_loop, path_per_loop = find_paths()
max_steps = max([s for s in steps_per_loop.values()])
result1 = max_steps // 2
# print(f'Valid path length: {max_steps}, farthest position: {result1}')
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
valid_start_moves = [move for move, step in steps_per_loop.items() if step == max_steps]
valid_start_char = find_valid_start_char(valid_start_moves)
# print(f'Valid start moves: {valid_start_moves}, valid start char: {valid_start_char}')

c, r = start_position
lines[r] = lines[r][:c] + valid_start_char + lines[r][c+1:]
valid_path = path_per_loop[valid_start_moves[0]]
# print(f'Valid path size: {len(valid_path)}')

clear_fields_not_in_path(valid_path)

tiles_inside = 0
for row in range(HEIGHT):
    for col in range(WIDTH):
        if (col, row) in valid_path:
            continue
        hl = find_H_bounds(row, col)
        hr = find_H_bounds(row, col, left=False)
        vl = find_V_bounds(row, col)
        vr = find_V_bounds(row, col, left=False)
        all_bounds_odd = hl % 2 and hr % 2 and vl % 2 and vr %2
        if all_bounds_odd:
            tiles_inside += 1
        # print(f'({row},{col}): {hl}, {hr}, {vl}, {vr} {"<-- MATCH" if all_bounds_odd else ""}')

result2 = tiles_inside
aoc.print_result(2, result2, exp2)

# for line in lines:
#     print(line)
