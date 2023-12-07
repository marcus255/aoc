with open('input_06.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

times = [53, 83, 72, 88]
distances = [333, 1635, 1289, 1532]

def get_better_scores(time, record):
    better_scores = 0
    for t in range(1, time + 1):
        d = (time - t) * t
        if d > record:
            better_scores += 1
    return better_scores

total = 1
for i in range(len(times)):
    total *= get_better_scores(times[i], distances[i])
print(total)

# Part 2
time = 53837288
distance = 333163512891532

print(get_better_scores(time, distance))
