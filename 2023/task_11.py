import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 374, 8410

# Common
HEIGHT = len(lines)
WIDTH = len(lines[0])
same_rows, same_cols = [], []
space = [[x for x in line] for line in lines]
for i, row in enumerate(space):
    empty_elems = 0
    for col in row:
        if col == '.':
            empty_elems += 1
    if empty_elems == WIDTH:
        same_rows.append(i)

for i in range(WIDTH):
    empty_elems = 0
    for j in range(HEIGHT):
        if space[j][i] == '.':
            empty_elems += 1
    if empty_elems == HEIGHT:
        same_cols.append(i)

print(same_cols)
# for i in range(WIDTH, 0, -1):
#     if i in same_cols:
#         for j in range(HEIGHT):
#             space[j].insert(i, '.')

# WIDTH = len(space[0])

# for i in range(HEIGHT, 0, -1):
#     if i in same_rows:
#         space.insert(i, space[i])

# HEIGHT = len(space)

# Part 1
# for s in space:
#     print(''.join(s))

coords = []
for i, row in enumerate(space):
    for j, elem in enumerate(row):
        if elem == '#':
            coords.append((i, j))
EMTPY_SPACE = 1000_000
distances = []
for i, x in enumerate(coords):
    for j, y in enumerate(coords):
        if i != j:
            same_row_count = 0
            same_col_count = 0
            for same_row in same_rows:
                if x[0] > y[0]:
                    a = x[0]
                    b = y[0]
                else:
                    a = y[0]
                    b = x[0]
                if same_row in range(b, a):
                    same_row_count += 1
            for same_col in same_cols:
                if x[1] > y[1]:
                    a = x[1]
                    b = y[1]
                else:
                    a = y[1]
                    b = x[1]
                if same_col in range(b, a):
                    same_col_count += 1
            extra_x_steps = same_row_count * (EMTPY_SPACE - 1)
            extra_y_steps = same_col_count * (EMTPY_SPACE - 1)
            d = abs(x[0] - y[0]) + abs(x[1] - y[1]) + extra_x_steps + extra_y_steps
            # print(f'{i+1}=>{j+1}: {d}')
            distances.append(d)

 
import functools
import operator
result1 = functools.reduce(operator.add, distances) // 2


# print(coords)


aoc.print_result(1, result1, exp1)

# Part 2

aoc.print_result(2, result2, exp2)

#  ...#......
#  .......#..
#  #.........
#  ..........
#  ......#...
#  .#........
#  .........#
#  ..........
#  .......#..
#  #...#.....