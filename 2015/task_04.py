import aoc
from hashlib import md5

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 609043, 6742839

# Common
key = lines[0]

def find_number(start_seq):
    hash = None
    i = 0
    while True:
        hash = md5((key + str(i)).encode())
        if hash.hexdigest().startswith(start_seq):
            return i
        i += 1

# Part 1
aoc.mark_task_start()
result1 = find_number('00000')
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = find_number('000000')
aoc.print_result(2, result2, exp2)
