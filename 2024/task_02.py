import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 2, 4

# Common
sequences = []
for line in lines:
    sequences.append([int(x) for x in line.split(' ')])

def is_inc_or_dec(numbers):
    inc = numbers[1] > numbers[0]
    for i in range(len(numbers) - 1):
        local_inc = numbers[i + 1] > numbers[i]
        if local_inc != inc:
            return False
    return True

def get_incs(numbers):
    increments = []
    for i in range(len(numbers) - 1):
        increments.append(numbers[i + 1] - numbers[i])
    return increments

def get_abs_incs(numbers):
    return [abs(x) for x in get_incs(numbers)]

# Part 1
aoc.mark_task_start()
safe = []
for numbers in sequences:
    if not is_inc_or_dec(numbers):
        continue
    if not all([x in [1, 2, 3] for x in get_abs_incs(numbers)]):
        continue
    safe.append(numbers)

result1 = len(safe)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
safe = []
for numbers in sequences:
    if is_inc_or_dec(numbers) and all([x in [1, 2, 3] for x in get_abs_incs(numbers)]):
        safe.append(numbers)
        continue
    for i in range(len(numbers)):
        new_numbers = numbers[:i] + numbers[i + 1:]
        if is_inc_or_dec(new_numbers) and all([x in [1, 2, 3] for x in get_abs_incs(new_numbers)]):
            safe.append(new_numbers)
            break

result2 = len(safe)
aoc.print_result(2, result2, exp2)
