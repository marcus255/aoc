import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 13, 36

# Common
DIRS = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
steps = []
for line in lines:
    dir, val = line.split(' ')
    steps.extend([dir] * int(val))

def get_distance(head, tail):
    (hx, hy), (tx, ty) = head, tail
    if abs(hx - tx) == 1 and abs(hy - ty) == 1:
        # Adjacent diagonally - consider it as distance 1
        return 1
    return abs(hx - tx) + abs(hy - ty)

def make_move(head_pos, tail_pos, move):
    new_head_pos = (head_pos[0] + move[0], head_pos[1] + move[1])
    nhx, nhy = new_head_pos
    tx, ty = tail_pos
    dx, dy = (nhx - tx, nhy - ty)
    dist = get_distance(new_head_pos, tail_pos)
    if dist == 2:
        tail_pos = (tx + dx / 2, ty + dy / 2)
    elif dist >= 3:
        move = (dx / abs(dx), dy / abs(dy))
        tail_pos = (tx + move[0], ty + move[1])
    return new_head_pos, tail_pos

def print_rope_and_wait(rope):
    SIZE = 15 if aoc.is_test_mode() else 300
    for y in range(-SIZE, SIZE):
        for x in range(-SIZE, SIZE):
            print(rope.index((x, y)) if (x, y) in rope else '.', end='')
        print()
    input()

# Part 1
aoc.mark_task_start()
tail_pos = head_pos = (0, 0)
tail_visited = set()
for step in steps:
    move = DIRS[step]
    head_pos, tail_pos = make_move(head_pos, tail_pos, move)
    tail_visited.add(tail_pos)
result1 = len(tail_visited)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
rope = [(0, 0)] * 10 # 10 segments at indexes 0(HEAD), 1, 2, 3, 4, 5, 6, 7, 8, 9(TAIL)
tail_visited = set()

# Different test vector for part 2
if aoc.is_test_mode():
    lines = ['R 5','U 8','L 8','D 3','R 17','D 10','L 25','U 20']
    steps = []
    for line in lines:
        dir, val = line.split(' ')
        steps.extend([dir] * int(val))

for step in steps:
    move = DIRS[step]
    for i in range(len(rope) - 1):
        head_i, tail_i = i, i + 1
        head, tail = rope[head_i], rope[tail_i]
        # Save head position change only, not to move the tail twice
        rope[head_i], new_tail = make_move(head, tail, move)
        if new_tail == tail:
            # Tail did not move, do not update the rest of the rope
            break
        # Tail position change is the new move for next segment
        move = (new_tail[0] - tail[0], new_tail[1] - tail[1])
        # If this is the last head-tail segment, update the tail also
        if tail_i == len(rope) - 1:
            rope[tail_i] = new_tail
    tail_visited.add(rope[-1])
    # print_rope_and_wait(rope)

result2 = len(tail_visited)
aoc.print_result(2, result2, exp2)
