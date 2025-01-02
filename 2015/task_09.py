import aoc
from heapq import heappop, heappush

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 605, 982

# Common
distances = {}
connections = {}
for line in lines:
    srcdst, dist = line.split(' = ')
    src, dst = srcdst.split(' to ')
    distances.update({(src, dst): int(dist)})
    distances.update({(dst, src): int(dist)})
    connections.setdefault(src, []).append(dst)
    connections.setdefault(dst, []).append(src)

def find_path(start, shortest=True):
    queue = [(0, start, set([start]))]
    while queue:
        distance, city, visited = heappop(queue)
        if len(visited) == len(connections):
            return distance if shortest else -distance
        for new_city in connections[city]:
            if new_city not in visited:
                next_hop = distances[(city, new_city)]
                new_distance = distance + (next_hop if shortest else -next_hop)
                heappush(queue, (new_distance, new_city, visited | set([new_city])))

# Part 1
aoc.mark_task_start()
result1 = min([find_path(city) for city in connections])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = max([find_path(city, shortest=False) for city in connections])
aoc.print_result(2, result2, exp2)
