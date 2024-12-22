import aoc
from functools import cache
from itertools import permutations

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 126384, 154115708116294
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
START_NUM_POS = numpad_coords['A']
START_ARROW_POS = A_KEY

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
arrow_moves = {
#   (from,  to)   : [step1, step2, ..., A_KEY]
    (U_KEY, L_KEY): [[D_KEY, L_KEY, A_KEY]],
    (U_KEY, R_KEY): [[D_KEY, R_KEY, A_KEY], [R_KEY, D_KEY, A_KEY]],
    (U_KEY, D_KEY): [[D_KEY, A_KEY]],
    (U_KEY, A_KEY): [[R_KEY, A_KEY]],
    (U_KEY, U_KEY): [[A_KEY,]],

    (L_KEY, U_KEY): [[R_KEY, U_KEY, A_KEY]],
    (L_KEY, R_KEY): [[R_KEY, R_KEY, A_KEY]],
    (L_KEY, D_KEY): [[R_KEY, A_KEY]],
    (L_KEY, A_KEY): [[R_KEY, R_KEY, U_KEY, A_KEY], [R_KEY, U_KEY, R_KEY, A_KEY]],
    (L_KEY, L_KEY): [[A_KEY]],

    (R_KEY, U_KEY): [[L_KEY, U_KEY, A_KEY], [U_KEY, L_KEY, A_KEY]],
    (R_KEY, L_KEY): [[L_KEY, L_KEY, A_KEY]],
    (R_KEY, D_KEY): [[L_KEY, A_KEY]],
    (R_KEY, A_KEY): [[U_KEY, A_KEY]],
    (R_KEY, R_KEY): [[A_KEY]],

    (D_KEY, U_KEY): [[U_KEY, A_KEY]],
    (D_KEY, L_KEY): [[L_KEY, A_KEY]],
    (D_KEY, R_KEY): [[R_KEY, A_KEY]],
    (D_KEY, A_KEY): [[U_KEY, R_KEY, A_KEY], [R_KEY, U_KEY, A_KEY]],
    (D_KEY, D_KEY): [[A_KEY]],

    (A_KEY, U_KEY): [[L_KEY, A_KEY]],
    (A_KEY, L_KEY): [[D_KEY, L_KEY, L_KEY, A_KEY], [L_KEY, D_KEY, L_KEY, A_KEY]],
    (A_KEY, D_KEY): [[D_KEY, L_KEY, A_KEY], [L_KEY, D_KEY, A_KEY]],
    (A_KEY, R_KEY): [[D_KEY, A_KEY]],
    (A_KEY, A_KEY): [[A_KEY]],
}
arrow_moves_lengths = {k: len(v[0]) for k, v in arrow_moves.items()}

def get_arrows(current, next):
    dirs = []
    dr, dc = next[0] - current[0], next[1] - current[1]
    dirs = [D_KEY if dr > 0 else U_KEY] * abs(dr) + [R_KEY if dc > 0 else L_KEY] * abs(dc)
    all_dirs = list(set(permutations(dirs)))
    dirs = []
    for d in all_dirs:
        if any([
            current == numpad_coords['0'] and d[0] == (L_KEY),
            current == numpad_coords['A'] and d[:2] == (L_KEY, L_KEY),
            next == numpad_coords['0'] and d[-1] == (R_KEY),
            next == numpad_coords['A'] and d[-2:] == (R_KEY, R_KEY),
        ]):
            # Skip invalid moves, i.e. moves over empty key on the left of '0' key
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
        for d in dirs:
            queue.append((pos_to, rest[1:], arrows + list(d) + [A_KEY]))
    return keypad_seqs

@cache
def get_len(start, end, iteration):
    if iteration == 1:
        return arrow_moves_lengths[(start, end)]
    shortest = 1e12
    for seq in arrow_moves[(start, end)]:
        length = 0
        for new_start, new_end in zip([START_ARROW_POS] + seq, seq):
            length += get_len(new_start, new_end, iteration - 1)
        shortest = min(shortest, length)
    return shortest

def get_min_len(sequence, iterations):
    arrows = get_arrows_for_numbers(sequence)
    shortest = 1e12
    for seq in arrows:
        length = 0
        # Zipping allows to prepend 'A' to the start sequence
        # start => [A, 1, 2]
        # end => [1, 2]
        # zip(start, end) = [(A, 1), (1, 2)]
        for start, end in zip([START_ARROW_POS] + seq, seq):
            length += get_len(start, end, iterations)
        shortest = min(shortest, length)
    return shortest

# Part 1
aoc.mark_task_start()
result1 = 0
for sequence in sequences:
    best = get_min_len(sequence, 2)
    result1 += best * int(sequence.replace('A', ''))
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = 0
for sequence in sequences:
    best = get_min_len(sequence, 25)
    result2 += best * int(sequence.replace('A', ''))
aoc.print_result(2, result2, exp2)
