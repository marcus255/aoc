import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 103, 405

# Common
# Input lines look like this:
# Sue 1: goldfish: 6, trees: 9, akitas: 0
aunts = []
for line in lines:
    _, *items = line.split(': ')
    items = ":".join(items).split(', ')
    items = {k: int(v) for k, v in [item.split(':') for item in items]}
    aunts.append(items)

pattern = {
    'children': 3,  'cats': 7,      'samoyeds': 2,  'pomeranians': 3,   'akitas': 0,
    'vizslas': 0,   'goldfish': 5,  'trees': 3,     'cars': 2,          'perfumes': 1,
}

# Part 1
aoc.mark_task_start()
for i, aunt in enumerate(aunts, start=1):
    matches = 0
    for k, v in aunt.items():
        if k in pattern and v == pattern[k]:
            matches += 1
    if matches == 3:
        result1 = i
        break
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
greater_than = set(['cats', 'trees'])
fewer_than = set(['pomeranians', 'goldfish'])
for i, aunt in enumerate(aunts, start=1):
    matches = 0
    for k, v in aunt.items():
        if k in greater_than:
            if v > pattern[k]:
                matches += 1
        elif k in fewer_than:
            if v < pattern[k]:
                matches += 1
        elif v == pattern[k]:
            matches += 1
    if matches == 3:
        result2 = i
        break
aoc.print_result(2, result2, exp2)
