import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 13, 30

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# Part 1
aoc.mark_task_start()
total_score = 0
matches_per_card = []
for line in lines:
    line = line.split(': ')[1]
    [winning_nums, numbers] = line.split(' | ')
    winning_nums = winning_nums.split(' ')
    numbers = numbers.split(' ')
    winning_nums = list(filter(lambda num: len(num), winning_nums))
    numbers = list(filter(lambda num: len(num), numbers))

    win_count = len(winning_nums)
    count = len(numbers)
    total_count = win_count + count

    sum = set(winning_nums + numbers)
    match_count = total_count - len(sum)

    score = 2**(match_count - 1)
    if total_count == len(sum):
        score = 0
    # print(match_count, score)
    matches_per_card.append([match_count])
    total_score += score

result1 = total_score
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
total_cards = 0
for i, matches in enumerate(matches_per_card):
    total_cards += 1
    # print(f'Card {i+1}: {matches}')
    for c in matches:
        for j in range(matches[0]):
            try:
                matches_per_card[i+j+1].append(matches_per_card[i+j+1][0])
                # print(f'adding {i+j+1+1}')
                total_cards += 1
            except IndexError:
                pass

result2 = total_cards
aoc.print_result(2, result2, exp2)