import aoc
import re
from aoc_utils import join_ranges

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 26, 56000011

# Common
# Line looks like this:
# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
r = re.compile(r'Sensor at x=(?P<x>-?\d+), y=(?P<y>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)')
sensors = {}
beacons_at_y = {}
for line in lines:
    x, y, bx, by = tuple(map(int, r.match(line).groups()))
    if by not in beacons_at_y:
        beacons_at_y[by] = set()
    beacons_at_y[by].add((bx, by))
    d = abs(x - bx) + abs(y - by)
    sensors[(x, y)] = ((x - d, y), (x + d, y), y - d, y + d)

def find_range_at_y(sensor, y):
    (lx, ly), (rx, ry), min_y, max_y = sensor
    if y < min_y or y > max_y:
        # Line y is outside of the sensor's range
        return None
    a = abs(y - ly)
    return lx + a, rx - a

# Part 1
aoc.mark_task_start()
Y_ROW = 10 if aoc.is_test_mode() else 2_000_000
values = set()
for sensor in sensors.values():
    x = find_range_at_y(sensor, Y_ROW)
    if not x:
        continue
    x1, x2 = x
    for i in range(x1, x2 + 1):
        # Creating such large sets is slow, but it will do for part 1
        values.add(i)
result1 = len(values) - len(beacons_at_y.get(Y_ROW, 0))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
XY_MAX = 20 if aoc.is_test_mode() else 4_000_000
y = XY_MAX
while True:
    ranges = []
    for sensor in sensors.values():
        x = find_range_at_y(sensor, y)
        if not x:
            continue
        ranges.append(x)
    ranges = join_ranges(ranges)
    if len(ranges) != 1:
        # It means there's no continuous range.
        # Make sure the gap is 1 element wide and get gap's value as x
        assert ranges[0][-1] + 2 == ranges[1][0]
        x = ranges[0][-1] + 1
        result2 = x * 4_000_000 + y
        break
    y -= 1

aoc.print_result(2, result2, exp2)
