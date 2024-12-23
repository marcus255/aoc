import aoc
from itertools import product

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 7, 'co,de,ka,ta'

# Common
computers = [x.split('-') for x in lines]

def find_pcs(pc):
    pcs = []
    pcs.extend([b for a, b in computers if a == pc])
    pcs.extend([a for a, b in computers if b == pc])
    return pcs

def find_all_pc_sets(pc, required, pc_sets):
    pc_set = tuple(sorted(required))
    if pc_set in pc_sets:
        return
    pc_sets.add(pc_set)
    for connected_pc in connections[pc]:
        if connected_pc in required:
            continue
        # Check if all elements of 'required' are in 'connections[connected_pc]'
        if not required <= connections[connected_pc]:
            continue
        # Add 'connected_pc' to 'required' and search further
        find_all_pc_sets(connected_pc, required | {connected_pc}, pc_sets)

# Part 1
aoc.mark_task_start()
triplets = set()
for a, b in computers:
    a_pcs = find_pcs(a)
    b_pcs = find_pcs(b)
    for pca, pcb in product(a_pcs, b_pcs):
        if pca == pcb and any([a[0] == 't', b[0] == 't', pca[0] == 't']):
            triplets.add(tuple(sorted((a, b, pca))))
result1 = len(triplets)
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
connections = {}
for a, b in computers:
    connections[a] = connections.get(a, set()) | {b}
    connections[b] = connections.get(b, set()) | {a}
pc_sets = set()
for c in connections:
    find_all_pc_sets(c, {c}, pc_sets)
largest_set = max(pc_sets, key=len)
result2 = ','.join(sorted(largest_set))
aoc.print_result(2, result2, exp2)
