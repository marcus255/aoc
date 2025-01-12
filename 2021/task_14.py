import aoc
from collections import Counter
from functools import cache

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1588, 2188189693529

# Common
template = lines[0]
pairs = {k: v for k, v in (x.split(' -> ') for x in lines[2:])}

def process_polymer(template, pairs):
    polymer = template[0]
    for a, b in zip(template, template[1:]):
        polymer += pairs[a + b] + b
    return polymer

@cache
def insert_char(a, b):
    # Use pairs as global to enable caching
    global pairs
    middle = pairs[a + b]
    return a + middle, middle + b

# Part 1
aoc.mark_task_start()
polymer = template
for _ in range(10):
    polymer = process_polymer(polymer, pairs)
counter = list(Counter(polymer).most_common())
result1 = counter[0][1] - counter[-1][1]
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
# Instead of keeping track of all letters, track number of 2-char sequences,
# which will repeat over time. Each 2-char sequence will produce 2 new 2-char sequences
seqs = {}
for a, b in zip(template, template[1:]):
    seqs[a + b] = seqs.get(a + b, 0) + 1
for _ in range(40):
    new_seqs = {}
    for (a, b), v in seqs.items():
        s1, s2 = insert_char(a, b)
        new_seqs[s1] = new_seqs.get(s1, 0) + v
        new_seqs[s2] = new_seqs.get(s2, 0) + v
    seqs = new_seqs
# Count the letters in each pair and reduce it to single dict
letters = {}
for (a, b), v in seqs.items():
    letters[a] = letters.get(a, 0) + v
    letters[b] = letters.get(b, 0) + v
# First and last characters of the final sequence are not part of any pair,
# add 1 for first and last letters of template sequence to account for that
letters[template[0]] += 1
letters[template[-1]] += 1
counter = list(Counter(letters).most_common())
# Each letter is counted twice, as it is always in two connected pairs, so divede by 2
result2 = counter[0][1] // 2 - counter[-1][1] // 2
aoc.print_result(2, result2, exp2)
