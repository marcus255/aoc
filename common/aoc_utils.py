from math import sqrt

def rotated_2d(array, rotate_left=True, mutable=True):
    rotated = list(zip(*array))[::-1] if rotate_left else list(zip(*array[::-1]))
    return [list(line) for line in rotated] if mutable else rotated

def rotated_2d_left(array):
    return rotated_2d(array, rotate_left=True)

def rotated_2d_right(array):
    return rotated_2d(array, rotate_left=False)

def translated_2d(array, mutable=True):
    translated = list(zip(*array))
    return [list(line) for line in translated] if mutable else translated

def polygon_area(vertices):
    # Shoelace formula
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def find_factors(n):
    factors = [1]
    for i in range(2, int(sqrt(n) + 2)):
        if n % i == 0:
            if i not in factors:
                factors.append(i)
                if n // i not in factors:
                    factors.append(n // i)
    return sorted(factors)

def join_ranges(ranges):
    joined = []
    ranges.sort()
    for low, high in ranges:
        if not joined or joined[-1][1] < low - 1:
            joined.append((low, high))
        else:
            joined[-1] = (joined[-1][0], max(joined[-1][1], high))
    return joined
