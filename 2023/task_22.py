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
    while not move_illegal:
        new_pos = [[x, y, z-1] for x, y, z in block]
        for x, y, z in new_pos:
            if z < 1 or [x, y, z] in grid:
                move_illegal = True
                break
        if not move_illegal:
            block[:] = copy.deepcopy(new_pos)
    grid += block

def print_blocks(blocks, width=12, height=20):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    line = ['.' for _ in range(width)]
    grid = [line[:] for _ in range(height)]
    grid2 = [line[:] for _ in range(height)]

    for i, block in enumerate(blocks):
        for x, y, z in block:
            grid[height-z][x] = letters[i%len(letters)]
            grid2[height-z][y] = letters[i%len(letters)]
    
    for l1, l2 in zip(grid, grid2):
        print(f'{"".join(l1)}  {"".join(l2)}')

def move_all_down(grid, blocks):
    print(f'blocks:\n{blocks}')
    blocks = sorted(blocks, key=lambda x:x[0][Z])
    print(f'Sorted blocks:\n{blocks}')

    for block in blocks:
        move_down(block, grid)

# Part 1
aoc.mark_task_start()
grid = []
move_all_down(grid, blocks)
print_blocks(blocks, height=10 if aoc.is_test_mode() else 160)

grid_set = set([tuple(x) for x in grid])
if len(grid) != len(grid_set):
    raise RuntimeError(f'list {len(grid)} set {len(grid_set)}')

# print(f'Grid:\n{grid}')

# Part 2

for block in blocks:
    # Sort segments in block from lowest Z to highest
    block[:] = sorted(block, key=lambda x: x[Z])
# Sort blocks from highest Z of first segment to lowest
blocks = sorted(blocks, key=lambda x:x[0][Z], reverse=True)
print(f'Reverse sorted blocks after fall:\n{blocks}')

# From now on, do not rearrange blocks, as we will use their indexes

# Map grid positions to id of block it is a part of
xyz_to_block = {}
for i, block in enumerate(blocks):
    for x, y, z in block:
        block_key = tuple(map(tuple, block))
        xyz_to_block[(x, y, z)] = i

support_blocks = []
for i, block in enumerate(blocks):
    support_blocks.append([])
    z = block[0][Z]
    if z == 1:
        print(f'{blocks[i]} sits on ground')
        continue
    for x, y, _ in block:
        key = (x, y, z - 1)
        if key in xyz_to_block and xyz_to_block[key] not in support_blocks[i]:
            support_blocks[i].append(xyz_to_block[key])

print('\nSupport blocks:')
for i, v in enumerate(support_blocks):
    print(f'{i}: {blocks[i]} lays on {v}')


fallable_blocks = 0
num_blocks = len(support_blocks)
for i, v in enumerate(support_blocks):
    val = support_blocks[i]
    # remove n-th block and validate which blocks will fall
    support_blocks[i] = []
    print(f'\nRemoved {i}')
    # blocks_above = support_blocks[num_blocks-i:]
    removed_blocks = [i]
    for j in range(i - 1, -1, -1):
        # print(f'Checking {j}, support {support_blocks[j]}, removed {removed_blocks}')
        if support_blocks[j] and all(x in removed_blocks for x in support_blocks[j]):
            # print(f'Block {j} {blocks[j]} no longer supported')
            removed_blocks.append(j)
            fallable_blocks += 1
            continue

    support_blocks[i] = val

result2 = fallable_blocks

# Part 2
aoc.mark_task_start()


aoc.print_result(2, result2, exp2)
