import aoc
import re
from collections import deque

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 330, 286

# Common
# Input lines look like this:
# Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
r = re.compile(r'(?P<src>[A-Za-z]+) would (?P<action>[a-z]+) (?P<amount>\d+) happiness units by sitting next to (?P<dst>[A-Za-z]+)\.')

distances = {}
names = []
for line in lines:
    src, action, amount, dst = r.match(line).groups()
    names.append(src)
    value = int(amount) if action == 'gain' else -int(amount)
    key = tuple(sorted((src, dst)))
    distances.setdefault(key, 0)
    distances[key] += value
names = list(set(names))

def get_highest_score(names, distances):
    queue = deque([(0, [names[0]])])
    best = 0
    while queue:
        distance, visited = queue.popleft()
        first, last = visited[0], visited[-1]
        if len(visited) == len(names) + 1 and first == last:
            best = max(best, distance)
            continue
        if len(visited) > len(names):
            continue
        for n in names:
            if n == last:
                continue
            if n in visited and len(visited) != len(names):
                continue
            next_hop = distances[tuple(sorted([last, n]))]
            queue.append((distance + next_hop, visited + [n]))
    return best

# Part 1
aoc.mark_task_start()
result1 = get_highest_score(names, distances)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
extra = 'Snowman'
for name in names:
    distances[tuple(sorted([name, extra]))] = 0
names.append(extra)
result2 = get_highest_score(names, distances)
aoc.print_result(2, result2, exp2)
