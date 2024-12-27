import aoc
import re
from copy import deepcopy

lines = aoc.get_lines(__file__, lstrip=False)
result1, result2 = 0, 0
exp1, exp2 = 'CMZ', 'MCD'

# Common
regex = re.compile(r'move (\d+) from (\d) to (\d)')
input_stacks = {}
instructions = []
for line in lines:
    if '[' in line:
        # transform '[A] --- [B] [C]' line into 'A - B C',
        # where '---' is the space where no container is present
        line = line.replace('[', '').replace(']', '').replace('    ', '  ')
        for i in range(len(line) // 2 + 1):
            if line[2 * i] != ' ':
                if i not in input_stacks:
                    input_stacks[i] = []
                input_stacks[i].append(line[2 * i])
    elif 'move' in line:
        m = regex.match(line)
        instructions.append(m.groups())

for stack in input_stacks.values():
    stack.reverse()

def get_top_containers(stacks, move_multiple=False):
    for count, src, dst in instructions:
        for _ in range(int(count)):
            src_stack = stacks[int(src) - 1]
            dst_stack = stacks[int(dst) - 1]
            if move_multiple:
                dst_stack.extend(src_stack[-int(count):])
                stacks[int(src) - 1] = src_stack[:-int(count)]
                break
            else:
                dst_stack.append(src_stack.pop())
    last_elems = [stacks[i][-1] for i in range(len(stacks))]
    return ''.join(last_elems)

# Part 1
aoc.mark_task_start()
result1 = get_top_containers(deepcopy(input_stacks))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = get_top_containers(deepcopy(input_stacks), move_multiple=True)
aoc.print_result(2, result2, exp2)
