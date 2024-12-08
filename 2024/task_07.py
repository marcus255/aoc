import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 3749, 11387

# Common
nums = []
for line in lines:
    k, v = line.split(': ')
    nums.append((int(k), [int(x) for x in v.split(' ')]))

# Part 1
aoc.mark_task_start()
sum_of_matched = 0
for k, v in nums:
    # opertions
    for i in range(2**(len(v)-1)):
        # numbers
        result = v[0]
        for j in range(1, len(v)):
            if (i >> (j-1)) & 1:
                result += v[j]
            else:
                result *= v[j]
        if result == k:
            sum_of_matched += result
            break
result1 = sum_of_matched
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
def check_result(exp_result, curr_result, numbers):
    if not len(numbers):
        return curr_result == exp_result
    mult = check_result(exp_result, curr_result * numbers[0], numbers[1:])
    add = check_result(exp_result, curr_result + numbers[0], numbers[1:])
    concat = check_result(exp_result, int(str(curr_result) + str(numbers[0])), numbers[1:])
    return any([mult, add, concat])

sum_of_matched = 0
for exp_result, nums in nums:
    if check_result(exp_result, nums[0], nums[1:]):
        sum_of_matched += exp_result

result2 = sum_of_matched
aoc.print_result(2, result2, exp2)
