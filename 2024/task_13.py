import aoc
import re
from itertools import product

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 480, 875318608908

# Common
rules = []
rules2 = []
additional = 10000000000000
A_COST, B_COST = 3, 1

rule = {}
coord_re = re.compile(r'Button ([AB]): X\+(\d+), Y\+(\d+)')
prize_re = re.compile(r'Prize: X=(\d+), Y=(\d+)')
for line in lines:
    if re.match(coord_re, line):
        label, x, y = re.match(coord_re, line).groups()
        rule[label.lower()] = (int(x), int(y))
    elif re.match(prize_re, line):
        x, y = re.match(prize_re, line).groups()
        x, y = int(x), int(y)
        rule['p'] = (x, y)
        rules.append(rule)
        rule2 = rule.copy()
        rule2['p'] = (x + additional, y + additional)
        rules2.append(rule2)
        rule = {}

# inefficient way, works only for part 1
def find_num_moves(rule):
    ax, ay = rule['a']
    bx, by = rule['b']
    px, py = rule['p']
    for i, j in product(range(100), range(100)):
        prize_x = ax * i + bx * j
        prize_y = ay * i + by * j
        if prize_x == px and prize_y == py:
            return i, j
    return None

# Part 1
aoc.mark_task_start()
for rule in rules:
    moves = find_num_moves(rule)
    if moves:
        i, j = moves
        result1 += i * A_COST + j * B_COST
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
rules = rules2
for rule in rules:
    ax, ay = rule['a']
    bx, by = rule['b']
    px, py = rule['p']
    # Solution for linear equations with 2 variables and 2 equations
    m = (px*by - py*bx) / (ax*by - ay*bx)
    n = (px - ax*m) / bx

    # If m and n are integers, it means that lines intersect in a point
    if m.is_integer() and n.is_integer():
        result2 += int(m) * A_COST + int(n) * B_COST

aoc.print_result(2, result2, exp2)
