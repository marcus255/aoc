import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 3, 1623178306

# Common
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def print_nodes():
    cur_node = nodes[0]
    for _ in range(len(nodes)):
        print(cur_node.value, end=' ')
        cur_node = cur_node.next
    print()

def init_nodes(numbers):
    nodes = [Node(num) for num in numbers]
    for i in range(len(numbers)):
        nodes[i].next = nodes[(i+1) % len(numbers)]
        nodes[i].prev = nodes[(i-1) % len(numbers)]
    return nodes

def run_decryption(nodes):
    # Cycle lenght is one less than the number of nodes, since we are removing the node we are moving
    cycle_len = len(nodes) - 1
    for node in nodes:
        if node.value == 0:
            # No action for node with value 0, but stash its reference
            node_0 = node
            continue
        # If the move is to the left, convert it to the right, given we know the length of the cycle
        value = (node.value) if node.value > 0 else (cycle_len + node.value)
        # Save some work if we travel more than one cycle
        value %= cycle_len
        other = node
        for _ in range(value):
            other = other.next
        if other == node:
            continue
        # Stitch the place we removed the node from
        node.next.prev = node.prev
        node.prev.next = node.next
        # Stitch the new node in to the right of the other node
        other.next.prev = node
        node.next = other.next
        other.next = node
        node.prev = other
    return node_0

# Part 1
numbers = list(map(int, lines))
aoc.mark_task_start()
nodes = init_nodes(numbers)
node = run_decryption(nodes)
for _ in range(3):
    for _ in range(1000):
        node = node.next
    result1 += node.value
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
MULTIPLIER = 811589153
numbers = [num * MULTIPLIER for num in numbers]
nodes = init_nodes(numbers)
for _ in range(10):
    node = run_decryption(nodes)
for _ in range(3):
    for _ in range(1000):
        node = node.next
    result2 += node.value
aoc.print_result(2, result2, exp2)
