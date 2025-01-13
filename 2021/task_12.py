import aoc
from collections import deque, Counter
from functools import cache

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 226, 3509

connections : dict[str: list[str]] = {}
# Common
for line in lines:
    a, b = line.split('-')
    connections.setdefault(a, []).append(b)
    connections.setdefault(b, []).append(a)

# Part 1
aoc.mark_task_start()
all_paths = []
queue = deque([('start', tuple())])
while queue:
    current, cur_path = queue.popleft()
    if current == 'end':
        all_paths.append(cur_path)
        continue
    for next in connections[current]:
        if next.islower() and next in cur_path:
            continue
        queue.append((next, cur_path + (current,)))
result1 = len(all_paths)
aoc.print_result(1, result1, exp1)

@cache
def any_visited_twice(visited):
    for k, v in Counter(visited).most_common():
        if k.islower() and v == 2:
            return True
    return False

def count_small_visited_twice(visited):
    visited_twice = 0
    for k, v in Counter(visited).most_common():
        if k.islower() and v == 2:
            visited_twice += 1
    return visited_twice

# Part 2
aoc.mark_task_start()
all_paths = []
queue = deque([('start', tuple())])
while queue:
    current, cur_path = queue.popleft()
    if current == 'end':
        all_paths.append(cur_path)
        continue
    for next in connections[current]:
        if next == 'start':
            continue
        if next.islower():
            if cur_path.count(next) == 2:
                continue
            if cur_path.count(next) == 1 and any_visited_twice(cur_path):
                continue              
        queue.append((next, cur_path + (current,)))

# For some reason, some results have more that one small cave visited twice.
# Filter these entries out
all_paths = list(filter(lambda x: count_small_visited_twice(x) <= 1, all_paths))
result2 = len(all_paths)
aoc.print_result(2, result2, exp2)
