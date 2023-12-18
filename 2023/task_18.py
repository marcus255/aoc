import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 62, 1

# Common
lines = [line.split(' ') for line in lines]
moves = [line[0] for line in lines]
depths = [int(line[1]) for line in lines]
colors = [line[2] for line in lines]
NO_MOVE, LEFT, RIGHT, UP, DOWN = (0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)
dirs = {'U': UP, 'D': DOWN, 'L': LEFT, 'R': RIGHT}
inside_moves = {'U': RIGHT, 'D': LEFT, 'L': UP, 'R': DOWN}

def is_right_turn(prev, next):
    # print(f'Right: {prev} {next}')
    if prev and (prev, next) in [(RIGHT, DOWN), (DOWN, LEFT), (LEFT, UP), (UP, RIGHT)]:
        return True
    else:
        return False
def is_left_turn(prev, next):
    # print(f'Left: {prev} {next}')
    if prev and (prev, next) in [(RIGHT, UP), (UP, LEFT), (LEFT, DOWN), (DOWN, RIGHT)]:
        return True
    else:
        return False

# Part 1
aoc.mark_task_start()

# part 2 processing
num_to_move = {'0':'R', '1':'D', '2':'L', '3':'U'}
moves, depths = [], []
for col in colors:
    hex_depth = col[2:-2]
    move = num_to_move[col[-2]]
    depth = int(hex_depth, 16)
    # print(move, depth)
    moves.append(move)
    depths.append(depth)




SIZE = (16, 16) if aoc.is_test_mode() else (600, 600)
grid = [['.' for _ in range(2*SIZE[1])] for _ in range(2*SIZE[0])]

first_r, first_c = dirs[moves[0]]

pos = (SIZE[0] // 2, SIZE[1] // 2)
prev_move = None
prev_turn = None
turn = None
coords = [pos]
max_r, min_r, max_c, min_c = pos[0], pos[1], pos[0], pos[1]
print(f'Starting at {pos}')
for i, (move, depth) in enumerate(zip(moves, depths)):
    m = dirs[move]
    prev_frag_change = 0
    if is_right_turn(prev_move, m):
        # print(f'RIGHT: ({pos}) => {prev_move}, {m}')
        turn = 'R'
    if is_left_turn(prev_move, m):
        # print(f'LEFT: ({pos}) => {prev_move}, {m}')
        turn = 'L'

    if prev_turn == 'R' and turn == 'R':
        prev_frag_change = 1

    if prev_turn == 'L' and turn =='L':
        prev_frag_change = -1

    if prev_frag_change:
        # import pdb
        # pdb.set_trace()
        orig_pos = pos
        updown_move = prev_frag_change*prev_move[0]
        lr_move = prev_frag_change*prev_move[1]
        if prev_move == DOWN and prev_frag_change == 1:
            updown_move = 1
        elif prev_move == DOWN and prev_frag_change == -1:
            updown_move = -1
        elif prev_move == UP and prev_frag_change == 1:
            updown_move = -1
        elif prev_move == UP and prev_frag_change == -1:
            updown_move = 1
        elif prev_move == RIGHT and prev_frag_change == 1:
            lr_move = 1
        elif prev_move == RIGHT and prev_frag_change == -1:
            lr_move = -1
        elif prev_move == LEFT and prev_frag_change == 1:
            lr_move = -1
        elif prev_move == LEFT and prev_frag_change == -1:
            lr_move = 1

        coords[-1] = (coords[-1][0] + updown_move, coords[-1][1] + lr_move)


        pos = coords[-1]
        # print(f'Changing: {orig_pos} - > {pos}')
    pos = (pos[0] + m[0] * depth, pos[1] + m[1] * depth)
    if i == (len(moves) - 1):
        print(f'Extra step:', pos[0] + m[0], pos[1] + m[1])
        pos = (pos[0] + m[0], pos[1] + m[1])
    coords.append(pos)
    # for _ in range(depth):
    max_r = pos[0] if pos[0] > max_r else max_r
    min_r = pos[0] if pos[0] < min_r else min_r
    max_c = pos[1] if pos[1] > max_c else max_c
    min_c = pos[1] if pos[1] < min_c else min_c
    #     pos = (pos[0] + m[0], pos[1] + m[1])
    #     grid[pos[0]][pos[1]] = '#'
    prev_move = m
    prev_turn = turn

'''
................#.....#...  
...............#..........  
..........................  
...............#.#........  
..........................  
...............#.#........  
....................#.#...  
....................#.#...  
...............##.........  
..........................  
................#.....#...  

#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######
'''

# for r, c in coords:
#     try:    
#         grid[SIZE[0]//2 + r][SIZE[1]//2 + c] = '#'
#     except IndexError:
#         print(f'Inv index: {SIZE[0]//2 + r} {SIZE[1]//2 + c}')

# for r in range(2*SIZE[0]):
#     row = grid[r]
#     print(f'{"".join(row)}')

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
rrr = [r for (r, c) in coords]
ccc = [c for (r, c) in coords]
# print(rrr)
# print(ccc)

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
area = PolyArea(ccc, rrr)
print(f'area: {area}')
area = int(area)
# 0.26353377782163534


# print()
# print()
# print()

# for r in range(min_r, min_r + 15): #, max_r+1):
#     row = grid[r]
#     print(f'{"".join(row[min_c:max_c+1])}')
#     # if r > max_r:
#     #     break

path_len = 0
# for r, _ in enumerate(grid):
#     for c, _ in enumerate(row):
#         if grid[r][c] == '#':
#             path_len += 1
# print(min_r, max_r, min_c, max_c)
# print(max_r - min_r, max_c - min_c)

result1 = path_len + area
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()



aoc.print_result(2, result2, exp2)
