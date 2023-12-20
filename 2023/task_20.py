import sys
import aoc
import math

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 32000000, 1

# Common
modules = {}
conj_modules = []
bcast_signals = None
LOW, HIGH = 0, 1

# Parse modules
for line in lines:
    name, rest = line.split(' -> ')
    receivers = rest.split(', ')

    if name == 'broadcaster':
        bcast_signals = [(name, 0, 'broadcaster') for name in receivers]
    else:
        mod_type, mod_name = name[0], name[1:]

        if mod_type == '&':
            conj_modules.append(mod_name)

        # use one element list as state, so it can be mutated inside this tuple
        state, src_mod_pulses = [], {}
        modules[mod_name] = (mod_type, receivers, [LOW], src_mod_pulses)

# Initialize conjunction modules' souces to LOW
for mod_name, (mod_type, receivers, _, _) in modules.items():
    for r_name in receivers:
        if r_name in conj_modules:
            modules[r_name][3][mod_name] = LOW

def flipflops_off(modules):
    for mod_type, _, state, _ in modules.values():
        if mod_type == '%' and state[0] == HIGH:
            return False
    return True

def process_button_push(modules, signals, sources=None, step_markers=None, step=None):
    low_pulses, high_pulses = 0, 0
    while signals:
        dest_name, pulse, src_name = signals.pop(0)
        if pulse == HIGH:
            high_pulses += 1
        else:
            low_pulses += 1
        if dest_name not in modules:
            continue
        mod_type, receivers, state, src_mod_pulses = modules[dest_name]
        pulse_to_send = pulse
        if mod_type == '%' and pulse == LOW:
            state[0] = LOW if state[0] else HIGH
            pulse_to_send = state[0]
            for r_name in receivers:
                signals.append((r_name, pulse_to_send, dest_name))
        elif mod_type == '&':
            src_mod_pulses[src_name] = pulse_to_send
            pulse_to_send = HIGH
            if sum(src_mod_pulses.values()) == len(src_mod_pulses):
                pulse_to_send = LOW
            elif sources and dest_name in sources:
                step_markers[dest_name].append(step)
            for r_name in receivers:
                signals.append((r_name, pulse_to_send, dest_name))
        # print(f'{src_name} -> {pulse} -> {mod_type}{dest_name}')

        if flipflops_off(modules) and not len(signals):
            break
    return low_pulses, high_pulses

# Part 1
aoc.mark_task_start()
PUSH_COUNT=1000
low_pulses, high_pulses = 0, 0
for step in range(1, PUSH_COUNT+1):
    lp, hp = process_button_push(modules, bcast_signals[:])
    low_pulses += lp + 1
    high_pulses += hp
result1 = low_pulses * high_pulses
aoc.print_result(1, result1, exp1)

# Part 2
if aoc.is_test_mode():
    sys.exit(0)

aoc.mark_task_start()
# Find modules, which must all be HIGH in order for 'rx' to get LOW signal
sources = modules['tg'][3].keys()
step_markers = {x: [] for x in sources}
total_steps = 0
step = 1
while True:
    process_button_push(modules, bcast_signals[:], sources, step_markers, step)
    step += 1
    # Get 10 repeats of each source module and make sure they repeat every X steps
    if all([len(x) > 10 for x in step_markers.values()]):
        for markers in step_markers.values():
            diff = markers[1] - markers[0]
            for i in range(1, len(markers)):
                if markers[i] - markers[i - 1] != diff:
                    raise RuntimeError('No pattern in data')
        sequence_lengths = [x[1] - x[0] for x in step_markers.values()]
        total_steps = math.lcm(*sequence_lengths)
        break

result2 = total_steps
aoc.print_result(2, result2, exp2)
