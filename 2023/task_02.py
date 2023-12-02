with open('input_02.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

avail_cubes = { 'red': 12, 'green': 13, 'blue': 14 }
possible_games = 0
for i, line in enumerate(lines):
    # Example line:
    # Game 1: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red
    games = line.split(': ')[-1].split('; ')
    possible = True
    for game in games:
        set = game.split(', ')
        for s in set:
            num_color = s.split(' ')
            num = int(num_color[0])
            color = num_color[1]

            if num > avail_cubes[color]:
                possible = False
                break
        if possible == False:
            break
    
    if possible:
        possible_games += (i + 1)

print(f'Sum of possible games: {possible_games}')
        
# Part 2
total_score = 0
for line in lines:
    games = line.split(': ')[-1].split('; ')
    min_set = {'red': 0, 'green': 0, 'blue': 0}
    for game in games:
        set = game.split(', ')
        for s in set:
            num_color = s.split(' ')
            num = int(num_color[0])
            color = num_color[1]
            if num > min_set[color]:
                min_set[color] = num
    
    row_score = min_set['red'] * min_set['green'] * min_set['blue']
    total_score += row_score

print(f'Total score: {total_score}')