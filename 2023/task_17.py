import aoc
from heapq import heappop, heappush

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 102, 94

# Common
grid = [[int(c) for c in row] for row in lines]
H, W = len(grid), len(grid[0])
END_POSITION = (H - 1, W - 1)
LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)
arrows = {LEFT: '<', RIGHT: '>', UP: '^', DOWN: 'v'}
directions = [RIGHT, DOWN, LEFT, UP]

def print_path(path):
    empty_grid = [['.' for _ in row] for row in grid]
    for i, pos in enumerate(path):
        # if i > 0:
        #     move = (pos[0] - path[i-1][0], pos[1] - path[i-1][1])
        #     empty_grid[pos[0]][pos[1]] = arrows[move]
        # else:
        #     empty_grid[pos[0]][pos[1]] = 'S'
        empty_grid[pos[0]][pos[1]] = str(grid[pos[0]][pos[1]])
    for row in empty_grid:
        print(''.join(row))

def print_path_set(path):
    path = [p[0] for p in path]
    empty_grid = [['.' for _ in row] for row in grid]
    for i, pos in enumerate(path):
        empty_grid[pos[0]][pos[1]] = '#'
    for row in empty_grid:
        print(''.join(row))

# heat_losses = ()
global_heat = 1
def move():
    start_position = (0, 0)
    last_move = (0, 0)
    same_moves = 0
    heat_loss = 0
    path = set()
    queue = [(heat_loss, start_position, last_move, same_moves)]
    while queue:
        heat_loss, position, last_move, same_moves = heappop(queue)
        r, c = position

        if (position, last_move, same_moves) in path:
            continue

        path.add((position, last_move, same_moves))

        global global_heat
        if heat_loss > global_heat:
            global_heat = heat_loss
            # print(f'heat loss: {heat_loss}, queue size: {len(queue)}')
            # print_path_set(path)
        if position == END_POSITION:
            print(f'End hit, heat loss: {heat_loss}')
            return heat_loss

        if same_moves < 3 and last_move != (0, 0):
            new_r, new_c = r + last_move[0], c + last_move[1]
            if 0 <= new_r < H and 0 <= new_c < W:
                heappush(queue, (heat_loss + grid[new_r][new_c], (new_r, new_c), last_move, same_moves + 1))

        for direction in directions:
            rdir, cdir = direction

            if direction == (-last_move[0], -last_move[1]) or direction == last_move:
                continue
            new_r, new_c = r + rdir, c + cdir
            if new_r >= H or new_r < 0 or new_c >= W or new_c < 0:
                continue

            heappush(queue, (heat_loss + grid[new_r][new_c], (new_r, new_c), direction, 1))

def move2():
    start_position = (0, 0)
    last_move = (0, 0)
    same_moves = 0
    heat_loss = 0
    cache = set()
    global_heat = 0
    queue = [(heat_loss, start_position, last_move, same_moves, [])]
    while queue:
        # print(len(queue))
        heat_loss, position, last_move, same_moves, path = heappop(queue)
        r, c = position

        if (position, last_move, same_moves) in cache:
            continue

        cache.add((position, last_move, same_moves))

        if heat_loss > global_heat:
            global_heat = heat_loss
            # print(f'heat loss: {heat_loss}, queue size: {len(queue)}')
            # print_path(path)
        if position == END_POSITION and same_moves in range(4, 11):
            print(f'End hit, heat loss: {heat_loss}')
            nums = [grid[r][c] for r, c in path]
            print(nums)
            print(f'Sum: {sum(nums)}')
            print_path(path)
            return heat_loss
        # import pdb
        # pdb.set_trace()
        if same_moves < 10 and last_move != (0, 0):
            new_r, new_c = r + last_move[0], c + last_move[1]
            if 0 <= new_r < H and 0 <= new_c < W:
                heappush(queue, (heat_loss + grid[new_r][new_c], (new_r, new_c), last_move, same_moves + 1, path + [(new_r, new_c)]))
        if same_moves > 3 or last_move == (0, 0):

            for direction in directions:
                rdir, cdir = direction

                if direction == (-last_move[0], -last_move[1]) or direction == last_move:
                    continue
                new_r, new_c = r + rdir, c + cdir
                if new_r >= H or new_r < 0 or new_c >= W or new_c < 0:
                    continue
                heappush(queue, (heat_loss + grid[new_r][new_c], (new_r, new_c), direction, 1, path + [(new_r, new_c)]))

# Part 1
aoc.mark_task_start()
result1 = move()
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()

result2 = move2()

aoc.print_result(2, result2, exp2)
'''
2413432311323     2>>34^>>>1323     2>>>>>>>>1323
3215453535623     32v>>>35v5623     32154535v5623
3255245654254     32552456v>>54     32552456v4254
3446585845452     3446585845v52     34465858v5452
4546657867536     4546657867v>6     45466578v>>>>
1438598798454     14385987984v4     143859879845v
4457876987766     44578769877v6     445787698776v
3637877979653     36378779796v>     363787797965v
4654967986887     465496798688v     465496798688v
4564679986453     456467998645v     456467998645v
1224686865563     12246868655<v     122468686556v
2546548887735     25465488877v5     254654888773v
4322674655533     43226746555v>     432267465553v
'''