import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 152, 301

# Common
monkeys = {}
ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}
for line in lines:
    monkey, rest = line.split(': ')
    monkeys[monkey] = int(rest) if rest.isdigit() else (rest.split(' '))

def get_result(monkey):
    values = monkeys[monkey]
    if isinstance(values, int):
        return values
    a, op, b = values
    return ops[op](get_result(a), get_result(b))

# Part 1
aoc.mark_task_start()
result1 = get_result('root')
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
child_1, _, child_2 = monkeys['root']
# Inspecting the output shows, that value for child_2 is not affected by changes of 'humn'
# Hence, we only need to verify the value of child_1 after changing 'humn'
# Also, the output shows that the value of child_1 is increasing with increasing 'humn'
monkeys['humn'] = 0
num1 = get_result(child_1)
num2 = get_result(child_2)
prev_diff = 0
# Start from some large increment and then narrow down
inc = 10 ** 20
i = 0
while num1 != num2:
    i += inc
    monkeys['humn'] = i
    num1 = get_result(child_1)
    diff = abs(num1 - num2)
    # The lower the diff, the closer we are to the goal
    if diff > prev_diff:
        # If we start to drift further from the goal, reverse the direction and reduce increment
        inc = -inc // 10
    prev_diff = diff
result2 = i
aoc.print_result(2, result2, exp2)
