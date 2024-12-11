import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1, 1

# Common
input_stones = list(map(int, lines[0].split()))

def transform_stone(stone):
    if stone == 0:
        return (1, None)
    num_digits = len(str(stone))
    if num_digits % 2 == 0:
        return ((stone // (10 ** (num_digits // 2))), stone % (10 ** (num_digits // 2)))
    else:
        return (stone * 2024, None)

# Part 1
aoc.mark_task_start()
blinks = 25
stones = input_stones[:]
for i in range(blinks):
    new_stones = []
    for stone in stones:
        new_stones += list(filter(lambda x: x is not None, transform_stone(stone)))
    stones = new_stones

result1 = len(stones)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
blinks = 75
stones = {stone: 1 for stone in input_stones}
for i in range(blinks):
    new_stones = {}
    for stone, count in stones.items():
        s1, s2 = transform_stone(stone)

        new_stones[s1] = (new_stones[s1] + count) if s1 in new_stones else count
        if s2 is not None:
            new_stones[s2] = (new_stones[s2] + count) if s2 in new_stones else count
    stones = new_stones

result2 = sum(stones.values())
aoc.print_result(2, result2, exp2)
