import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 11, 26

# Common
def find_marker_position(seq, marker_len):
    for i in range(len(seq) - marker_len + 1):
        subseq = seq[i:i+marker_len]
        if len(set(subseq)) == marker_len:
            return i + marker_len

# Part 1
aoc.mark_task_start()
result1 = find_marker_position(lines[0], 4)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = find_marker_position(lines[0], 14)
aoc.print_result(2, result2, exp2)
