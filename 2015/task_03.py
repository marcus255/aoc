import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 2, 11

# Common
dirs = lines[0]
DIRS = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
START = (0, 0)

# Part 1
aoc.mark_task_start()
unique = {START}
pos = START
for d in dirs:
    pos = (pos[0] + DIRS[d][0], pos[1] + DIRS[d][1])
    unique.add(pos)
result1 = len(unique)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
unique = {START}
pos1 = pos2 = START
for i, d in enumerate(dirs):
    pos = pos1 if i % 2 == 0 else pos2
    new_pos = (pos[0] + DIRS[d][0], pos[1] + DIRS[d][1])
    if i % 2 == 0:
        pos1 = new_pos
    else:
        pos2 = new_pos
    unique.add(new_pos)
result2 = len(unique)
aoc.print_result(2, result2, exp2)
