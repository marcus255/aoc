import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 'ghjaabcc', 'cqkaabcc'

# Common
letters = 'abcdefghijklmnopqrstuvwxyz'
triplets = list(map(lambda x: ''.join(x), zip(letters, letters[1:], letters[2:])))
doubles = set(zip(letters, letters))
forbidden = set('iol')

def inc_pw(pw):
    pw = list(pw)
    i = len(pw) - 1
    while i >= 0:
        if pw[i] == 'z':
            pw[i] = 'a'
            i -= 1
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break
    return ''.join(pw)

def find_next_pw(pw):
    while True:
        pw = inc_pw(pw)
        # Passwords may not contain the letters i, o, or l
        if any([c in forbidden for c in pw]):
            continue
        # Passwords must include one increasing straight of at least three letters
        if not any([triplet in pw for triplet in triplets]):
            continue
        # Passwords must contain at least two different, non-overlapping pairs of letters
        pw_doubles = set(zip(pw, pw[1:]))
        if len(pw_doubles & doubles) < 2:
            continue
        return pw

# Part 1
aoc.mark_task_start()
result1 = find_next_pw(lines[0])
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = find_next_pw('cqjxxyzz')
aoc.print_result(2, result2, exp2)
