import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 26, 61229

info = []
# Common
for line in lines:
    left, right = line.split(' | ')
    left = list(map(lambda x: ''.join(sorted(x)), left.split(' ')))
    right = list(map(lambda x: ''.join(sorted(x)), right.split(' ')))
    info.append((left, right))

# Number 1: [2, 5]                  # unique: 2 segments
# Number 7: [0, 2, 5]               # unique: 3 segments
# Number 4: [1, 2, 3, 5]            # unique: 4 segments
# Number 2: [0, 2, 3, 4, 6]       ###
# Number 3: [0, 2, 3, 5, 6]         # 5 segments
# Number 5: [0, 1, 3, 5, 6]       ###
# Number 0: [0, 1, 2, 4, 5, 6]    ###
# Number 6: [0, 1, 3, 4, 5, 6]      # 6 segments
# Number 9: [0, 1, 2, 3, 5, 6]    ###
# Number 8: [0, 1, 2, 3, 4, 5, 6]   # unique: 7 segments

def decode_wires(numbers):
    numbers.sort(key=len)
    # assign known numbers: 1, 4, 7, 8
    digits = ['' for _ in range(10)]
    digits[1] = numbers[0]
    digits[4] = numbers[2]
    digits[7] = numbers[1]
    digits[8] = numbers[9]

    numbers = set(numbers) - set(digits)

    # Find number 9 by checking which number contains sum of 4 and 7 segments
    digits[9] = list(filter(lambda n: (set(digits[4]) | set(digits[7])).issubset(set(n)), numbers))[0]
    numbers -= set(digits)
    
    # Find number 0, which has 6 segments and contains segments of 1.
    # The other 6 segment digit is then number 6
    for n in [x for x in numbers if len(x) == 6]:
        contains_one = set(digits[1]).issubset(set(n))
        digits[0 if contains_one else 6] = n
    numbers -= set(digits)
    
    # Now only 3 more digits remain, all of length 5.
    # Find number 3, as it is the only one to contain number 1
    digits[3] = list(filter(lambda n: set(digits[1]).issubset(set(n)), numbers))[0]
    numbers -= set(digits)
    
    # Now only 5 and 2 remain. Segments of number 5 are contained in segments of number 6.
    # The other number 5 segment digit is then number 2
    for n in numbers:
        subset_of_six = set(n).issubset(set(digits[6]))
        digits[5 if subset_of_six else 2] = n
    numbers -= set(digits)

    # No more numbers should be left
    if len(numbers):
        raise ValueError

    return {v: str(k) for k, v in enumerate(digits)}

# Part 1
aoc.mark_task_start()
unique_lens = [2, 3, 4, 7]
for _, output in info:
    result1 += len([x for x in output if len(x) in unique_lens])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
for input, output in info:
    mapping = decode_wires(input)
    result2 += int(''.join([mapping[x] for x in output]))
aoc.print_result(2, result2, exp2)
