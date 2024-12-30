import aoc
from collections import Counter
from collections import deque

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 64, 58

# Common
lava_cells = []
for line in lines:
    lava_cells.append(tuple(map(int, line.split(','))))

def create_faces(x, y, z):
    faces = [[] for _ in range(6)]
    # Use binary numbers 000-111 to get all 8 vertices
    for i in range(0b111 + 1):
        zi = i & 1
        yi = (i >> 1) & 1
        xi = (i >> 2) & 1
        vertex = (x + xi, y + yi, z + zi)
        faces[0 if zi else 1].append(vertex)
        faces[2 if yi else 3].append(vertex)
        faces[4 if xi else 5].append(vertex)
    return [tuple(w) for w in faces]

# Part 1
aoc.mark_task_start()
all_faces = []
for x, y, z in lava_cells:
    faces = create_faces(x, y, z)
    all_faces.extend(faces)
occurrences = list(Counter(all_faces).values())
oc_counter = Counter(occurrences)
# Get the number of faces that are used exactly once
result1 =  oc_counter[1]
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
counter = Counter(all_faces)
faces_counts = counter.most_common()
outter_faces = [face for face, count in faces_counts if count == 1]

# First, get the bounding box that will fit all the lava cells + 1 cell margin
xs, ys, zs = zip(*lava_cells)
maxx, maxy, maxz = max(xs) + 1, max(ys) + 1, max(zs) + 1
minx, miny, minz = min(xs) - 1, min(ys) - 1, min(zs) - 1

# Use path finding to get all air cells. Treat lava cells as walls
DIRS = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
queue = deque([(minx, miny, minz)])
air_cells = {(minx, miny, minz)}
while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in DIRS:
        nx, ny, nz = x + dx, y + dy, z + dz
        if nx < minx or nx > maxx or ny < miny or ny > maxy or nz < minz or nz > maxz:
            continue
        if (nx, ny, nz) in air_cells:
            continue
        if (nx, ny, nz) in lava_cells:
            continue
        air_cells.add((nx, ny, nz))
        queue.append((nx, ny, nz))

air_faces = set()
for x, y, z in air_cells:
    air_faces.update(create_faces(x, y, z))

# Count the number of faces that are both in air_faces and outter_faces
result2 = len(air_faces & set(outter_faces))
aoc.print_result(2, result2, exp2)
