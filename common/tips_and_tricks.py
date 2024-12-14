import pdb
import sys

# Generators - to save memory. They are lazy-initialized
normal_list = [i for i in range(10**6)]
generator = (i for i in range(10**6))
print(f'{sum(normal_list)}, {sum(generator)}')
print(f'List size: {sys.getsizeof(normal_list)} B, generator size: {sys.getsizeof(generator)} B')

# Counting objects using Counters
from collections import Counter
numbers = [9,11,33,5,7,8,6,2,4,33,11,33,11,9,9,9,9]
counter = Counter(numbers)
print(f'\nCounter object, sorted by default: {counter}')
print(f'Number of "11" occurrences in the list: {counter[11]}')
# Returns a list of tuples that match: [(item1, count1), (item2, count2), ...]
# Size of the list corresponds to the argument passed to function most_common()
most_1, most_2 = counter.most_common(2)
print(f'1st most common: {most_1[0]}, total {most_1[1]} times')
# There are 2 values that are 2nd most common, lower will be returned
print(f'2nd most common: {most_2[0]}, total {most_2[1]} times')

# Merging dictionaries
d1 = { 'a': 1, 'b': 2 }
d2 = { 'a': 5, 'c': 10 }
merged_dict = { **d1, **d2 }
# second dict values will overwrite existing values from first dict
print(f'\nMerged dictionary using "{{**d1, **d2}}":\t{merged_dict}')
# using python 3.9 operators
merged_dict = d1 | d2
print(f'Merged dictionary using "d1 | d2":\t{merged_dict}')
d1 |= d2
print(f'Merged dictionary using "d1 |= d2":\t{d1}')


# map function
some_list = [5, 6, 7, 8, 9]
cubes = list(map(lambda x: x**3, some_list))
print(f'\n{some_list} ==cube==> {cubes}')
# Converting to other type
cubes_str = map(str, cubes)
print(f'List of int converted to list of strings {"-".join(cubes_str)}')

# all() and any()
list1 = [1, 2, 3, 4]
list2 = [0, 1, 0, 0]
list3 = [0, 0, 0, 0]
print(f'\nAll non-zero in {list1}?: {all(list1)}')
print(f'All non-zero in {list2}?: {all(list2)}')
print(f'ANY non-zero in {list2}?: {any(list2)}')
print(f'ANY non-zero in {list3}?: {all(list3)}')

# zip function - zipping
names = ['Arc', 'Boa', 'Cin']
numbers = [1, 2, 3, 4, 5, 6]
chars = ['X', 'Y', 'Z', 'A']
zipped = list(zip(names, numbers, chars))
print(f'\nZipped object: {zipped}')
# Size matches size of smallest input array
# 'strict=True' can be used to raise an error if sizes don't match
print(f'Zipped object size: {len(zipped)}')
n, num, ch = zipped[0]
print(f'Zipped object first elem: {n}-{num}-{ch}')

# zip function - unzipping
name_ages = [('Mike', 20), ('Jane', 21), ('Kate', 23)]
names, ages = zip(*name_ages)
print(f'Unzipped names: {", ".join(list(names))}, unzipped ages: {ages}')

# zip function - creating dict
name_age_dict = dict(zip(names, ages))
print(f'Dict from lists: {name_age_dict}')

# zip with enumerate in loop
print(f'\nZip with enumerate:')
for i, (name, age) in enumerate(zip(names, ages)):
    print(f'{i}: {name}={age}')

# Do not use default mutable arguments, use None instead
def append_bad(n, l=[]):
    l.append(n)
    return l
l1 = append_bad(1)
l2 = append_bad(2)
# Every call to the function share the same list!
print(f'\nLists: {l1} {l2}')
def append_ok(n, l=None):
    if l is None:
        l = []
    l.append(n)
    return l
l1 = append_ok(1)
l2 = append_ok(2)
print(f'Lists: {l1} {l2}')




# Python debugging - similar to GDB
# pdb.set_trace()
# for i in range(5):
#     print('inside loop')
# print('loop ended')