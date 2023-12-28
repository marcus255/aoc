import aoc
import sympy

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 2, 47

# Common
X, Y = 0, 1

'''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''
vectors = []
for line in lines:
    xyz, dxdydz = line.split(' @ ')
    x, y, z = xyz.split(', ')
    dx, dy, dz = dxdydz.split(', ')
    x, y, z = int(x), int(y), int(z)
    dx, dy, dz = int(dx), int(dy), int(dz)
    vectors.append(((x, y, z), (x + dx, y + dy, z + dz), (dx, dy, dz)))

def intersection(A, B, C, D):
    # Line AB represented as a1x + b1y = c1
    a1, b1= B[Y] - A[Y], A[X] - B[X]
    c1 = a1 * A[X] + b1 * A[Y]
    # Line CD represented as a2x + b2y = c2
    a2, b2 = D[Y] - C[Y], C[X] - D[X]
    c2 = a2 * C[X] + b2 * C[Y]
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    x = (b2*c1 - b1*c2)/determinant
    y = (a1*c2 - a2*c1)/determinant
    # print(f'{A},{B} {C}{D} intersect at {x,y}')
    return (x, y)

def is_in_past(v, p):
    v1x, v1y, v1dx, v1dy = v[0][X], v[0][Y], v[2][X], v[2][Y]
    if v1dx < 0 and p[X] > v1x or v1dx > 0 and p[X] < v1x:
        # print(f'Intersect X in past: {v[0]} {v[0]}')
        return True
    if v1dy < 0 and p[Y] > v1y or v1dy > 0 and p[Y] < v1y:
        # print(f'Intersect Y in past: {v[0]} {v[0]}')
        return True
    return False

# Part 1
aoc.mark_task_start()
collides = 0
MIN, MAX = 200000000000000, 400000000000000
t1, t2 = (7, 27) if aoc.is_test_mode() else (MIN, MAX)
for i, v1 in enumerate(vectors):
    for v2 in vectors[i+1:]:
        p = intersection(v1[0], v1[1], v2[0], v2[1])
        if p and t1 <= p[X] <= t2 and t1 <= p[Y] <= t2:
            v1x, v1y, v1dx, v1dy = v1[0][X], v1[0][Y], v1[2][X], v1[2][Y]
            if is_in_past(v1, p) or is_in_past(v2, p):
                continue
            # print(f'{v1} {v2} intersect at ({p[X]:.2f}, {p[Y]:.2f})')

            collides += 1
        
result1 = collides
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
x, y, z, dx, dy, dz = sympy.symbols("x, y, z, dx, dy, dz")
equations = []
for (xi, yi, zi), _, (dxi, dyi, dzi) in vectors:
    equations.append((dx - dxi) * (yi - y) - (xi - x) * (dy - dyi))
    equations.append((dy - dyi) * (zi - z) - (yi - y) * (dz - dzi))
    solutions = []
    for solution in sympy.solve(equations):
        if all(s % 1 == 0 for s in solution.values()) and len(solution) == 6:
            solutions.append(solution)
    if len(solutions) == 1:
        sl = solutions[0]
        result2 = solutions[0][x] + solutions[0][y] + solutions[0][z]
        break

aoc.print_result(2, result2, exp2)
