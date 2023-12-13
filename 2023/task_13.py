import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 405, 400

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
        # print(ref_count)
        rcount = 0
        for offset in range(1, len(mirror)):
            try:
                if r-offset+1 < 0:
                    break
                if mirror[r-offset+1] == mirror[r+offset]:
                    # print(''.join(mirror[r-offset+1]), ''.join(mirror[r+offset]))
                    # print('adding', r, r-offset+1, r+offset)
                    rcount += 1
                else:
                    break
            except IndexError:
                # print(f'Invalid index {r} {r-offset+1} {r+offset}')
                break
        if not rcount:
            continue
        to_left = r + 1
        to_right = len(mirror) - to_left
        min_dist = min(to_left, to_right)
        if min_dist == rcount:
            ref_count.append((to_left, rcount))
    ref_count = sorted(ref_count, key=lambda x:x[1])
    # print(ref_count)

    return tuple(ref_count)

# Part 1
total = 0
# for mirror in mirrors:
#     href = find_reflection(mirror)
#     href = href[0][0] if href else 0
#     rotated_mirror = list(zip(*mirror))
#     vref = find_reflection(rotated_mirror)
#     vref = vref[0][0] if vref else 0

#     # print(f'vref: {vref}, href: {href}')
#     total += vref + 100 * href

result1 = total
aoc.print_result(1, result1, exp1)

# Part 2
total = 0
for mirror in mirrors:
    href = find_reflection(mirror)
    rotated_mirror = list(zip(*mirror))
    vref = find_reflection(rotated_mirror)

    hrefs, vrefs = set(), set()
    vref2, href2 = 0,0
    for i in range(len(mirror)):
        for j in range(len(mirror[0])):
            mirror[i][j] = '.' if mirror[i][j] == '#' else '#'
    
            href2 = find_reflection(mirror)

            rotated_mirror = list(zip(*mirror))
            vref2 = find_reflection(rotated_mirror)


            if href2:
                # print(f'\nh: ({i}, {j}) => {href2}')
                for h in href2:
                    hrefs.add(h)
                # for l in mirror:
                #     print(''.join(l))
                
            if vref2:
                for v in vref2:
                    vrefs.add(v)
                # print(f'v: ({i}, {j}) => {vref2}')
                
            mirror[i][j] = '.' if mirror[i][j] == '#' else '#'

            # if href2 or vref2:
            #     break

            # if (vref2 and not href2) or (href2 and not vref2):


    # print(f'subvref: {vref2}, subhref: {href2}')

    vref = set(vref)
    href = set(href)
    # print(f'hrefs {hrefs} href {href}')
    # print(f'vrefs {vrefs} href {vref}')

    vrefs -= vref
    hrefs -= href
    if len(vrefs) > 1 or len(hrefs) > 1:
        raise RuntimeError
    print(f'hrefs {hrefs} vrefs {vrefs}')
    href = list(hrefs)[0][0] if len(hrefs) else 0
    vref = list(vrefs)[0][0] if len(vrefs) else 0

    total += vref + 100 * href

result2 = total
aoc.print_result(2, result2, exp2)
