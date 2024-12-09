import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1928, 2858

# Common
line = list(map(int, list(lines[0])))
disk = []
files = []
empty_spaces = []
for i in range(len(line)):
    size = line[i]
    file_id = i // 2
    position = len(disk)
    if i % 2 == 0:
        files.append((file_id, position, size))
        disk += [file_id for _ in range(line[i])]
    else:
        empty_spaces.append((position, size))
        disk += [None for _ in range(line[i])]

# Part 1
# desc:    2333133121414131402
# input:   00...111...2...333.44.5555.6666.777.888899
# output:  0099811188827773336446555566..............
aoc.mark_task_start()
index = 0
defrag_disk = []
for i in range(len(disk) - 1, 0, -1):
    if i <= index:
        defrag_disk.append(disk[i])
        break
    if disk[i] is not None:
        while disk[index] is not None:
            defrag_disk.append(disk[index])
            index += 1
        defrag_disk.append(disk[i])
        index += 1

sum = 0
for i, val in enumerate(defrag_disk):
    if val is not None:
        sum += val * i

result1 = sum
aoc.print_result(1, result1, exp1)

# Part 2
# desc:    2333133121414131402
# input :  00...111...2...333.44.5555.6666.777.888899
# step 1:  0099.111...2...333.44.5555.6666.777.8888..
# step 2:  0099.1117772...333.44.5555.6666.....8888..
# step 3:  0099.111777244.333....5555.6666.....8888..
# step 4:  00992111777.44.333....5555.6666.....8888..
aoc.mark_task_start()
reallocated = []
for i in range(len(files) - 1, 0, -1):
    id, pos, size = files[i]
    for j in range(len(empty_spaces)):
        space_pos, space_size = empty_spaces[j]
        if space_pos >= pos:
            continue
        if space_size >= size:
            reallocated.append((id, space_pos, size))
            if space_size > size:
                empty_spaces[j] = (space_pos + size, space_size - size)
            else:
                empty_spaces.remove((space_pos, space_size))
            files.remove((id, pos, size))
            break

files = sorted(files + reallocated, key=lambda x: x[1])
sum = 0
for id, pos, size in files:
    for s in range(size):
        sum += id * (pos + s)

result2 = sum
aoc.print_result(2, result2, exp2)
