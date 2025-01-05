import aoc
import re

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 62842880, 57600000

# Common
# Input lines look like this:
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
r = re.compile(r'([A-Za-z]+).+?(-?\d+).+?(-?\d+).+?(-?\d+).+?(-?\d+).+?(-?\d+)')
items = []
for line in lines:
    name, *params = r.match(line).groups()
    items.append(tuple(map(int, params)))
TEASPUN_COUNT = 100
DESIRED_CALORIES = 500

def find_best(ingredients, spoons_left, props, ing_index, exp_cal=None):
    ing = ingredients[ing_index]
    best = 0
    for spoons in range(1, spoons_left +  1):
        new_props = a, b, c, d, e = [prop + spoons * ing[prop_i] for prop_i, prop in enumerate(props)]
        if ing_index + 1 == len(ingredients):
            # All ingredients added
            if exp_cal and e != exp_cal:
                continue
            best = max(best, max(0, a) * max(0, b) * max(0, c) * max(0, d))
        else:
            # Decrease spoons_left and add another ingredient
            best = max(best, find_best(ingredients, spoons_left - spoons, new_props, ing_index + 1, exp_cal))
    return best

# Part 1
aoc.mark_task_start()
result1 = find_best(items, TEASPUN_COUNT, (0, 0, 0, 0, 0), 0)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = find_best(items, TEASPUN_COUNT, (0, 0, 0, 0, 0), 0, DESIRED_CALORIES)
aoc.print_result(2, result2, exp2)
