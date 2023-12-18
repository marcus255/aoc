import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 62, 1

# Common
lines = [line.split(' ') for line in lines]
moves = [line[0] for line in lines]
depths = [int(line[1]) for line in lines]
NO_MOVE, LEFT, RIGHT, UP, DOWN = (0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)
dirs = {'U': UP, 'D': DOWN, 'L': LEFT, 'R': RIGHT}
inside_moves = {'U': RIGHT, 'D': LEFT, 'L': UP, 'R': DOWN}


# Part 1
aoc.mark_task_start()
SIZE = (30, 30) if aoc.is_test_mode() else (600, 600)
grid = [['.' for _ in range(SIZE[1])] for _ in range(SIZE[0])]

pos = (SIZE[0] // 2, SIZE[1] // 2)
coords = []
max_r, min_r, max_c, min_c = pos[0], pos[1], pos[0], pos[1]
for move, depth in zip(moves, depths):
    m = dirs[move]
    
    coords.append((pos, move))
    for _ in range(depth):
        max_r = pos[0] if pos[0] > max_r else max_r
        min_r = pos[0] if pos[0] < min_r else min_r
        max_c = pos[1] if pos[1] > max_c else max_c
        min_c = pos[1] if pos[1] < min_c else min_c
        pos = (pos[0] + m[0], pos[1] + m[1])
        grid[pos[0]][pos[1]] = '#'
    prev_move = move

for r in range(min_r, max_r+1):
    row = grid[r]
    print(f'{"".join(row[min_c:max_c+1])}')
    # if r > max_r:
    #     break

# prev = (0, 0)
# prev_move = (0, 0)
# for (r, c), m in coords:
#     inside = inside_moves[m]
#     # print(r, c, inside)
#     if inside == DOWN or prev == DOWN or (prev_move == DOWN and m == RIGHT):
#         for rr in range(r + 1, SIZE[0]):
#             if grid[rr][c] == '#':
#                 # print(f'break at {rr}, {c}')
#                 break
#             else:
#                 grid[rr][c] = '#'
#     if inside == UP or prev == UP:
#         for rr in range(r - 1, 0, -1):
#             if grid[rr][c] == '#':
#                 # print(f'break at {rr}, {c}')
#                 break
#             else:
#                 grid[rr][c] = '#'
#     prev = inside
#     prev_move = m
        

import numpy as np
rrr = [r for (r, c), _ in coords]
ccc = [c for (r, c), _ in coords]
print(rrr)
print(ccc)

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
area = PolyArea(rrr, ccc)
print(f'area: {area}')
area = int(area)
# 0.26353377782163534


print()
print()
print()

for r in range(min_r, min_r + 15): #, max_r+1):
    row = grid[r]
    print(f'{"".join(row[min_c:max_c+1])}')
    # if r > max_r:
    #     break

path_len = 0
for r, _ in enumerate(grid):
    for c, _ in enumerate(row):
        if grid[r][c] == '#':
            path_len += 1
print(min_r, max_r, min_c, max_c)
print(max_r - min_r, max_c - min_c)

result1 = path_len + area
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()



aoc.print_result(2, result2, exp2)
