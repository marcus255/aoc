import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 3068, 1514285714288

# Common

# 5 types of rocks. '#' is rock, '.' is empty space. '^' is the origin
#
#   ####   .#.   ..#   #   ##       r c   r c
#   ^      ###   ..#   #   ##      (1,0) (1,1)
#          .#.   ###   #   ^       (0,0) (0,1)
#          ^     ^     #           ^
#                      ^           origin (row=0, column=0)

rocks = [
    {'h': 1, 'size': 4, 'coords': [(0,0), (0,1), (0,2), (0,3)]},
    {'h': 3, 'size': 5, 'coords': [(0,1), (1,0), (1,1), (1,2), (2,1)]},
    {'h': 3, 'size': 5, 'coords': [(0,0), (0,1), (0,2), (1,2), (2,2)]}, 
    {'h': 4, 'size': 4, 'coords': [(0,0), (1,0), (2,0), (3,0)]}, 
    {'h': 2, 'size': 4, 'coords': [(0,0), (0,1), (1,0), (1,1)]}
]
move_map = {'<': (0, -1), '>': (0, 1), 'v': (-1, 0)}
wind = lines[0]
MOVE_DOWN = (-1, 0)
WIDTH = 7
INIT_HEIGHT = 1
INSERT_COL = 2
SPACE_REQUIRED = 3

def print_chambers(chamber, rock_coords, label='Chambers'):
    print(f'\n{label}')
    for i, level, in enumerate(chamber):
        r = len(chamber) - i - 1
        level = ['@' if ((r, c) in rock_coords) else ('#' if chamber[r][c] == '#' else '.') for c in range(WIDTH)]
        print(f'{"".join(level)}')

def get_top_level_index(chamber):
    for i, level in enumerate(chamber):
        if '#' not in level:
            return i
    return len(chamber) - 1

def add_new_levels(chamber, levels):
    for i in range(levels):
        chamber.append(['.' for _ in range(WIDTH)])

def get_new_level_count(chamber, rock_height):
    space_required = rock_height + SPACE_REQUIRED
    chamber_height = len(chamber)
    rock_top = get_top_level_index(chamber)
    space_avail = chamber_height - rock_top
    return space_required - space_avail

def init_rock_position(position, rock_coords):
    row_offset, col_offset = position
    new_coords = []
    for row, col in rock_coords:
        new_coords.append((row_offset + row, col_offset + col))
    return new_coords

def move_rock(move, rock_coords, chamber):
    move_valid = True
    new_coords = []
    row_move, col_move = move
    for row, col in rock_coords:
        r, c = row + row_move, col + col_move
        new_coords.append((r, c))
        if r < 0 or c < 0 or c >= WIDTH or chamber[r][c] == '#':
            move_valid = False
            break
    return new_coords if move_valid else None

def embedd_rock(chamber, rock_coords):
    for r, c in rock_coords:
        if chamber[r][c] == '#':
            raise RuntimeError(f'Unexpected rock already at position ({r},{c})')
        chamber[r][c] = '#'

def simulate_rockfall(chamber, num_rocks, use_skipping=False):
    no_more_moves = True
    rock_coords = []
    move_counter = 0
    rock_counter = 0
    extra_rows = 0
    pattern = { 'start': 100 if use_skipping else num_rocks, 'len': 20 }

    while rock_counter < num_rocks:
        wind_index = move_counter % len(wind)
        wind_move = wind[wind_index]
        # print(f'Rock {rock_counter+1}, move {move_counter+1}: {wind_move}', len(chamber))
        move_counter += 1
        rock = rocks[rock_counter % len(rocks)]

        if no_more_moves:
            new_levels = get_new_level_count(chamber, rock['h'])
            if new_levels < 0:
                del chamber[new_levels:]
            elif new_levels > 0:
                add_new_levels(chamber, new_levels)

            insert_position = (len(chamber) - rock['h'], INSERT_COL)
            rock_coords = init_rock_position(insert_position, rock['coords'])
            # print_chambers(chamber, rock_coords, 'rock added')
            no_more_moves = False

        new_rock_coords = move_rock(move_map[wind_move], rock_coords, chamber)
        if new_rock_coords:
            rock_coords = new_rock_coords
            # print_chambers(chamber, rock_coords, 'Wind move done')

        new_rock_coords = move_rock(MOVE_DOWN, rock_coords, chamber)
        if new_rock_coords:
            rock_coords = new_rock_coords
            # print_chambers(chamber, rock_coords, 'Down move done')
        else:
            # print_chambers(chamber, rock_coords, 'No down move')
            embedd_rock(chamber, rock_coords)
            rock_coords = []
            # print_chambers(chamber, rock_coords, 'Rock embedded')
            no_more_moves = True

            pattern_len = pattern['len']
            current_wind = (wind + wind)[wind_index-pattern_len:wind_index]
            chamber_top = ''.join(sum(chamber[-pattern_len:], []))
            if rock_counter == pattern['start']:
                pattern['chamber_top'] = chamber_top
                pattern['rock_index'] = rock_counter
                pattern['wind'] = current_wind
                pattern['chamber_height'] = len(chamber)
            elif rock_counter > pattern['start']:
                if current_wind == pattern['wind'] and chamber_top == pattern['chamber_top']:
                    rocks_in_sequence = rock_counter - pattern['rock_index']
                    rows_in_sequence = len(chamber) - pattern['chamber_height']
                    repeat_count = (num_rocks - rock_counter) // rocks_in_sequence
                    rock_counter += repeat_count * rocks_in_sequence
                    extra_rows = rows_in_sequence * repeat_count
                    print(f'Sequence: {rocks_in_sequence} rocks, {rows_in_sequence} rows, {repeat_count} repeats')
                    print(f'Adding {extra_rows} extra rows, skipping to rock {rock_counter}')
                    pattern['start'] = num_rocks
            rock_counter += 1

    return extra_rows

# Part 1
NUM_ROCKS = 2022
chamber = [['.' for _ in range(WIDTH)] for _ in range(INIT_HEIGHT)]
simulate_rockfall(chamber, NUM_ROCKS)
result1 = get_top_level_index(chamber)
# print_chambers(chamber[-10:], [], 'Top')
# print_chambers(chamber[:10], [], 'Bottom')
aoc.print_result(1, result1, exp1)

# Part 2
NUM_ROCKS = 1_000_000_000_000
chamber = [['.' for _ in range(WIDTH)] for _ in range(INIT_HEIGHT)]
extra_rows = simulate_rockfall(chamber, NUM_ROCKS, use_skipping=True)
result2 = extra_rows + get_top_level_index(chamber)
aoc.print_result(2, result2, exp2)
