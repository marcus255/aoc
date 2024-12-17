import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1, 1

# Common
programs_registers = []
registers = {}
programs = []
instr_pointer = 0

for line in lines:
    program = []
    if 'Register' in line:
        reg = line.split()[1]
        k, v = line.split('Register ')[1].split(': ')
        registers[k] = int(v)
    if 'Program' in line:
        program = line.split()[1].split(',')
        programs.append(program)
        program = []
        programs_registers.append(registers)
        registers = {}

def adv(x):
    registers['A'] = registers['A'] // 2**x
def bxl(x):
    registers['B'] = registers['B'] ^ x
def bst(x):
    registers['B'] = x % 8
def jnz(x):
    if registers['A'] != 0:
        global instr_pointer
        instr_pointer = x - 2
def bxc(x):
    registers['B'] = registers['B'] ^ registers['C']
def out(x):
    output.append(x % 8)
def bdv(x):
    registers['B'] = registers['A'] // 2**x
def cdv(x):
    registers['C'] = registers['A'] // 2**x

instructions = {
    '0': lambda x: adv(x),
    '1': lambda x: bxl(x),
    '2': lambda x: bst(x),
    '3': lambda x: jnz(x),
    '4': lambda x: bxc(x),
    '5': lambda x: out(x),
    '6': lambda x: bdv(x),
    '7': lambda x: cdv(x),
}
combo_operands = {
    '4': lambda: registers['A'],
    '5': lambda: registers['B'],
    '6': lambda: registers['C'],
}

# Part 1
results1 = [
    (0, 0, 0, '4,6,3,5,6,3,5,2,1,0'),
    (0, 1, 9, ''),
    (10, 0, 0, '0,1,2'),
    (0, 0, 0, '4,2,5,6,7,7,7,7,3,1,0'),
    (0, 26, 0, ''),
    (0, 44354, 43690, '')
]
for i, program in enumerate(programs):
    aoc.mark_task_start()
    output = []
    instr_pointer = 0
    registers = programs_registers[i]
    while instr_pointer < len(program) - 1:
        instr = program[instr_pointer]
        operand = program[instr_pointer+1]
        orig_operand = operand
        if instr not in ['1', '3'] and 7 > int(operand) >= 4:
            operand = combo_operands[operand]()
        instructions[instr](int(operand))
        instr_pointer += 2
    result = (registers['A'], registers['B'], registers['C'], ','.join(map(str, output)))
    aoc.print_result(1, result, results1[i])

# Part 2
aoc.mark_task_start()

aoc.print_result(2, result2, exp2)
