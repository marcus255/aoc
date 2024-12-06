import aoc
from collections import deque

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 143, 123

# Common
pages_started = False
rules, pages = [], []
for line in lines:
    if line == '':
        pages_started = True
        continue
    if pages_started:
        pages.append(line.split(','))
    else:
        k, v = line.split('|')
        rules.append((k, v))

def find_rules(rules, key, values):
    matching_rules = []
    for k, v in rules:
        if k == key and v in values:
            matching_rules.append((k, v))
    return matching_rules

# Part 1
aoc.mark_task_start()
incorrect_pages = []
for page in pages:
    page_valid = True
    for i in range(len(page)):
        if not page_valid:
            break
        for j in range(len(page)):
            if i == j or j < i:
                continue
            if (page[i], page[j]) not in rules:
                page_valid = False
                incorrect_pages.append(page)
                break
    if page_valid:
        result1 += int(page[len(page) // 2])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
incorrect_pages = deque(incorrect_pages)

while len(incorrect_pages):
    page = incorrect_pages.pop()
    page_valid = True
    rr = []
    for i in range(len(page)):
        r = find_rules(rules, page[i], page[:i] + page[i:])
        rr.append((page[i], len(r)))
        for j in range(len(page)):
            if i == j:
                continue
    rr.sort(key=lambda x: -x[1])
    result2 += int(rr[len(rr) // 2][0])
aoc.print_result(2, result2, exp2)
