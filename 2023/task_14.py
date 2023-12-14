import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 136, 64

# Common


def sub_collapse_line(line, start, stop):
    loose_rocks = 0
    # print(f'sub: {line}')
    for i in range(start, stop):
        item = line[i]
        if item == 'O':
            loose_rocks += 1
            line[i] = '.'
    i = start
    while loose_rocks:
        if line[i] != '#':
            line[i] = 'O'
            loose_rocks -= 1
        i += 1
    # print(f'sub: {line}')
    return line

def collapse_line(line):
    line_len = len(line)
    start_i = 0
    while start_i < line_len:
        if line[start_i] == '#':
            start_i += 1
            continue
        try:
            end_i = line.index('#', start_i)
        except ValueError:
            end_i = line_len
        segment_len = end_i - start_i
        # print(start_i, end_i)
        if end_i - start_i > 1:
            line = sub_collapse_line(line, start_i, end_i)
            if line_len != len(line):
                raise RuntimeError
        start_i += segment_len
        # break
    return line

def get_line_load(line):
    load = 0
    for i, item in enumerate(line):
        if item == 'O':
            load += (len(line) - i)
    return load

# Part 1


# rotated_grid = list(zip(*lines))
# rotated_grid = [list(line) for line in rotated_grid]


# total_load = 0
# for line in rotated_grid:
#     # print(f'\nLine {line}')
#     line = collapse_line(line)
#     # print(f'     {line}')
#     total_load += get_line_load(line)
#     # break

# result1 = total_load
aoc.print_result(1, result1, exp1)

# Part 2
CYCLES = 1000_000_000
# CYCLES = 3
print(f'\n Initial grid')
for l in lines:
    print(' '.join(l))
# Rotating left
rotated_grid = list(zip(*lines))[::-1]
rotated_grid = [list(line) for line in rotated_grid]
total_load = 0
subsums = []


done = False
tries = 0
x = 0
while x < CYCLES:
    for y in range(4):
        for ii, line in enumerate(rotated_grid):
            line = collapse_line(line)
        # Rotating right
        rotated_grid = list(zip(*rotated_grid[::-1]))
        rotated_grid = [list(line) for line in rotated_grid]


    sum_rocks = 0
    tmp_grid = list(zip(*rotated_grid[::-1]))
    # print(f'\n grid at ({x})')
    # for l in tmp_grid:
    #     print(' '.join(l))
    for i, line in enumerate(tmp_grid):
        s= line.count('O') * (len(line) - i)
        sum_rocks += s
    #     print(f'{i}: row load {s}, count {line.count("O")}')
    # print(f'Sum: {sum_rocks}')
    subsums.append(sum_rocks)

    num = 10
    offset = 800
    pat_len = 50
    subarr = subsums[offset:]
    prev_i = pat_len
    seq_lens = []
    if x > offset and not done:
        for i in range(pat_len, len(subarr)):
            if len(subarr[i:i+pat_len]) != len(subarr[:pat_len]):
                continue
            if not done and subarr[i:i+pat_len] == subarr[:pat_len]:
                if prev_i != i:
                    print(i - prev_i)
                    seq_lens.append(i - prev_i)
                prev_i = i
                if len(seq_lens) > 10:
                    seq_len = max(seq_lens)
                    skip = ((CYCLES - x) // seq_len) * seq_len
                    print(f'Skipping {skip} {seq_len}')
                    x += skip
                    # x -= 1
                    done = True

    if x == (CYCLES - 1):
        break
    
    x += 1

print(f'x: {x+1}')

total_load = subsums[-1]

# Rotating right
rotated_grid = list(zip(*rotated_grid[::-1]))
rotated_grid = [list(line) for line in rotated_grid]


print(f'\n grid at end')
for l in rotated_grid:
    print(' '.join(l))

result2 = total_load
aoc.print_result(2, result2, exp2)
