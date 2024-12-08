import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 14, 34

# Common
grid = []
for line in lines:
    grid.append(list(line))
antennas = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            if grid[i][j] not in antennas:
                antennas[grid[i][j]] = []
            antennas[grid[i][j]].append((i, j))

def get_antinodes(grid, antennas, in_line=False):
    antinodes = set()
    for coords in antennas.values():
        for i in range(len(coords)):
            if in_line:
                antinodes.add(coords[i])
            for j in range(i+1, len(coords)):
                a, b = coords[i], coords[j]
                x1, y1 = a[0] - b[0], a[1] - b[1]
                x2, y2 = b[0] - a[0], b[1] - a[1]
                while True:
                    anti1 = (a[0] + x1, a[1] + y1)
                    if not all([0 <= anti1[0] < len(grid), 0 <= anti1[1] < len(grid[0])]):
                        break
                    antinodes.add(anti1)
                    if not in_line:
                        break
                    a = anti1
                while True:
                    anti2 = (b[0] + x2, b[1] + y2)
                    if not all([0 <= anti2[0] < len(grid), 0 <= anti2[1] < len(grid[0])]):
                        break
                    antinodes.add(anti2)
                    if not in_line:
                        break
                    b = anti2
    return len(antinodes)

# Part 1
aoc.mark_task_start()
result1 = get_antinodes(grid, antennas, in_line=False)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = get_antinodes(grid, antennas, in_line=True)
aoc.print_result(2, result2, exp2)
