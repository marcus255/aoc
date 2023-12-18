import aoc
import aoc_utils as utils

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 62, 952408144115

# Common
lines = [line.split(' ') for line in lines]
NO_MOVE, LEFT, RIGHT, UP, DOWN = (0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)
dir_to_move = {'U': UP, 'D': DOWN, 'L': LEFT, 'R': RIGHT}

def is_right_turn(prev, next):
    return prev and (prev, next) in [(RIGHT, DOWN), (DOWN, LEFT), (LEFT, UP), (UP, RIGHT)]

def is_left_turn(prev, next):
    return prev and (prev, next) in [(RIGHT, UP), (UP, LEFT), (LEFT, DOWN), (DOWN, RIGHT)]

def add_extra_move(prev_move, curr_move, prev_turn, turn, coords):
    if is_right_turn(prev_move, curr_move):
        turn = 'R'
    if is_left_turn(prev_move, curr_move):
        turn = 'L'

    extra_move = (0, 0)
    if prev_turn == 'R' and turn == 'R':
        extra_move = prev_move
    elif prev_turn == 'L' and turn =='L':
        extra_move = (-prev_move[0], -prev_move[1])

    # Extend last edge's length by 1 if last two turns were to right, 
    # shrink last edge's length by 1 if last two turns were to left
    pos = (coords[-1][0] + extra_move[0], coords[-1][1] + extra_move[1])
    coords[-1] = pos

    return pos, turn

def path_to_coords():
    pos, prev_move, prev_turn, turn = None, None, None, None
    coords = [(0, 0)]
    for direction, edge_len in zip(moves, depths):
        curr_move = dir_to_move[direction]

        # Polygon which includes the outer path has different area
        # than actual polygon defined by coordinates of this path
        # This algorithm extends/shrinks edges approprietaly.
        # Other way is to use Pick's theorem
        pos, turn = add_extra_move(prev_move, curr_move, prev_turn, turn, coords)
        prev_turn = turn
        prev_move = curr_move

        # Make current move
        pos = (pos[0] + curr_move[0] * edge_len, pos[1] + curr_move[1] * edge_len)
        coords.append(pos)

    # Need to add one more element at the end of the path
    coords.append((pos[0] + curr_move[0], pos[1] + curr_move[1]))

    return coords

# Part 1
aoc.mark_task_start()
moves = [line[0] for line in lines]
depths = [int(line[1]) for line in lines]
result1 = int(utils.polygon_area(path_to_coords()))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
colors = [line[2] for line in lines]
moves, depths = [], []
for col in colors:
    # parsing color '(#6c74e0)', where 0x6c74e is depth and '0' is direction LEFT
    moves.append("RDLU"[int(col[-2])])
    depths.append(int(col[2:-2], 16))
result2 = int(utils.polygon_area(path_to_coords()))
aoc.print_result(2, result2, exp2)
