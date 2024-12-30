import aoc
import re
from heapq import heappush, heappop

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1651, 1

# Common
# Lines may look like this:
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve HH has flow rate=22; tunnel leads to valve GG
r = re.compile(r'Valve (?P<valve>[A-Z]+) has flow rate=(?P<flow>\d+); tunnel[s]? lead[s]? to valve[s]? (?P<dst>.+)')
valves = {}
for line in lines:
    m = r.match(line)
    valves[m.group('valve')] = (int(m.group('flow')), m.group('dst').split(', '))

# Part 1
aoc.mark_task_start()

aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()

aoc.print_result(2, result2, exp2)
