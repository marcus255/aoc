import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1 = 13140
exp_crt = '''
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
'''.strip()
exp2 = exp_crt.count('#')


# Common
ops = [(op, int(val)) for op, val in [line.split(' ') if ' ' in line else (line, 0) for line in lines]]
check_cycles = [20, 60, 100, 140, 180, 220]

# Part 1
aoc.mark_task_start()
cycle, x = 0, 1
for op, val in ops:
    cycle_inc = 1 if op == 'noop' else 2
    for _ in range(cycle_inc):
        cycle += 1
        if cycle in check_cycles:
            result1 += cycle * x
    if op == 'addx':
        x += val
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
cycle, x = 0, 1
crt, current_row = [], []
for op, val in ops:
    sprite = [x - 1, x, x + 1]
    cycle_inc = 1 if op == 'noop' else 2
    for _ in range(cycle_inc):
        current_row.append('#' if cycle % 40 in sprite else '.')
        cycle += 1
        if cycle % 40 == 0:
            crt.append(current_row)
            current_row = []
    if op == 'addx':
        x += val

# For the task input, CRT should print out 'FZBPBFZF' text
# for row in crt:
#     print(''.join('█' if char == '#' else char for char in row))

# As a result, copmare the number of '#' in the CRT with the expected result
result2 = ''.join([''.join(row) for row in crt]).count('#')

aoc.print_result(2, result2, exp2)
