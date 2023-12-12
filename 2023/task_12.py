import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 21, 525152

# Common
patterns = []
numbers = []
for line in lines:
    p, n = line.split(' ')
    n = [int(x) for x in n.split(',')]
    patterns.append(p)
    numbers.append(n)

def get_broken_spring_lengths(row):
    sizes = []
    broken_spring = False
    size = 0
    for c in row:
        if c == '#':
            if not broken_spring and size == 0:
                broken_spring = True
                size += 1

            elif broken_spring:
                size +=1
        elif c == '.' and size != 0:
            sizes.append(size)
            broken_spring = False
            size = 0
    if size != 0:
        sizes.append(size)
    return sizes

import itertools
num_matches = 0
for p, n in zip(patterns, numbers):

    unknown = p.count('?')
    possible = itertools.product('#.', repeat=unknown)
    # print(possible)
    for posib in possible:
        # print(posib)
        temp_str = p
        for pos in posib:
            temp_str = temp_str.replace('?', pos, 1)
        if get_broken_spring_lengths(temp_str) == n:
            # print(f'match: {"".join(posib)} {temp_str}, {p}, {n}')
            num_matches += 1
            
    print(p, n, get_broken_spring_lengths(p))
result1 = num_matches



# Part 1

aoc.print_result(1, result1, exp1)

# Part 2

aoc.print_result(2, result2, exp2)

for p, n in zip(patterns, numbers):
    p = '?'.join([p for _ in range(5)])
    orig_n = n[:]
    for x in range(4):
        n.extend(orig_n)

#   ???.### 1,1,3
#   .??..??...?##. 1,1,3
#   ?#?#?#?#?#?#?#? 1,3,1,6
#   ????.#...#... 4,1,1
#   ????.######..#####. 1,6,5
#   ?###???????? 3,2,1

#   #.#.### 1,1,3
#   .#...#....###. 1,1,3
#   .#.###.#.###### 1,3,1,6
#   ####.#...#... 4,1,1
#   #....######..#####. 1,6,5
#   .###.##....# 3,2,1