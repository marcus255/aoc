import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 15, 12

# Common
# 1 = A = X = Rock
# 2 = B = Y = Paper
# 3 = C = Z = Scissors
m = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
# results of the rounds, where key is (opponent_choice, our_choice)
# and value is the result: 3 = draw, 6 = win, 0 = lose
results = {
    (1, 2): 6, (2, 3): 6, (3, 1): 6, # win
    (1, 1): 3, (2, 2): 3, (3, 3): 3, # draw
    (1, 3): 0, (2, 1): 0, (3, 2): 0, # lose
}
rounds = [list(map(lambda x: m[x], line.split(' '))) for line in lines]

# Part 1
aoc.mark_task_start()
for left, right in rounds:
    result1 += right + results[(left, right)]
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
weaker = {1: 3, 2: 1, 3: 2}
stronger = {1: 2, 2: 3, 3: 1}
same = {1: 1, 2: 2, 3: 3}
# X = 1 = lose, Y = 2 = draw, Z = 3 = win
mapping = {1: weaker, 2: same, 3: stronger}
for left, result in rounds:
    choice = mapping[result][left]
    result2 += results[(left, choice)] + choice

aoc.print_result(2, result2, exp2)
