import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = None, 117440

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

instructions = {
    '0': lambda x: registers.update({'A': registers['A'] // 2**x}),
    '1': lambda x: registers.update({'B': registers['B'] ^ x}),
    '2': lambda x: registers.update({'B': x % 8}),
    '3': lambda x: (globals().update({'instr_pointer': x - 2}) if registers['A'] != 0 else None),
    '4': lambda x: registers.update({'B': registers['B'] ^ registers['C']}),
    '5': lambda x: output.append(x % 8),
    '6': lambda x: registers.update({'B': registers['A'] // 2**x}),
    '7': lambda x: registers.update({'C': registers['A'] // 2**x}),
}
combo_operands = {
    '4': lambda: registers['A'],
    '5': lambda: registers['B'],
    '6': lambda: registers['C'],
}

def run(program):
    global output
    global instr_pointer
    output = []
    instr_pointer = 0
    while instr_pointer < len(program) - 1:
        instr = program[instr_pointer]
        operand = program[instr_pointer+1]
        if instr not in ['1', '3'] and 7 > int(operand) >= 4:
            operand = combo_operands[operand]()
        instructions[instr](int(operand))
        instr_pointer += 2
    return ','.join(map(str, output))

def run2(program, instr_index, match, result):
    if instr_index < 0:
        result.append(match)
        return True
    for bit_mask in range(8):
        reg_a, instr_pointer = match << 3 | bit_mask, 0
        while instr_pointer < len(program) - 1:
            instr = int(program[instr_pointer])
            operand = int(program[instr_pointer+1])

            # Define operations in place, globals make looping harder
            if operand <= 3: op = operand
            elif operand == 4: op = reg_a
            elif operand == 5: op = reg_b
            elif operand == 6: op = reg_c

            if   instr == 0: reg_a //= 2**op
            elif instr == 1: reg_b ^= operand
            elif instr == 2: reg_b = op & 7
            elif instr == 3: instr_pointer = operand - 2 if reg_a != 0 else instr_pointer
            elif instr == 4: reg_b ^= reg_c
            elif instr == 5: output_char = op & 7; break
            elif instr == 6: reg_b = reg_a // 2**op
            elif instr == 7: reg_c = reg_a // 2**op
            instr_pointer += 2
        if output_char == int(program[instr_index]) and run2(program, instr_index - 1, match << 3 | bit_mask, result):
            return True
    return False

# Part 1
results1 = [
    (0, 0, 0, '5,7,3,0') ,
    (0, 0, 0, '4,6,3,5,6,3,5,2,1,0'),
    (0, 1, 9, ''),
    (10, 0, 0, '0,1,2'),
    (0, 0, 0, '4,2,5,6,7,7,7,7,3,1,0'),
    (0, 26, 0, ''),
    (0, 44354, 43690, '')
]
for i, program in enumerate(programs):
    aoc.mark_task_start()
    registers = programs_registers[i]
    output_str = run(program)
    result = (registers['A'], registers['B'], registers['C'], output_str)
    aoc.print_result(1, result, results1[i])

# Part 2
aoc.mark_task_start()
program = programs[0]
registers = programs_registers[0]
result = []
run2(program, len(program) - 1, 0, result)
result2 = result[0]
aoc.print_result(2, result2, exp2)
