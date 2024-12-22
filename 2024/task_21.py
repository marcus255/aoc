import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 126384, 1
sequences = lines

# Common
numpad_coords = {
    #    (r, c)
    'A': (3, 2),
    '0': (3, 1),  # +---+---+---+
    '1': (2, 0),  # | 7 | 8 | 9 |
    '2': (2, 1),  # +---+---+---+
    '3': (2, 2),  # | 4 | 5 | 6 |
    '4': (1, 0),  # +---+---+---+
    '5': (1, 1),  # | 1 | 2 | 3 |
    '6': (1, 2),  # +---+---+---+
    '7': (0, 0),  #     | 0 | A |
    '8': (0, 1),  #     +---+---+
    '9': (0, 2),
}

U_KEY, L_KEY, D_KEY, R_KEY, A_KEY = (0, 1), (1, 0), (1, 2), (2, 1), (0, 2)
UP_DIR, LEFT_DIR, DOWN_DIR, RIGHT_DIR = (-1, 0), (0, -1), (1, 0), (0, 1)
ARROWS = {U_KEY: '^', L_KEY: '<', D_KEY: 'v', R_KEY: '>', A_KEY: 'A'}

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
keypad_transitions = { # Value must be a tuple, hence the comma
#   (from, to): (step1, step2, ...)
    (U_KEY, L_KEY): [(D_KEY, L_KEY)],
    (U_KEY, R_KEY): [(D_KEY, R_KEY), (R_KEY, D_KEY)],
    (U_KEY, D_KEY): [(D_KEY,)],
    (U_KEY, A_KEY): [(R_KEY,)],
    (U_KEY, U_KEY): [],

    (L_KEY, U_KEY): [(R_KEY, U_KEY)],
    (L_KEY, R_KEY): [(R_KEY, R_KEY)],
    (L_KEY, D_KEY): [(R_KEY,)],
    (L_KEY, A_KEY): [(R_KEY, R_KEY, U_KEY), (R_KEY, U_KEY, R_KEY)],
    (L_KEY, L_KEY): [],

    (R_KEY, U_KEY): [(L_KEY, U_KEY), (U_KEY, L_KEY)],
    (R_KEY, L_KEY): [(L_KEY, L_KEY)],
    (R_KEY, D_KEY): [(L_KEY,)],
    (R_KEY, A_KEY): [(U_KEY,)],
    (R_KEY, R_KEY): [],

    (D_KEY, U_KEY): [(U_KEY,)],
    (D_KEY, L_KEY): [(L_KEY,)],
    (D_KEY, R_KEY): [(R_KEY,)],
    (D_KEY, A_KEY): [(U_KEY, R_KEY), (R_KEY, U_KEY)],
    (D_KEY, D_KEY): [],

    (A_KEY, U_KEY): [(L_KEY,)],
    (A_KEY, L_KEY): [(D_KEY, L_KEY, L_KEY), (L_KEY, D_KEY, L_KEY)],
    (A_KEY, D_KEY): [(D_KEY, L_KEY), (L_KEY, D_KEY)],
    (A_KEY, D_KEY): [(D_KEY, L_KEY)],
    (A_KEY, R_KEY): [(D_KEY,)],
    (A_KEY, A_KEY): [],
}

START_NUM_POS = numpad_coords['A']
START_ARROW_POS = A_KEY

from itertools import permutations
def get_arrows(curr_pos, next_pos):
    dirs = []
    # print(f'curr_pos: {curr_pos}, next_pos: {next_pos}')
    if curr_pos == next_pos:
        raise Exception(f"Same position: {curr_pos}")
    dr, dc = next_pos[0] - curr_pos[0], next_pos[1] - curr_pos[1]
    dirs = [D_KEY if dr > 0 else U_KEY] * abs(dr) + [R_KEY if dc > 0 else L_KEY] * abs(dc)
    all_dirs = list(set(permutations(dirs)))
    dirs = []
    for d in all_dirs:
        if curr_pos == numpad_coords['0']:
            if d[0] == (L_KEY):
                continue
        elif curr_pos == numpad_coords['A']:
            if d[:2] == (L_KEY, L_KEY):
                continue
        elif next_pos == numpad_coords['A']:
            if d[-2:] == (R_KEY, R_KEY):
                continue
        elif next_pos == numpad_coords['0']:
            if d[-1] == (R_KEY):
                continue
        dirs.append(d)
    return dirs

def get_arrows_for_numbers(sequence):
    keypad_seqs = []
    queue = [(START_NUM_POS, sequence[:], [])]
    while queue:
        pos_from, rest, arrows = queue.pop(0)
        if not rest:
            keypad_seqs.append(arrows)
            continue
        pos_to = numpad_coords[rest[0]]
        dirs = get_arrows(pos_from, pos_to)
        # print(f'{rest[0]}: pos_from: {pos_from}, pos_to: {pos_to}, dirs: {dirs}')
        for d in dirs:
            queue.append((pos_to, rest[1:], arrows + list(d) + [A_KEY]))
    return keypad_seqs

def get_arrows_for_arrows(sequence):
    # print(f'arrow sequence: {sequence}')
    arrow_seqs = []
    queue = [(START_ARROW_POS, sequence[:], [])]
    while queue:
        pos_from, rest, arrows = queue.pop(0)
        if not rest:
            # print(f'pos_from: {pos_from}, arrows: {arrows}')
            arrow_seqs.append(arrows)
            continue
        pos_to = rest[0]
        dirs = keypad_transitions[(pos_from, pos_to)]
        # print(f'{rest[0]}: pos_from: {pos_from}, pos_to: {pos_to}, dirs: {dirs}')
        for d in dirs:
            # print(f'pos_from: {pos_from}, pos_to: {pos_to}, d: {d}')
            queue.append((pos_to, rest[1:], arrows + list(d) + [A_KEY]))
        if not dirs:
            queue.append((pos_to, rest[1:], arrows + [A_KEY]))
    return arrow_seqs

from heapq import heappop, heappush

def solve(arrows):
    queue = []
    lengths = []
    STEPS_LEFT = 2
    for sequence in arrows:
        start_cost = len(sequence)
        heappush(queue, (start_cost, STEPS_LEFT, sequence))
    while queue:
        cost, steps_left, sequence = heappop(queue)
        # print(f'cost: {cost}, seq: {sequence}')
        if steps_left == 0:
            # print(f'cost: {cost}, sequence: {sequence}')
            lengths.append(len(sequence))
            continue
        seqs = get_arrows_for_arrows(sequence)
        for seq in seqs:
            new_cost = cost + len(seq)
            heappush(queue, (new_cost, steps_left - 1, seq))
    return min(lengths)

# Part 1
aoc.mark_task_start()
result1 = 0
for sequence in sequences:
    arrows = get_arrows_for_numbers(sequence)
    min_len = solve(arrows)
    result1 += min_len * int(sequence.replace('A', ''))
    # print(f'{sequence} shortest seq length: {min_len}')
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()



aoc.print_result(2, result2, exp2)

