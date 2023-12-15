import aoc
import aoc_utils as utils
from functools import cache

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 136, 64

# Common
def sub_collapse_line(line, start, stop):
    loose_rocks = 0
    for i in range(start, stop):
        item = line[i]
        if item == 'O':
            loose_rocks += 1
            line[i] = '.'
    i = start
    while loose_rocks:
        if line[i] != '#':
            line[i] = 'O'
            loose_rocks -= 1
        i += 1
    return line

@cache
def collapse_line(line):
    line_len = len(line)
    tmp_line = list(line)
    start_i = 0
    while start_i < line_len:
        if tmp_line[start_i] == '#':
            start_i += 1
            continue
        try:
            end_i = tmp_line.index('#', start_i)
        except ValueError:
            end_i = line_len
        segment_len = end_i - start_i
        if end_i - start_i > 1:
            tmp_line = sub_collapse_line(tmp_line, start_i, end_i)
            if line_len != len(tmp_line):
                raise RuntimeError
        start_i += segment_len
    return tmp_line

def get_grid_load(grid):
    sum_rocks = 0
    for i, line in enumerate(grid):
        s = line.count('O') * (len(line) - i)
        sum_rocks += s
    return sum_rocks

def print_grid(grid, msg='Grid'):
    print(f'\n{msg}:')
    for line in grid:
        print(' '.join(line))

def find_repeating(array, pat_len):
    prev_i = pat_len
    seq_lens = []
    for i in range(pat_len, len(array)):
        if len(array[i:i+pat_len]) != len(array[:pat_len]):
            continue
        if array[i:i+pat_len] == array[:pat_len]:
            if prev_i != i:
                seq_lens.append(i - prev_i)
            prev_i = i
            if len(seq_lens) > 10:
                return max(seq_lens)
    return 0

# Part 1
aoc.mark_task_start()
current_grid = utils.rotated_2d_left(lines)
current_grid = [collapse_line(tuple(line)) for line in current_grid]
result1 = get_grid_load(utils.rotated_2d_right(current_grid))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
CYCLES = 1000_000_000
PATTERN_LEN = 50
PATTERN_OFFSET = 800
# print_grid(lines, 'Initial grid')
current_grid = utils.rotated_2d_left(lines)
subsums = []
repeat_found = False
cycle = 0

while cycle < CYCLES:
    for y in range(4):
        current_grid = [collapse_line(tuple(line)) for line in current_grid]
        current_grid = utils.rotated_2d_right(current_grid)

    grid_load = get_grid_load(utils.rotated_2d_right(current_grid))
    subsums.append(grid_load)

    if cycle > PATTERN_OFFSET and not repeat_found:
        seq_len = find_repeating(subsums[PATTERN_OFFSET:], PATTERN_LEN)
        if seq_len:
            repeat_found = True
            skip = ((CYCLES - cycle) // seq_len) * seq_len
            cycle += skip
    cycle += 1

current_grid = utils.rotated_2d_right(current_grid)
# print_grid(current_grid, 'Grid after all cycles')
result2 = subsums[-1]
aoc.print_result(2, result2, exp2)
