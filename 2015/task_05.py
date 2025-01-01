import aoc
import re

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1, 2

# Common
VOVELS = 'aeiou'
EXCLUDED = ['ab', 'cd', 'pq', 'xy']
def check_sequence(seq):
    for ex in EXCLUDED:
        if ex in seq:
            return False
    vovels = sum([seq.count(v) for v in VOVELS if v in seq])
    if vovels < 3:
        return False
    for a, b in zip(seq, seq[1:]):
        if a == b:
            return True
    return False

def check_sequence_2(seq):
    # check if seq contains two non-overlapping subsequences of length 2
    for a, b in zip(seq, seq[1:]):
        subseq = a + b
        matches = [x.span() for x in re.finditer(subseq, seq)]
        if len(matches) >= 2:
            # If condition met, go to the next rule
            break
    else:
        return False
    # Check if seq contains XYX subsequence, examples: 'aba', 'aaa', 'hxh'
    for a, c in zip(seq, seq[2:]):
        if a == c:
            return True
    return False

# Part 1
aoc.mark_task_start()
for seq in lines:
    result1 += 1 if check_sequence(seq) else 0
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
if aoc.is_test_mode():
    lines = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
for seq in lines:
    result2 += 1 if check_sequence_2(seq) else 0
aoc.print_result(2, result2, exp2)
