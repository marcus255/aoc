import aoc
from aoc_utils import translated_2d
from copy import deepcopy

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 4512, 1924

# Common
numbers = list(map(int, lines[0].split(',')))
boards = []
for line in lines[1:]:
    if not line:
        board = []
        boards.append(board)
    else:
        board.append([int(x) for x in line.split(' ') if x != ''])    

def mark_number(board, number):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == number:
                board[r][c] = -1

def is_all_line_marked(board):
    for row in board:
        if row == [-1] * len(row):
            return True
    for row in translated_2d(board):
        if row == [-1] * len(row):
            return True
    return False

def count_marked(board, input_board):
    marked = 0
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            if item != -1:
                marked += input_board[r][c]
    return marked

def solve(numbers, boards, last_wins=False):
    input_boards = deepcopy(boards)
    for n in numbers:
        for i, board in enumerate(boards):
            mark_number(board, n)
            if is_all_line_marked(board):
                if last_wins and len([x for x in boards if x]) > 1:
                    boards[i] = []
                else:
                    return count_marked(board, input_boards[i]) * n

# Part 1
aoc.mark_task_start()
result1 = solve(numbers, deepcopy(boards))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = solve(numbers, boards, last_wins=True)
aoc.print_result(2, result2, exp2)
