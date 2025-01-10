import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 5934, 26984457539

# Common
fish = {}
for number in map(int, lines[0].split(',')):
    fish.setdefault(number, 0)
    fish[number] += 1

def get_fish_count(fish, days):
    for _ in range(days):
        new_fish = {}
        for k, v in fish.items():
            if k > 0:
                new_fish.setdefault(k - 1, 0)
                new_fish[k - 1] += v
            else:
                new_fish.setdefault(6, 0)
                new_fish[6] += v
                new_fish.setdefault(8, 0)
                new_fish[8] += v
        fish = new_fish
    return sum(fish.values())

# Part 1
aoc.mark_task_start()
result1 = get_fish_count(fish, days=80)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = get_fish_count(fish, days=256)
aoc.print_result(2, result2, exp2)
