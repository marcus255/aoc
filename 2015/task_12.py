import aoc
import json

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 3, 4

# Common
input = json.loads(lines[0])

def count_numbers(input, avoid=None):
    if isinstance(input, int):
        return input
    elif isinstance(input, list):
        return sum([count_numbers(i, avoid) for i in input])
    elif isinstance(input, dict):
        if avoid and avoid in input.values():
            return 0
        return sum([count_numbers(i, avoid) for i in input.values()])
    return 0

# Part 1
aoc.mark_task_start()
result1 = count_numbers(input)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
if aoc.is_test_mode():
    input = json.loads('[1,{"c":"red","b":2},3]')
result2 = count_numbers(input, avoid='red')
aoc.print_result(2, result2, exp2)
