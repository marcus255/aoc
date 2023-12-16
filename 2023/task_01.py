import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 142, 281

mapping = {
    # Valid result for 'nineight' is '98', hence leaving last char unchanged
    'one': '1e',
    'two': '2o',
    'three': '3e',
    'four': '4r',
    'five': '5e',
    'six': '6x',
    'seven': '7n',
    'eight': '8t',
    'nine': '9e',
}
part_lines = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
# Part 1
aoc.mark_task_start()
total = 0
for line in part_lines:
    digits = list(filter(lambda x: x in '0123456789', line))
    if len(digits):
        total += int(digits[0] + digits[-1])


result1 = total
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
lines_converted = []
for line in lines:
    for i, c in enumerate(line):
        if i >= len(line):
            continue
        for k, v in mapping.items():
            try:
                index = line.index(k)
            except ValueError:
                index = -1
            if index == i:
                line = line.replace(k, v, 1)
                break
    lines_converted.append(line)

lines = lines_converted
total = 0
for line in lines:
    digits = list(filter(lambda char: char.isdigit(), line))
    total += (int(digits[0]) * 10 + int(digits[-1]))

result2 = total
aoc.print_result(2, result2, exp2)