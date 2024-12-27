import aoc
from collections import deque

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 95437, 24933642

# Common
current_path = deque([])
unique_paths = set()
files = {}
for line in lines:
    if '$ cd ' in line:
        dir_name = line[5:]
        if dir_name == '..':
            current_path.pop()
        else:
            current_path.append(dir_name)
            unique_paths.add(tuple(current_path))
    elif line.startswith('dir ') or '$ ls' in line:
        pass
    else:
        size, file_name = line.split(' ')
        filepath = tuple(current_path) + (file_name,)
        files[filepath] = int(size)

dir_sizes = {}
for dirpath in unique_paths:
    dir_sizes[dirpath] = sum([size for filepath, size in files.items() if filepath[:len(dirpath)] == dirpath])

# Part 1
aoc.mark_task_start()
result1 = sum(filter(lambda x: x <= 100_000, dir_sizes.values()))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
TOTAL_SPACE = 70_000_000
REQ_FREE_SPACE = 30_000_000
space_left = TOTAL_SPACE - dir_sizes[('/',)]
space_needed = REQ_FREE_SPACE - space_left
dirs_sorted = sorted(dir_sizes.items(), key=lambda x: x[1])

for _, dirsize in dirs_sorted:
    if dirsize >= space_needed:
        result2 = dirsize
        break

aoc.print_result(2, result2, exp2)
