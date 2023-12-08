import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1, 6

instructions = lines[0]
mapping = {}
for line in lines[2:]:
    a, xy = line.split(' = (')
    x, y = xy.split(')')[0].split(', ')
    if a in mapping:
        raise RuntimeError('a already in mapping')
    mapping[a] = (x, y)
    # print(a, x, y)

# next_inst = 'AAA'
# result1 = 0
# while next_inst != 'ZZZ':
#     for inst in instructions:
#         m = mapping[next_inst]
#         next_inst = m[0] if inst == 'L' else m[1]
#         result1 += 1

# aoc.print_result(1, result1, exp1)

# Part 2

next_points = []
for next in mapping.keys():
    if next.endswith('A'):
        next_points.append(next)
end_points = []
for end in mapping.keys():
    if end.endswith('Z'):
        end_points.append(end)
print(end_points)

l_map = {k: v[0] for k, v in mapping.items()}
r_map = {k: v[1] for k, v in mapping.items()}

result2 = 0
all_end_z = False
while True:
    for inst in instructions:
        new_next_points = next_points[:]
        next_points = [l_map[n] if inst == 'L' else r_map[n] for n in next_points]
        result2 += 1
        # end_z = 0
        # for p in next_points:
        #     if p.endswith('Z'):
        #         end_z += 1
        # all_end_z = end_z == len(end_points)
        all_end_z = True
        for p in next_points:
            if not p.endswith('Z'):
                all_end_z = False
                break
        if all_end_z:
            break
    if all_end_z:
        break
    if not result2 % (1024*8):
        print(result2, next_points)
    # if end_z > 2:
    #     print(result2, next_points, end_z)

aoc.print_result(2, result2, exp2)
