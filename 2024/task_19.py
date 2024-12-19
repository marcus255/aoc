import aoc
from functools import cache

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 6, 16

# Common
patterns = lines[0].split(', ')
designs = lines[2:]

@cache
def is_design_valid(design):
    if design == '':
        return True
    for i in range(len(design) + 1):
        if design[:i] in patterns and is_design_valid(design[i:]):
            return True
    return False

@cache
def get_valid_combinations(design):
    if design == '':
        return 1
    valid = 0
    for i in range(len(design) + 1):
        if design[:i] in patterns:
            valid += get_valid_combinations(design[i:])
    return valid

# Part 1
aoc.mark_task_start()
result1 = sum([is_design_valid(design) for design in designs])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = sum([get_valid_combinations(design) for design in designs])
aoc.print_result(2, result2, exp2)
