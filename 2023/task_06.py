import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 288, 71503

line1 = ' '.join(lines[0].split())
line2 = ' '.join(lines[1].split())
times = [int(x) for x in line1.split(' ')[1:]]
distances = [int(x) for x in line2.split(' ')[1:]]

def get_better_scores(time, record):
    better_scores = 0
    for t in range(1, time + 1):
        d = (time - t) * t
        if d > record:
            better_scores += 1
    return better_scores

# Part 1
aoc.mark_task_start()
total = 1
for i in range(len(times)):
    total *= get_better_scores(times[i], distances[i])
result1 = total
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
time = int(''.join([str(x) for x in times]))
distance = int(''.join([str(x) for x in distances]))
result2 = get_better_scores(time, distance)
aoc.print_result(2, result2, exp2)
