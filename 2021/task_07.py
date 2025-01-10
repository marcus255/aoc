import aoc
from functools import cache

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 37, 168

# Common
numbers = sorted(list(map(int, lines[0].split(','))))

@cache
def geometric_distance(n):
    return sum(range(1, n + 1))

def get_cost_geom(numbers, value):
    return sum(map(lambda x: geometric_distance(abs(x - value)), numbers))

def get_cost(numbers, value):
    return sum(map(lambda x: abs(x - value), numbers))

def find_min(numbers, min_cost, cost_function=get_cost):
    for i in range(min(numbers), max(numbers)):
        cost = cost_function(numbers, i)
        if cost > min_cost:
            return min_cost
        min_cost = min(min_cost, cost)

# Part 1
aoc.mark_task_start()
result1 = find_min(numbers, float('inf'))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = find_min(numbers, float('inf'), cost_function=get_cost_geom)
aoc.print_result(2, result2, exp2)
