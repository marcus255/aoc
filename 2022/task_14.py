import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 24, 93

# Common
rocks = []
for line in lines:
    corners = []
    for c in line.split(' -> '):
        corners.append(tuple(map(int, c.split(','))))
    rocks.append(corners)

# Limits used for printing the grid
MAX_X = max(max(x for x, _ in rock) for rock in rocks)
MAX_Y = max(max(y for _, y in rock) for rock in rocks)
MIN_X = min(min(x for x, _ in rock) for rock in rocks)
MIN_Y = 0

source = (500, 0)
grid = {}
for rock in rocks:
    for (x1, y1), (x2, y2) in zip(rock, rock[1:]):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x1, y)] = '#'
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[(x, y1)] = '#'

def print_grid(grid):
    for y in range(MIN_Y, MAX_Y + 1):
        for x in range(MIN_X, MAX_X + 1):
            print(grid.get((x, y), '.'), end='')
        print()

def fill_with_sand(grid):
    sand = 0
    # while sand does not reach the source
    while source not in grid:
        pos = source
        while True:
            new_pos = (pos[0], pos[1] + 1)
            if new_pos[1] > MAX_Y:
                # Sand is falling out of the grid
                return sand
            nx, ny = new_pos
            # Possible places for sand, in order of preference:
            # down, left-down, right-down
            for p in [new_pos, (nx - 1, ny), (nx + 1, ny)]:
                if p not in grid:
                    pos = p
                    break
            else:
                # Couldn't fit the sand, leave it in current position
                grid[pos] = 'o'
                break
        sand += 1
    return sand

# Part 1
aoc.mark_task_start()
result1 = fill_with_sand(grid)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
# Construct a floor at the bottom of the grid
floor_y = MAX_Y + 2
sx, sy = source
# Make it wide enough to catch all the sand
floor_x_min, floor_x_max = sx - (floor_y - sy), sx + (floor_y - sy)
# Add the floor to the grid from part 1
for x in range(floor_x_min, floor_x_max + 1):
    grid[(x, floor_y)] = '#'
# Adjust the limits after adding the floor
MAX_Y, MIN_X, MAX_X = floor_y, floor_x_min, floor_x_max
# print_grid(grid)

# Use the result from part 1 not to compute it again
result2 = result1 + fill_with_sand(grid)
aoc.print_result(2, result2, exp2)
