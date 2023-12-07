import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 6440, 5905

card_strengths = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cards_weights =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

# 7. Five of a kind, where all five cards have the same label: AAAAA
def is_7(cards):
    return len(set(cards)) == 1

# 6. Four of a kind, where four cards have the same label and one card has a different label: AA8AA
def is_6(cards):
    if len(set(cards)) != 2:
        return False
    first = cards[0]
    f_count, s_count = 0, 0
    for card in cards:
        if card == first:
            f_count += 1
        else:
            s_count += 1
    return True if (f_count == 1 or s_count == 1) else False

# 5. Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
def is_5(cards):
    if len(set(cards)) != 2:
        return False
    first = cards[0]
    f_count, s_count = 0, 0
    for card in cards:
        if card == first:
            f_count += 1
        else:
            s_count += 1

    return True if (f_count == 2 or s_count == 2) else False

# 4. Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
def is_4(cards):
    if len(set(cards)) != 3:
        return False
    for card in cards:
        if cards.count(card) == 3:
            return True
    return False

# 3. Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
def is_3(cards):
    if len(set(cards)) != 3:
        return False
    pairs = 0
    for card in cards:
        if cards.count(card) == 2:
            pairs += 1
    return pairs == 4

# 2. One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
def is_2(cards):
    if len(set(cards)) != 4:
        return False
    for card in cards:
        if cards.count(card) == 2:
            return True
    return False

# 1. High card, where all cards' labels are distinct: 23456
def is_1(cards):
    return len(set(cards)) == 5

def get_score(cards):
    score = 0
    if is_7(cards):
        score = 7
    elif is_6(cards):
        score = 6
    elif is_5(cards):
        score = 5
    elif is_4(cards):
        score = 4
    elif is_3(cards):
        score = 3
    elif is_2(cards):
        score = 2
    elif is_1(cards):
        score = 1
    return score

results = []
for line in lines:
    cards, bid = line.split(' ')
    score = get_score(cards)

    weight_str = ''
    for c in cards:
        weight_str += cards_weights[card_strengths.index(c)]
    results.append((score, bid, weight_str))

# sort by score, then by weight_str
results.sort(key=lambda x: (x[0], x[2]))

result1 = 0
for i, (score, bid, _) in enumerate(results):
    result1 += ((i+1) * int(bid))

aoc.print_result(1, result1, exp1)

#Part 2
card_strengths_2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
all = card_strengths_2[1:]

# prepare possible replacement strings for 'J', 'JJ', ..., 'JJJJJ' combinations
reps = [[] for _ in range(5)]
for c1 in all:
    reps[0].append(c1)
    for c2 in all:
        reps[1].append(c1+c2)
        for c3 in all:
            reps[2].append(c1+c2+c3)
            for c4 in all:
                reps[3].append(c1+c2+c3+c4)
                for c5 in all:
                    reps[4].append(c1+c2+c3+c4+c5)

results = []
for line in lines:
    cards, bid = line.split(' ')
    best_cards = cards
    score = get_score(cards)
    sorted_cards = ''.join(sorted(cards))

    for i, replacements in enumerate(reps):
        js = 'J' * (i+1)
        occurences = sorted_cards.count('J')
        if (i+1) > occurences:
            break
        for r in replacements:
            tmp_cards = sorted_cards.replace(js, r, 1)
            tmp_score = get_score(tmp_cards)
            if tmp_score > score:
                score = tmp_score
                for c in r:
                    best_cards = cards.replace('J', c, 1)

    weight_str = [cards_weights[card_strengths_2.index(c)] for c in best_cards]
    weight_str_orig = [cards_weights[card_strengths_2.index(c)] for c in cards]
    results.append((score, weight_str_orig, weight_str, bid, cards, best_cards))

# sort by score, then by weight_str_orig, then by weight_str
results.sort(key=lambda x: (x[0], x[1], x[2]))

result2 = 0
for i, (score, _, _, bid, orig_cards, best_cards) in enumerate(results):
    # print(f'{i+1}: {orig_cards} -> {best_cards}, score: {score} bid: {bid}')
    result2 += ((i+1) * int(bid))

aoc.print_result(2, result2, exp2)
