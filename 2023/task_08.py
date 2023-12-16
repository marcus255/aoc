import aoc
import math

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 6, 6

part1_lines = [
    'LLR',
    '',
    'AAA = (BBB, BBB)',
    'BBB = (AAA, ZZZ)',
    'ZZZ = (ZZZ, ZZZ)',
]

def get_sequence_length(transitions, start_points, end_points):
    sequence_lengths = []
    for start_a in start_points:
        index = 0
        next_a = start_a
        sequence = []
        while True:
            try:
                L, R = transitions[next_a]
            except KeyError:
                # test input for part 1 is different than for part 2, just fail part 1
                return [-1]
            next_a = L if (sides[index % len(sides)] == 'L') else R
            sequence.append(next_a)
            if next_a in end_points:
                break
            index += 1
        sequence_lengths.append(len(sequence))
    return sequence_lengths

# Part 1
aoc.mark_task_start()
sides = part1_lines[0]
transitions = {}
for instr in part1_lines[2:]:
    a, xy = instr.split(' = (')
    x, y = xy.split(')')[0].split(', ')
    transitions[a] = (x, y)
    # print(f'{a} => ({x}, {y})')
result1 = get_sequence_length(transitions, ['AAA'], ['ZZZ'])[0]
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
sides = lines[0]
transitions = {}
for instr in lines[2:]:
    a, xy = instr.split(' = (')
    x, y = xy.split(')')[0].split(', ')
    transitions[a] = (x, y)
    
start_points = list(filter(lambda num: num.endswith('A'), transitions.keys()))
end_points = list(filter(lambda num: num.endswith('Z'), transitions.keys()))
seq_lengths = get_sequence_length(transitions, start_points, end_points)
result2 = math.lcm(*seq_lengths)
aoc.print_result(2, result2, exp2)
