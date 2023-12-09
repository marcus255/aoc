import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 114, 2

def extend(line):
    extended = [line]
    for row in range(len(line) - 1):
        new_line = []
        for col in range(len(line) - 1 - row):
            new_line.append(extended[row][col + 1] - extended[row][col])
        extended.append(new_line)
        if not len(list(filter(lambda x: x != 0, new_line))):
            break
    return extended

def find_value(extended, extend_right=True):
    prev_val, val = 0, 0
    for line in extended[::-1]:
        val = (prev_val + line[-1]) if extend_right else (line[0] - prev_val)
        prev_val = val
    return val

for i, line in enumerate(lines):
    line = line.split(' ')
    line = [int(x) for x in line]
    lines[i] = line

# Part 1
for numbers in lines:
    result1 += find_value(extend(numbers))
aoc.print_result(1, result1, exp1)

# Part 2
for numbers in lines:
    result2 += find_value(extend(numbers), False)
aoc.print_result(2, result2, exp2)
