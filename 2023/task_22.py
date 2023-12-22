import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 5, 7

'''
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''
# Common
X, Y, Z = 0, 1, 2
blocks = []
for line in lines:
    beg, end = line.split('~')
    A = [int(x) for x in beg.split(',')]
    B = [int(x) for x in end.split(',')]
    repeat_axis, size = None, 1
    for i in [X, Y, Z]:
        if abs(A[i] - B[i]) > 0:
            repeat_axis = i
            size += abs(A[i] - B[i])
            break
    
    block = [A[:]]
    for i in range(1, size):
        inc = (B[repeat_axis] - A[repeat_axis]) // (size - 1)
        new_block = A[:]
        new_block[repeat_axis] = new_block[repeat_axis] + inc * i
        block.append(new_block)
    blocks.append(block)

    print(f'A: {A}, B: {B}, axis: {repeat_axis}, size: {size} -> {block}')
import copy

def movable(block, grid):
    move_illegal = False
    while not move_illegal:
        new_pos = [[x, y, z-1] for x, y, z in block]
        for x, y, z in new_pos:
            if z < 1 or [x, y, z] in grid:
                move_illegal = True
                break
        if not move_illegal:
            return True
    return False

def move_down(block, grid):

    move_illegal = False
    moved = False
    while not move_illegal:
        new_pos = [[x, y, z-1] for x, y, z in block]
        for i, (x, y, z) in enumerate(new_pos):
            # if block == [[1, 1, 5], [1, 1, 6]] and [0, 1, 4] not in grid:
            #     import pdb
            #     pdb.set_trace()
            if z < 1 or [x, y, z] in grid:
                # print(f'Move illegal: {i}: {x},{y},{z}')
                move_illegal = True
                break
        if not move_illegal:
            block[:] = copy.deepcopy(new_pos)
            moved = True
    grid += block
    return moved


# Part 1
aoc.mark_task_start()
grid = []

print(f'blocks:\n{blocks}')
blocks = sorted(blocks, key=lambda x:x[0][Z])
print(f'Sorted blocks:\n{blocks}')

for block in blocks:
    # print(f'\nBefor: {block}')
    move_down(block, grid)
    # print(f'After: {block}')
    # print(f'Grid: {grid}')

grid_set = set([tuple(x) for x in grid])
# grid = list(grid_set)
# grid = [[*x] for x in grid]
if len(grid) != len(grid_set):
    raise RuntimeError(f'list {len(grid)} set {len(grid_set)}')

# print(f'Grid:\n{grid}')

removable_blocks = 0
grid_blocks = len(grid)
for n, block in enumerate(blocks):
    print(f'{n+1}: {block}')
    # tmp_grid = grid #copy.deepcopy(grid)
    for b in block:
        # print(f'rem {b}')
        grid.remove(b)
    if len(grid) != grid_blocks - len(block):
        raise RuntimeError(f'{len(grid)} {grid_blocks} {len(block)}')
    
    removable = True
    for other_block in blocks:
        if other_block is block:
            # print(f'Removed block, skip')
            continue
        # print(f'Comparing: {block} vs {other_block}')
        # print(f'Remaining grid:\n{tmp_grid}')
        # tmp_grid_2 = copy.deepcopy(grid)
        for bb in other_block:
            # print(f'rem {b}')
            grid.remove(bb)
        if movable(other_block, grid):
            # print(f'{block} -> fall {other_block}')
            removable = False
            grid += other_block
            break
        grid += other_block
    if removable:
        # print(f'Block removable: {block}')
        removable_blocks += 1

    # restore element
    grid += block

result1 = removable_blocks
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()



aoc.print_result(2, result2, exp2)
