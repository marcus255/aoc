import aoc
from collections import deque

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 26397, 288957

# Common
pairs_ltr = { '{': '}', '[': ']', '(': ')', '<': '>' }
pairs_rtl = { '}': '{', ']': '[', ')': '(', '>': '<' }

def check_sequence(seq, get_missing=False):
    queue = deque([])
    for c in seq:
        if c in pairs_rtl.values():
            queue.append(c)
        elif queue.pop() != pairs_rtl[c]:
                return c if not get_missing else None
    if get_missing:
        return [pairs_ltr[x] for x in list(queue)[::-1]]
    return None

# Part 1
aoc.mark_task_start()
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
for line in lines:
    c = check_sequence(line)
    result1 += points[c] if c else 0 
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
points = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for line in lines:
    chars = check_sequence(line, get_missing=True)
    if chars and isinstance(chars, list):
        score = 0
        for c in chars:
            score = score * 5 + points[c]
        scores.append(score)
result2 = sorted(scores)[len(scores) // 2]
aoc.print_result(2, result2, exp2)
