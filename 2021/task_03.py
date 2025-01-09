import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 198, 230

# Common
numbers = []
for line in lines:
    numbers.append(list(line))

def find_num(nums, most=True):
    c = 0
    while len(nums) > 1:
        ones = [nums[r][c] for r in range(len(nums))].count('1')
        zeros = len(nums) - ones
        condition = zeros > ones if most else ones >= zeros
        nums = [n for n in nums if n[c] == ('0' if condition else '1')]
        c += 1
    return int(''.join(nums[0]), base=2)

# Part 1
aoc.mark_task_start()
least, most = '', ''
for v_num in zip(*numbers):
    ones = v_num.count('1')
    zeros = len(numbers) - ones
    most += '1' if ones > zeros else '0'
    least += '0' if ones > zeros else '1'
result1 = int(most, base=2) * int(least, base=2)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = find_num(numbers[:]) * find_num(numbers[:], most=False)
aoc.print_result(2, result2, exp2)
