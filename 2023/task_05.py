import multiprocessing as mp
import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 35, 46

names = [
    'seed-to-soil', 
    'soil-to-fertilizer', 
    'fertilizer-to-water', 
    'water-to-light', 
    'light-to-temperature', 
    'temperature-to-humidity', 
    'humidity-to-location'
]
maps = {}
seeds = []
current_map = ''

for line in lines:
    if line == '':
        continue
    if 'seeds' in line:
        seeds = [int(x) for x in line.split(' ')[1:]]
        continue
    if 'map' in line:
        current_map = line.split(' map:')[0]
        continue
    if current_map not in maps:
        maps[current_map] = []
    dst_src_len = [int(x) for x in line.split(' ')]
    maps[current_map].append(dst_src_len)

def get_dst_num(map_name, src_num):
    for mapping in maps[map_name]:
        dst, src, length = mapping
        if src <= src_num < src + length:
            return dst + (src_num - src)
    return src_num

# Part 1
aoc.mark_task_start()
dst_numbers = []
for seed in seeds:
    dst_num = seed
    for name in names:
        dst_num = get_dst_num(name, dst_num)
    dst_numbers.append(dst_num)

result1 = min(dst_numbers)
aoc.print_result(1, result1, exp1)

global_mins = {}

# Part 2
def find_min(i):
    # print(f'Line {i}, num = {seeds[2*i+1]}, start = {seeds[2*i]}')
    min_location = 1000000000
    seed = seeds[2*i]
    num_seeds = seeds[2*i+1]

    start, end = 0, num_seeds
    for j in range(start, end, 1):
        dst_num = seed + j
        for name in names:
            dst_num = get_dst_num(name, dst_num)
        if dst_num < min_location:
            min_location = dst_num
        # if i == 7 and not j % (1024*1024):
        #     print(f'Progress: {(j*100)/end:.1f}%')
    # print(f'Global Min {min_location} at [{i}, {j}]')
    global_mins[i] = min_location

if __name__ == '__main__':
    aoc.mark_task_start()
    # threads = []
    # for i in range(len(seeds) // 2):
    #     thread = mp.Process(target=find_min, args=(i,))
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()
    print(f'Task skipped')    
    aoc.print_result(2, result2, exp2)