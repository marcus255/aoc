import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 4, 3

# Common
containers = sorted(list(map(int, lines)), reverse=True)

def solve(containers, goal, depth=1, cont_count=None):
    global min_cont_count
    total = 0
    for i in range(len(containers)):
        cont = containers[i:]
        if sum(cont) < goal:
            break
        first, new_cont = cont[0], cont[1:]
        if first == goal:
            min_cont_count = min(min_cont_count, depth)
            if cont_count and depth != cont_count:
                continue
            total += 1
        elif first > goal:
            continue
        total += solve(new_cont, goal - first, depth + 1, cont_count)
    return total

# Part 1
aoc.mark_task_start()
liters = 25 if aoc.is_test_mode() else 150
min_cont_count = float('inf')
result1 = solve(containers, liters)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = solve(containers, liters, cont_count=min_cont_count)
aoc.print_result(2, result2, exp2)
