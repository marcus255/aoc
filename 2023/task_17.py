import aoc
from heapq import heappop, heappush

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 102, 94

# Common
grid = [[int(c) for c in row] for row in lines]
H, W = len(grid), len(grid[0])
END_POSITION = (H - 1, W - 1)
NO_MOVE, LEFT, RIGHT, UP, DOWN = (0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)
directions = [UP, DOWN, LEFT, RIGHT]

def print_path(path):
    if not path:
        return
    empty_grid = [["." for _ in row] for row in grid]
    for r, c in path:
        empty_grid[r][c] = str(grid[r][c])
    for row in empty_grid:
        print("".join(row))

def get_min_heat(min_same=0, max_same=3):
    heat, start, move, same_moves, path = 0, (0, 0), NO_MOVE, 0, []
    queue = [(heat, start, move, same_moves, path)]
    moves_done = set()
    new_path = None

    while queue:
        heat, position, move, same_moves, path = heappop(queue)

        if (position, move, same_moves) in moves_done:
            continue
        moves_done.add((position, move, same_moves))

        if position == END_POSITION and same_moves in range(min_same, max_same + 1):
            print_path(path)
            return heat

        r, c = position
        if same_moves < max_same and move != NO_MOVE:
            new_r, new_c = r + move[0], c + move[1]
            if 0 <= new_r < H and 0 <= new_c < W:
                # new_path = path + [(new_r, new_c)] # for printing the path
                new_heat = heat + grid[new_r][new_c]
                heappush(queue, (new_heat, (new_r, new_c), move, same_moves + 1, new_path))

        if same_moves > min_same or move == NO_MOVE:
            for direction in directions:
                if direction in [move, (-move[0], -move[1])]:
                    continue
                rdir, cdir = direction
                new_r, new_c = r + rdir, c + cdir
                if 0 <= new_r < H and 0 <= new_c < W:
                    # new_path = path + [(new_r, new_c)] # for printing the path
                    new_heat = heat + grid[new_r][new_c]
                    heappush(queue, (new_heat, (new_r, new_c), direction, 1, new_path))

# Part 1
aoc.mark_task_start()
result1 = get_min_heat()
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
MIN_SAME_MOVES, MAX_SAME_MOVES = 3, 10
result2 = get_min_heat(MIN_SAME_MOVES, MAX_SAME_MOVES)
aoc.print_result(2, result2, exp2)
