import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 17, 16

# Common
coords = set()
folds = []
for line in lines:
    if ',' in line:
        coords.add(tuple(map(int, line.split(','))))
    elif '=' in line:
        axis, number = line[len('fold along '):].split('=')
        xfold, yfold = (int(number), 0) if axis == 'x' else (0, int(number))
        folds.append((xfold, yfold))

def get_folded_coords(coords, fold):
    xfold, yfold = fold
    folded_coords = set()
    for x, y in coords:
        if yfold and y > yfold:
            folded_coords.add((x, 2 * yfold - y))
        elif xfold and x > xfold:
            folded_coords.add((2 * xfold - x, y))
        else:
            folded_coords.add((x, y))
    return folded_coords

# Part 1
aoc.mark_task_start()
result1 = len(get_folded_coords(coords, folds[0]))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
folded_coords = coords.copy()
for fold in folds:
    folded_coords = get_folded_coords(folded_coords, fold)

# For the task input, folded paper should print out 'AHGCPGAU' text
# for y in range(10):
#     for x in range(50):
#         print('█' if (x, y) in folded_coords else '.', end='')
#     print()

# As a result, copmare the number of '#' in the folded paper with the expected result
result2 = len(folded_coords)
aoc.print_result(2, result2, exp2)
