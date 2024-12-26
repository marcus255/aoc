import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1, 1

# Common
items = []
item = []
for line in lines:
    if line:
        item.append(line)
    else:
        items.append(item)
        item = []
items.append(item)

locks_keys = [[], []]
W, H = len(items[0][0]), len(items[0])
for item in items:
    lock_key = [-1] * W
    for y in range(H):
        for x in range(W):
            if item[y][x] == '#':
                lock_key[x] += 1
    locks_keys[0 if item[0] == '#####' else 1].append(lock_key)

def key_match_lock(key, lock):
    for k, l in zip(key, lock):
        if k + l > 5:
            return False
    return True

# Part 1
aoc.mark_task_start()
result1 = 0
for lock in locks_keys[0]:
    for key in locks_keys[1]:
        if key_match_lock(key, lock):
            result1 += 1
aoc.print_result(1, result1, exp1)

# No part 2
