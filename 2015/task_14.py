import aoc
import re

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1120, 689

# Common
check_t = 1000 if aoc.is_test_mode() else 2503
# Input lines look like this:
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
r = re.compile(r'.+?(\d+).+?(\d+).+?(\d+).+')
reindeers = []
for line in lines:
    speed, fly_time, rest_time = list(map(int, r.match(line).groups()))
    reindeers.append((speed, fly_time, rest_time))

def get_distance(speed, fly_time, rest_time, check_time):
    cycle_time = fly_time + rest_time
    cycles = check_time // cycle_time
    time_remaining = check_time % cycle_time
    main_distance = speed * fly_time * cycles
    partial_distance = speed * min(time_remaining, fly_time)
    return main_distance + partial_distance

# Part 1
aoc.mark_task_start()
result1 = max([get_distance(speed, fly_t, rest_t, check_t) for speed, fly_t, rest_t in reindeers])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
scores = [0 for _ in reindeers]
for t in range(1, check_t + 1):
    distances = [get_distance(speed, fly_t, rest_t, t) for speed, fly_t, rest_t in reindeers]
    max_d = max(distances)
    for i, d in enumerate(distances):
        if d == max_d:
            scores[i] += 1
result2 = max(scores)
aoc.print_result(2, result2, exp2)
