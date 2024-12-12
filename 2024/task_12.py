import aoc
from itertools import product

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1930, 1206

# Common
def is_cell_adjacent(cell, other_cells):
    i, j = cell
    for ii, jj in other_cells:
        if (abs(i - ii) == 1 and j == jj) or (abs(j - jj) == 1 and i == ii):
            return True
    return False

def is_regions_adjacent(region1, region2):
    for cell in region1:
        if is_cell_adjacent(cell, region2):
            return True
    return False

def get_perimeter(cells):
    # First get the sum of perimiters of all cells
    # Then subtract 1 for each adjacent cell
    # For any two adjacent cells, the subtraction is done twice
    perimeter = 4 * len(cells)
    for i, j in cells:
        for ii, jj in cells:
            if (abs(i - ii) == 1 and j == jj) or (abs(j - jj) == 1 and i == ii):
                perimeter -= 1
    return perimeter

def merge_regions(regions):
    regions_changed = True
    while regions_changed:
        regions_changed = False
        for plant1, cells1 in regions:
            for plant2, cells2 in regions:
                if plant1 != plant2 or cells1 == cells2:
                    continue
                if is_regions_adjacent(cells1, cells2):
                    cells1 += cells2
                    regions.remove((plant2, cells2))
                    regions_changed = True

# Functions for Part 2
def get_adjacent_cells(cell, other_cells):
    i, j = cell
    horizontal, vertical = [], []
    for ii, jj in other_cells:
        if (abs(i - ii) == 1 and j == jj):
            horizontal.append(((i, ii), None))
        if (abs(j - jj) == 1 and i == ii):
            vertical.append((None, (j, jj)))
    return horizontal, vertical

def get_all_adjacent_cells(region1, region2):
    horizontal, vertical = {}, {}
    for cell in region1:
        hh, vv = get_adjacent_cells(cell, region2)
        for h in hh:
            horizontal.setdefault(h[0], []).append(cell[1])
        for v in vv:
            vertical.setdefault(v[1], []).append(cell[0])
    return horizontal, vertical

# Part 1
aoc.mark_task_start()
grid = [list(line) for line in lines]
regions = []
for i, j in product(range(len(grid)), range(len(grid[0]))):
    plant = grid[i][j]
    region_found = False
    for index, (region_plant, region_cells) in enumerate(regions):
        if region_plant == plant and is_cell_adjacent((i, j), region_cells):
            regions[index][1].append((i, j))
            region_found = True
            break
    if not region_found:
        regions.append((plant, [(i, j)]))
merge_regions(regions)
result1 = sum([len(cells) * get_perimeter(cells) for _, cells in regions])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
# get grid coordinates + 1 cell padding to allow regions to be adjacent to the border
grid_coords = [(i, j) for i in range(-1, len(grid) + 1) for j in range(-1, len(grid[0]) + 1)]
for plant, cells in regions:
    c = set(cells)
    other = set(grid_coords) - c
    hh, vv = get_all_adjacent_cells(c, other)
    h_edges = [sorted(x) for x in hh.values()]
    v_edges = [sorted(x) for x in vv.values()]

    # Now, split non-continuous edges into multiple continuous edges
    cont_edges = ([], [])
    for i, edges in enumerate([h_edges, v_edges]):
        for edge in edges:
            cont_edge = []
            for coord in edge:
                if len(cont_edge) == 0 or coord - cont_edge[-1] == 1:
                    cont_edge.append(coord)
                else:
                    cont_edges[i].append(cont_edge)
                    cont_edge = [coord]
            cont_edges[i].append(cont_edge)
    cont_h_edges, cont_v_edges = cont_edges
    result2 += len(cells) * (len(cont_h_edges) + len(cont_v_edges))

aoc.print_result(2, result2, exp2)
