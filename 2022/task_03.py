import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 157, 70

# Common
def get_score(chars):
    result = 0
    for c in chars:
        if c.islower():
            result += ord(c) - ord('a') + 1
        else:
            result += ord(c) - ord('A') + 1 + 26
    return result

# Part 1
aoc.mark_task_start()
common_chars = []
for line in lines:
    half = len(line) // 2
    a, b = line[:half], line[half:]
    common_chars.append(list(set.intersection(set(a), set(b)))[0])
result1 = get_score(common_chars)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
groups = []
for i, line in enumerate(lines):
    group_i = i // 3
    if len(groups) <= group_i:
        groups.append([])
    groups[group_i].append(line)
common_chars = []
for group in groups:
    common_chars.append(list(set.intersection(*[set(g) for g in group]))[0])
result2 = get_score(common_chars)
aoc.print_result(2, result2, exp2)
