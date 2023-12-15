import aoc
import itertools
from functools import cache

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 21, 525152

# Common
all_chars = []
all_sizes = []
for line in lines:
    chars, sizes = line.split(' ')
    sizes = [int(x) for x in sizes.split(',')]
    all_chars.append(chars)
    all_sizes.append(sizes)

@cache
def get_broken_spring_lengths(row):
    sizes = []
    broken_spring = False
    size = 0
    for c in row:
        if c == '#':
            if not broken_spring and size == 0:
                broken_spring = True
                size += 1
            elif broken_spring:
                size +=1
        elif c == '.' and size != 0:
            sizes.append(size)
            broken_spring = False
            size = 0
    if size != 0:
        sizes.append(size)
    return sizes

CACHE = {}
def get_num_solutions(chars, sizes, group_index=0):
    if len(chars) == 0:
        # Verify if all groups are completed
        return len(sizes) == 0 and group_index == 0
    
    key = (chars, sizes, group_index)
    if key in CACHE:
        return CACHE[key]
    
    solutions = 0
    next_char = chars[0]
    if next_char in ['?', '#']:
        # Keep adding to current group
        solutions += get_num_solutions(chars[1:], sizes, group_index + 1)

    # Action for '?' executed second time to branch
    if next_char in ['?', '.']:
        if group_index == 0:
            # No group processing, continue
            solutions += get_num_solutions(chars[1:], sizes)
        elif len(sizes) and sizes[0] == group_index:
            # Processing group, verify if it is complete
            solutions += get_num_solutions(chars[1:], sizes[1:])

    CACHE[key] = solutions
    return solutions

# Part 1
aoc.mark_task_start()
total_solutions = 0
for chars, sizes in zip(all_chars, all_sizes):
    num_solutions = get_num_solutions(chars + '.', tuple(sizes))
    total_solutions += num_solutions
result1 = total_solutions
aoc.print_result(1, result1, exp1)

# Part 2
# Functional programming, recursively invoke the function
aoc.mark_task_start()

total_solutions = 0
for chars, sizes in zip(all_chars, all_sizes):
    chars = '?'.join([chars for _ in range(5)])
    sizes_copy = sizes[:]
    for x in range(4):
        sizes.extend(sizes_copy)

    num_solutions = get_num_solutions(chars + '.', tuple(sizes))
    total_solutions += num_solutions

result2 = total_solutions
aoc.print_result(2, result2, exp2)

# Part 1
#   ???.### 1,1,3               - 1
#   .??..??...?##. 1,1,3        - 4
#   ?#?#?#?#?#?#?#? 1,3,1,6     - 1
#   ????.#...#... 4,1,1         - 1
#   ????.######..#####. 1,6,5   - 4
#   ?###???????? 3,2,1          - 10

# Part 2
#   ???.### 1,1,3               - 1
#   .??..??...?##. 1,1,3        - 16384
#   ?#?#?#?#?#?#?#? 1,3,1,6     - 1
#   ????.#...#... 4,1,1         - 16
#   ????.######..#####. 1,6,5   - 2500
#   ?###???????? 3,2,1          - 506250
