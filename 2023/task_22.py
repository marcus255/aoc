import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 5, 7

# Common
X, Y, Z = 0, 1, 2

def load_blocks():
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
    return blocks

def sorted_top_to_bottom(blocks):
    for block in blocks:
        # Sort segments in block from lowest Z to highest
        block[:] = sorted(block, key=lambda x: x[Z])
    # Sort blocks from highest Z of first segment to lowest
    return sorted(blocks, key=lambda x:x[0][Z], reverse=True)

def get_support_blocks(blocks):
    # Map grid positions to id of block it is a part of
    xyz_to_block = {}
    for i, block in enumerate(blocks):
        for x, y, z in block:
            xyz_to_block[(x, y, z)] = i

    support_blocks = []
    for i, block in enumerate(blocks):
        support_blocks.append([])
        # Get first fragment of the block, as it is the lowest one after sorting
        z = block[0][Z]
        # Look for supporting blocks only if not supported directly by ground
        if z > 1:
            for x, y, _ in block:
                key = (x, y, z - 1)
                if key in xyz_to_block and xyz_to_block[key] not in support_blocks[i]:
                    support_blocks[i].append(xyz_to_block[key])
        # print(f'Block {i}: {blocks[i]} supported by {support_blocks[i]}')
    return support_blocks

def move_down(block, grid):
    move_illegal = False
    while not move_illegal:
        for x, y, z in block:
            # Check only last 200 previously populated positions in grid to speed up
            if z - 1 < 1 or [x, y, z - 1] in grid[-200:]:
                move_illegal = True
                break
        if not move_illegal:
            for b in block:
                b[Z] = b[Z] - 1
    grid += block

def move_all_down(blocks):
    occupied = []
    for block in blocks:
        move_down(block, occupied)
    # Make sure there are no overlaps between blocks
    occupied_set = set([tuple(x) for x in occupied])
    if len(occupied) != len(occupied_set):
        raise RuntimeError(f'list {len(occupied)} set {len(occupied_set)}')

# Part 1
aoc.mark_task_start()
blocks = load_blocks()
# Sort blocks from lowest Z of first segment to highest
blocks = sorted(blocks, key=lambda x:x[0][Z])
move_all_down(blocks)
# Rearrange for easier traversing
blocks = sorted_top_to_bottom(blocks)
support_blocks = get_support_blocks(blocks)
fallable = 0
for i, _ in enumerate(support_blocks):
    for j, block in enumerate(support_blocks):
        if j != i and [i] == block:
            fallable += 1
            break
result1 = len(support_blocks) - fallable
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
fallable = 0
for i, v in enumerate(support_blocks):
    val = support_blocks[i]
    # remove n-th block and validate which blocks will fall
    removed_blocks = [i]
    for j in range(i - 1, -1, -1):
        # print(f'Checking {j}, support {support_blocks[j]}, removed {removed_blocks}')
        if support_blocks[j] and all(x in removed_blocks for x in support_blocks[j]):
            # print(f'Block {j} {blocks[j]} no longer supported')
            removed_blocks.append(j)
            fallable += 1
            continue

result2 = fallable
aoc.print_result(2, result2, exp2)
