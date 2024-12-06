import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 18, 9

# Common
def find_matches(coords, matches):
    count = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            text = ''
            for a, b in coords:
                ni, nj = i + a, j + b
                if any([ni < 0, nj < 0, ni >= len(lines), nj >= len(lines[0])]):
                    text = ''
                    break
                text += lines[ni][nj]
            if text in matches:
                count += 1
    return count

# Part 1
all_coords = [
    # XMAS  0,0 0,1 0,2 0,3
    # M     1,0
    # A     2,0
    # S     3,0
    [(0, 0), (0, 1), (0, 2), (0, 3)], # horizontal text
    [(0, 0), (1, 0), (2, 0), (3, 0)], # vertical text
    # X  X  0,0         0,3
    #  MM       1,1 1,2
    #  AA       2,1 2,2
    # S  S  3,0         3,3
    [(0, 0), (1, 1), (2, 2), (3, 3)], # diagonal text
    [(0, 3), (1, 2), (2, 1), (3, 0)], # diagonal text
]
matches = ['XMAS', 'SAMX']
aoc.mark_task_start()
for coords in all_coords:
    result1 += find_matches(coords, matches)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
# M M  0,0     0,2
#  A       1,1
# S S  2,0     2,2
coords = [(0, 0), (1, 1), (2, 2), (0, 2), (1, 1), (2, 0)]
matches = ['MASMAS', 'MASSAM', 'SAMMAS', 'SAMSAM']
result2 = find_matches(coords, matches)
aoc.print_result(2, result2, exp2)
