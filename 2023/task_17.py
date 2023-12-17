import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1, 1

# Common
grid = [[int(c) for c in row][:10] for row in lines[:10]]
H, W = len(grid), len(grid[0])
END_POSITION = (H - 1, W - 1)
LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)
arrows = {LEFT: '<', RIGHT: '>', UP: '^', DOWN: 'v'}
directions = [RIGHT, DOWN, LEFT, UP]

def print_path(path):
    empty_grid = [['.' for _ in row] for row in grid]
    for i, pos in enumerate(path):
        if i > 0:
            move = (pos[0] - path[i-1][0], pos[1] - path[i-1][1])
            empty_grid[pos[0]][pos[1]] = arrows[move]
    for row in empty_grid:
        print(''.join(row))

# heat_losses = ()
global_min = 1000
def move(position, last_move, same_moves, path, count=0, heat_loss=0):
    r, c = position
    if heat_loss > exp:
        return
    # if count < 20 and heat_loss > 5*20:
    #     return
    # if count > 28:
    #     return
    if r >= H or r < 0 or c >= W or c < 0:
        return
    if position in path:
        return
    global global_min
    heat_loss += grid[r][c]
    path.append(position)
    count += 1

    if position == END_POSITION:

        # if len(path) != len(set(path)):
        #     raise RuntimeError(f'{len(path)}, {len(set(path))}')
        # import pdb
        # pdb.set_trace()
        if heat_loss < global_min:
            global_min = heat_loss
            print(f'End hit, heat loss: {heat_loss}, len: {len(path)}, min: {global_min}')
            print_path(path)
        # heat_losses.add(heat_loss)
        return

    for direction in directions:
        rdir, cdir = direction
        if direction == last_move:
           if same_moves == 3:
              same_moves = 1
              continue
           else:
              same_moves += 1
        new_position = (r + rdir, c + cdir)
        move(new_position, direction, same_moves, path[:], count, heat_loss)

# Part 1
aoc.mark_task_start()
start_position = (0, 0)
last_move = RIGHT
same_moves = 0
path = []
all = [x for row in grid for x in row]
avg = sum(all)//len(all)
exp = avg * (H+W)
print(f'Sum: {sum(all)}, count: {len(all)}, avg: {avg}, exp: {exp}')
move(start_position, last_move, same_moves, path, heat_loss=-grid[0][0])
print(global_min)


aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()



aoc.print_result(2, result2, exp2)
'''
2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>
'''