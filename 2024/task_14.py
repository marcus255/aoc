import aoc
import sys
import re

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 12, 1

# Common
W, H = (11, 7) if aoc.is_test_mode() else (101, 103)
# Example line: p=0,4 v=3,-3
r = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')

input_robots = []
for line in lines:
    m = re.match(r, line)
    if m:
        pos = (int(m.group(1)), int(m.group(2)))
        vel = (int(m.group(3)), int(m.group(4)))
    input_robots.append((pos, vel))

def move_robot(pos, vel):
    return ((pos[0] + vel[0]) % W, (pos[1] + vel[1]) % H)

def move_all_robots(robots):
    for i, robot in enumerate(robots):
        pos, vel = robot
        robots[i] = (move_robot(pos, vel), vel)

def print_grid(robots):
    grid = [['.' for _ in range(W)] for _ in range(H)]
    for r in robots:
        x, y = r[0]
        grid[y][x] = '#'
    for row in grid:
        print(''.join(row))

# Part 1
aoc.mark_task_start()
robots = input_robots[:]
NUM_SECONDS = 100
for i in range(NUM_SECONDS):
    move_all_robots(robots)

q1, q2, q3, q4 = 0, 0, 0, 0
H2, W2 = H // 2, W // 2
for r in robots:
    x, y = r[0]
    if x < W2:
        if y < H2:
            q1 += 1
        elif y > H2:
            q2 += 1
    elif x > W2:
        if y < H2:
            q3 += 1
        elif y > H2:
            q4 += 1

result1 = q1 * q2 * q3 * q4
aoc.print_result(1, result1, exp1)

# Part 2
if aoc.is_test_mode():
    # No solution for test mode
    sys.exit()

aoc.mark_task_start()
robots = input_robots[:]
EXP_CONSECUTIVE = 15
n = 1
while n:
    move_all_robots(robots)
    robots.sort(key=lambda x: x[0][0])
    for h in range(H):
        # get unique robot's X coordinates in sorted order
        line = sorted(list(set([x[0][0] for x in robots if x[0][1] == h])))
        # expect christmass tree to contain a continuous horizontal line of robots
        if len(line) > EXP_CONSECUTIVE and len(line) == line[-1] - line[0] + 1:
            # print_grid(robots)
            result2 = n
            n = -1
            break
    n += 1

aoc.print_result(2, result2, exp2)
