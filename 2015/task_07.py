import aoc
from functools import cache

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 65079, 1

ops = {
    'OR': lambda x, y: x | y,
    'AND': lambda x, y: x & y,
    'RSHIFT': lambda x, y: (x >> y) & 0xffff,
    'LSHIFT': lambda x, y: (x << y) & 0xffff,
    'NOT': lambda x, y: ~x & 0xffff,
    None: lambda x, y: x
}

# Common
wires = {}
for line in lines:
    src, dst = line.split(' -> ')
    values = src.split(' ')
    in_1 = in_2 = op = None
    if len(values) == 1:
        in_1 = values[0]
    elif len(values) == 2:
        op, in_1 = values
    elif len(values) == 3:
        in_1, op, in_2 = values
    else:
        print(line, values)
        raise ValueError()
    wires[dst] = (in_1, op, in_2)

@cache
def get_value(wire):
    if not wire:
        return 0
    if isinstance(wire, int):
        return wire
    in_1, op, in_2 = wires[wire]
    in_1 = int(in_1) if in_1.isdigit() else get_value(in_1)
    in_2 = int(in_2) if in_2 and in_2.isdigit() else in_2
    return ops[op](get_value(in_1), get_value(in_2)) if op else in_1

# Part 1
aoc.mark_task_start()
wire = 'i' if aoc.is_test_mode() else 'a'
result1 = get_value(wire)
aoc.print_result(1, result1, exp1)

# Part 2
if not aoc.is_test_mode():
    aoc.mark_task_start()
    get_value.cache_clear()
    wires['b'] = (str(result1), None, None)
    result2 = get_value('a')
    aoc.print_result(2, result2, exp2)
