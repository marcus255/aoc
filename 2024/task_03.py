import aoc
import re
lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 161, 48

# Common
text = ''.join(lines)

# Part 1
aoc.mark_task_start()
matches = re.findall('mul\(\d+,\d+\)', text, re.DOTALL)
sum = 0
for m in matches:
    _, nums = m.split('(')
    x, y = nums.split(',')
    y, _ = y.split(')')
    sum += (int(x) * int(y))

result1 = sum
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
# Different test vector for part 2
if aoc.is_test_mode():
    text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

matches = re.findall('don\'t\(\).+?do\(\)', text)
for m in matches:
    text = text.replace(m, '')

matches = re.findall('mul\(\d+,\d+\)', text)
sum = 0
for m in matches:
    _, a = m.split('(')
    x, y = a.split(',')
    y, _ = y.split(')')
    sum += (int(x) * int(y))

result2 = sum
aoc.print_result(2, result2, exp2)
