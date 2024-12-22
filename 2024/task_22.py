import aoc
from collections import Counter

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 37327623, 23

# Common
numbers = list(map(int, lines))
COUNT = 2000

def get_next_secret_num(num):
    num ^= (num * 64)
    num %= 16777216
    num ^= (num // 32)
    num %= 16777216
    num ^= (num * 2048)
    num %= 16777216
    return num

def get_secret_nums(numbers):
    secret_nums = []
    for num in numbers:
        nums = []
        for _ in range(COUNT + 1):
            next_num = get_next_secret_num(num)
            nums.append((num, num % 10))
            num = next_num
        secret_nums.append(nums)
    return secret_nums

def get_all_diffs(secret_nums):
    all_diffs = []
    for num in secret_nums:
        diffs = []
        for j in range(1, COUNT):
            diffs.append((num[j][1]) - (num[j - 1][1]))
        all_diffs.append(diffs)
    return all_diffs

def get_all_diff_seqs(all_diffs):
    all_diff_seqs = []
    for j in range(COUNT - 3):
        for i in range(len(all_diffs)):
            all_diff_seqs.append(tuple(all_diffs[i][j:j + 4]))
    return all_diff_seqs

# Part 1
aoc.mark_task_start()
secret_nums = get_secret_nums(numbers)
result1 = sum([secret_nums[i][-1][0] for i in range(len(secret_nums))])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
numbers = [1, 2, 3, 2024] if aoc.is_test_mode() else numbers
secret_nums = get_secret_nums(numbers)
all_diffs = get_all_diffs(secret_nums)
all_diff_seqs = get_all_diff_seqs(all_diffs)

NUM_MOST_COMMON = 200 if aoc.is_test_mode() else 2
counter = Counter(all_diff_seqs)
most_common_seqs = list(counter.most_common(NUM_MOST_COMMON))[1:] # First most common will be [0, 0, 0, 0], ignore it
most_common_seqs = map(lambda x: list(x[0]), most_common_seqs)

result2 = 0
for most_common_seq in most_common_seqs:
    totals = []
    for i, num in enumerate(numbers):
        for j in range(COUNT - 4):
            if all_diffs[i][j:j+4] == most_common_seq:
                totals.append(secret_nums[i][j+4][1])
                break
    if sum(totals) > result2:
        result2 = sum(totals)

aoc.print_result(2, result2, exp2)
