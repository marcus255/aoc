import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 198, 1

# Common
numbers = []
for line in lines:
    numbers.append(list(line))

# Part 1
aoc.mark_task_start()
least, most = '', ''
for v_num in zip(*numbers):
    ones = v_num.count('1')
    zeros = len(numbers) - ones
    
    most += '1' if ones > zeros else '0'
    least += '0' if ones > zeros else '1'

result1 = int(most, base=2) * int(least, base=2)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()



aoc.print_result(2, result2, exp2)
