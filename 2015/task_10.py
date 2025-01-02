import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = '312211', 1166642

# Common
def transform(num):
    prev_c = num[0]
    subseqs = []
    subseq = ''
    for c in num:
        if c != prev_c:
            subseqs.append(subseq)
            subseq = ''
        subseq += c
        prev_c = c
    subseqs.append(subseq)
    new_str = ''
    for subseq in subseqs:
        new_str += str(len(subseq)) + subseq[0]
    return new_str

# Part 1
aoc.mark_task_start()
STEPS = 5 if aoc.is_test_mode() else 40
seq = lines[0]
for _ in range(STEPS):
    seq = transform(seq)
result1 = seq if aoc.is_test_mode() else len(seq)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
STEPS = 50
seq = lines[0]
for _ in range(STEPS):
    seq = transform(seq)
result2 = len(seq)
aoc.print_result(2, result2, exp2)
