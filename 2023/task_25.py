import aoc
import networkx
import random

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 54, 1

# Common
modules = {}
graph = networkx.Graph()
for line in lines:
    left, right = line.split(': ')
    if left not in modules:
        modules[left] = set()
    for r in right.split(' '):
        if r not in modules:
            modules[r] = set()
        if left not in modules:
            modules[left] = set()
        graph.add_edge(left, r, capacity=1.0)
        modules[left].add(r)
        modules[r].add(left)

aoc.mark_task_start()
while True:
    module1 = random.choice(list(modules.keys()))
    module2 = random.choice(list(modules.keys()))
    min_cut, parts = networkx.minimum_cut(graph, module1, module2)
    if min_cut == 3:
        break
result1 = len(parts[0]) * len(parts[1])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()

# aoc.print_result(2, result2, exp2)
