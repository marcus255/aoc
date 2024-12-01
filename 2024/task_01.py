import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 11, 31

# Common
a, b = [], []
for line in lines:
    aa, bb = line.split('   ')
    a.append(aa)
    b.append(bb)

# Part 1
aoc.mark_task_start()

a = sorted(a)
b = sorted(b)
distance = 0
for i in range(len(a)):
    distance += abs(int(a[i]) - int(b[i]))

result1 = distance
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
score = 0
for i in range(len(a)):
    score += int(a[i]) * b.count(a[i])

result2 = score
aoc.print_result(2, result2, exp2)
