import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1, 1

sequence = lines[0].split(',')

# Common
def get_hash(text):
    current_value = 0
    for t in text:
        current_value += ord(t)
        current_value *= 17
        current_value %= 256
    return current_value

# Part 1
total = 0
for s in sequence:
    total += get_hash(s)

result1 = total
aoc.print_result(1, result1, exp1)

# Part 2
boxes = [[] for _ in range(256)]
for s in sequence:
    
    if '=' in s:
        operation, focal = s.split('=')
        box_num = get_hash(operation)
        op_found = False
        for i, (op, foc) in enumerate(boxes[box_num]):
            if op == operation:
                boxes[box_num][i] = (operation, focal)
                op_found = True
                break
        if not op_found:
            boxes[box_num] = list(filter(lambda x: x[0] != operation, boxes[box_num]))
            boxes[box_num].append((operation, focal))
    else:
        operation = s[:-1]
        box_num = get_hash(operation)
        boxes[box_num] = list(filter(lambda x: x[0] != operation, boxes[box_num]))

for i, box in enumerate(boxes):
    if not box:
        continue
    print(f'\n{i}: ', end='')
    for lense in box:
        print(f'[{lense[0]} {lense[1]}]', end = '')
print()

power = 0
for i, box in enumerate(boxes):
    if not box:
        continue
    box_power = 0
    for j, (_, lense) in enumerate(box):
        box_power += (i + 1) * (j + 1) * int(lense)
    print(f'power {i}: {box_power}')
    power += box_power

result2 = power
aoc.print_result(2, result2, exp2)
