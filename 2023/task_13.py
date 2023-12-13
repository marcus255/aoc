import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 405, 1

# Common
mirrors = []
current_mirror = []
for line in lines:
    if line == '':
        mirrors.append(current_mirror)
        current_mirror = []
    else:
        current_mirror.append([x for x in line])
mirrors.append(current_mirror)

def find_reflection(mirror):
    ref_count = []
    for r in range(0, len(mirror)):
        # print(f'Row {r}')
        ref_count.append(0)
        # print(ref_count)
        for offset in range(1, len(mirror)):
            try:
                if r-offset+1 < 0:
                    break
                if mirror[r-offset+1] == mirror[r+offset]:
                    # print(''.join(mirror[r-offset+1]), ''.join(mirror[r+offset]))
                    # print('adding', r, r-offset+1, r+offset)
                    ref_count[r] += 1
                else:
                    break
            except IndexError:
                # print(f'Invalid index {r} {r-offset+1} {r+offset}')
                break
        to_left = r + 1
        to_right = len(mirror) - to_left
        min_dist = min(to_left, to_right)
        if min_dist != ref_count[r]:
            ref_count[r] = 0
    # print(ref_count)
    max_ref, max_i = 0, 0    
    for i, ref in enumerate(ref_count):
        if ref > max_ref:
            max_ref = ref
            max_i = i

    to_left = max_i + 1
    to_right = len(mirror) - to_left
    min_dist = min(to_left, to_right)
    # print(to_left, to_right, max_ref, len(mirror))
    return to_left if min_dist == max_ref else 0

#   #.##..##.
#   ..#.##.#.
#   ##......#
#   ##......#
#   ..#.##.#.
#   ..##..##.
#   #.#.##.#.


# Part 1
total = 0
for mirror in mirrors:
    href = find_reflection(mirror)
    rotated_mirror = list(zip(*mirror))
    vref = find_reflection(rotated_mirror)
    # if vref:
    #     vref = len(rotated_mirror) - vref
    print(f'vref: {vref}, href: {href}')
    total += vref + 100 * href
    if href and vref:
        for l in mirror:
            print(''.join(l))
    # print()
    # # if not href and not vref:
    # for l in rotated_mirror:
    #     print(''.join(l))

result1 = total
aoc.print_result(1, result1, exp1)

# Part 2

aoc.print_result(2, result2, exp2)
