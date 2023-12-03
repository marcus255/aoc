with open('input_03.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

symbols = list('*%@#+$-=/&')

symbol_positions = {}
for i, line in enumerate(lines):
    symbol_positions[i] = []
    for s in symbols:
        try:
            index = -1
            while index < len(line):
                index = line.index(s, index + 1)
                symbol_positions[i].append(index)
        except ValueError:
            pass

total = 0
for i, line in enumerate(lines):
    numbers_line = line
    for s in symbols:
        numbers_line = numbers_line.replace(s, '.')
    # print(numbers_line)
    numbers = numbers_line.split('.')
    numbers = list(filter(lambda elem: len(elem), numbers))
    # print(numbers)
    search_index = -1
    for number in numbers:
        # print(f'Number: {number}')

        start_index = numbers_line.index(number, search_index  + 1)
        search_index = start_index
        start_index = start_index - 1 if start_index != 0 else 0
        end_index = start_index + len(number)
        end_index = end_index + 1 if end_index != (len(numbers_line) -1) else (len(numbers_line) - 1)
        match = False
        for position in symbol_positions[i]:
            if start_index <= position <= end_index:
                # print(f'i Line {i}: {number} | {position} {start_index}-{end_index}')
                total += int(number)
                match = True
                break
        if match:
            continue

        prev_i = i - 1
        if prev_i >= 0:
            match = False
            for position in symbol_positions[i-1]:
                if start_index <= position <= end_index:
                    # print(f'i-1 Line {i}: {number} | {position} {start_index}-{end_index}')
                    total += int(number)
                    match = True
                    break
        if match:
            continue
            

        next_i = i + 1
        if next_i < len(lines):
            match = False
            for position in symbol_positions[i+1]:
                if start_index <= position <= end_index:
                    # print(f'i+1 Line {i}: {number} | {position} {start_index}-{end_index}')
                    total += int(number)
                    match = True
                    break
        if match:
            continue

print(total)

# Part 2
star_coords = [] # this will hold coordinates of cells adjacent to stars: (x, y)
for i, line in enumerate(lines):
    star_index = -1
    while star_index < len(line):
        try:
            star_index = line.index('*', star_index + 1)
        except ValueError:
            break
        adjacent_elems = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                coordinates = (i + y, star_index + x)
                adjacent_elems.append(coordinates)
        star_coords.append(adjacent_elems)

# for s in star_coords:
#     print(s)


all_indexes = []
for j, l in enumerate(line):
    all_indexes.append(j)

numbers_coords = {} # this will hold coordinates of with numbers: (x, y)
for i, line in enumerate(lines):
    numbers_line = line
    for s in symbols:
        numbers_line = numbers_line.replace(s, '.')
    # print(numbers_line)

    dot_indexes = []
    index = -1
    try:
        while index < len(numbers_line):
            index = numbers_line.index('.', index + 1)
            dot_indexes.append(index)
    except ValueError:
        pass

    skip_next = False
    for x in range(len(numbers_line)):
        if x in dot_indexes:
            skip_next = False
        if x not in dot_indexes and not skip_next:
            number = numbers_line[x:].split('.')[0]
            for width in range(len(number)):
                numbers_coords[(i, x + width)] = number
            skip_next = True

for k, v in numbers_coords.items():
    print(f'{k} => {v}')

def get_unique_adjacent_nums(star_coords):
    adjacent_nums = []
    for xy in star_coords:
        try:
            adjacent_nums.append(numbers_coords[xy])
        except KeyError:
            continue
    adjacent_nums = list(set(adjacent_nums))
    # print(adjacent_nums)
    return adjacent_nums

total = 0
for coord in star_coords:
    nums = get_unique_adjacent_nums(coord)
    if len(nums) != 2:
        print(f'Skipping: {len(nums)}')
        continue
    total += (int(nums[0]) * int(nums[1]))
    # print(f'{coord} => {nums}')

print(f'Total: {total}')