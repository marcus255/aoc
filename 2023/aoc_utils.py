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