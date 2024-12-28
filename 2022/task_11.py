import aoc
from copy import deepcopy
from functools import reduce

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 10605, 2713310158

# Common

# Input looks like this:
# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3
monkeys = []
monkey = {}
for line in lines:
    if 'Starting items: ' in line:
        items = line.split(': ')[1]
        monkey['items'] = [int(i) for i in items.split(', ')]
        monkey['inspections'] = 0
    elif 'Operation: ' in line:
        monkey['op'] = line.split(' = ')[1]
    elif 'Test: divisible by ' in line:
        monkey['div_by'] = int(line.split('divisible by ')[1])
    elif 'true' in line:
        monkey['throw_true'] = int(line.split('throw to monkey ')[1])
    elif 'false' in line:
        monkey['throw_false'] = int(line.split('throw to monkey ')[1])
    elif 'Monkey' in line and monkey:
        monkeys.append(monkey)
        monkey = {}
monkeys.append(monkey)

def run(monkeys, num_rounds, modulo=None, part2=False):
    for _ in range(num_rounds):
        for m in monkeys:
            items = m['items']
            for item in items:
                m['inspections'] += 1
                # m['op'] contains string like: 'old * 19', provide 'old' variable and evaluate the result
                old = item
                new_item = eval(m['op'])
                if not part2:
                    new_item //= 3
                throw_to = m['throw_true' if new_item % m['div_by'] == 0 else 'throw_false']
                if part2:
                    # For part 2, with larger number of rounds, we quickly fall into very big numbers
                    # However, the destination monkey number is based on new_item % m['div_by'] operation,
                    # so we can keep track only the number % (product of all div_by values)
                    new_item %= modulo
                monkeys[throw_to]['items'].append(new_item)
            m['items'] = []
    inspections = sorted([m['inspections'] for m in monkeys])
    return inspections[-1] * inspections[-2]

# Part 1
aoc.mark_task_start()
result1 = run(deepcopy(monkeys), 20)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
modulo = reduce(lambda x, y: x*y, [m['div_by'] for m in monkeys])
result2 = run(deepcopy(monkeys), 10_000, modulo, part2=True)
aoc.print_result(2, result2, exp2)
