import aoc
import aoc_utils as utils

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 405, 400

# Common
mirrors = []
mirror = []
for line in lines:
    if line == '':
        mirrors.append(mirror)
        mirror = []
    else:
        mirror.append([x for x in line])
mirrors.append(mirror)

def find_reflections(mirror):
    reflections = []
    num_rows = len(mirror)
    for row in range(0, num_rows):
        reflected_rows = 0
        for offset in range(1, num_rows):
            row_up = row - offset + 1
            row_down = row + offset
            if row_up < 0 or row_down >= num_rows:
                break
            if mirror[row_up] == mirror[row+offset]:
                reflected_rows += 1
            else:
                break
        if not reflected_rows:
            continue
        to_left = row + 1
        to_right = num_rows - to_left
        exp_reflect_rows = min(to_left, to_right)
        if exp_reflect_rows == reflected_rows:
            reflections.append((to_left, reflected_rows))

    reflections = sorted(reflections, key=lambda x:x[1])
    return tuple(reflections)

# Part 1
aoc.mark_task_start()
total = 0
for mirror in mirrors:
    href = find_reflections(mirror)
    href = href[0][0] if href else 0
    mirror = utils.translated_2d(mirror)
    vref = find_reflections(mirror)
    vref = vref[0][0] if vref else 0
    total += vref + 100 * href

result1 = total
aoc.print_result(1, result1, exp1)

def switch_item_at(grid, i, j):
    grid[i][j] = '.' if grid[i][j] == '#' else '#'

# Part 2
aoc.mark_task_start()
total = 0
for mirror in mirrors:
    href = find_reflections(mirror)
    vref = find_reflections(utils.translated_2d(mirror))

    hrefs, vrefs = set(), set()
    for i in range(len(mirror)):
        for j in range(len(mirror[0])):
            switch_item_at(mirror, i, j)
            href2 = find_reflections(mirror)
            vref2 = find_reflections(utils.translated_2d(mirror))
            hrefs.update(href2)
            vrefs.update(vref2)
            # Restore original item at (i, j)
            switch_item_at(mirror, i, j)

    # Remove original reflections from new reflections
    vrefs = list(vrefs - set(vref))
    hrefs = list(hrefs - set(href))
    # Make sure there is only one reflection per mirror
    if len(vrefs) + len(hrefs) != 1:
        raise RuntimeError

    href = hrefs[0][0] if len(hrefs) else 0
    vref = vrefs[0][0] if len(vrefs) else 0
    total += vref + 100 * href

result2 = total
aoc.print_result(2, result2, exp2)
