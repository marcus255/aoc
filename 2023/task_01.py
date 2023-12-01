with open('input_01.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

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

# Part 2
lines = lines_converted

total = 0
for line in lines:
    digits = list(filter(lambda char: char.isdigit(), line))
    total += (int(digits[0]) * 10 + int(digits[-1]))

print(f'Total: {total}')