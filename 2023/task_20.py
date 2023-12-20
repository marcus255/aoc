import aoc
import math

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 32000000, 1

# Common
modules = {}
conj_modules = []
flipflop_states = {}
bcast_signals = None
for line in lines:
    name, rest = line.split(' -> ')
    receivers = rest.split(', ')

    if name == 'broadcaster':
        bcast_signals = [(name, 0, 'broadcaster') for name in receivers]
    else:
        mod_type, mod_name = name[0], name[1:]
        
        if mod_type == '&':
            conj_modules.append(mod_name)
        elif mod_type == '%':
            flipflop_states[mod_name] = 0

        state = [0]
        connected_mod_pulses = {}
        modules[mod_name] = (mod_type, receivers, state, connected_mod_pulses)

for mod_name, (mod_type, receivers, _, _) in modules.items():
    for r_name in receivers:
        if r_name in conj_modules:
            modules[r_name][3][mod_name] = 0

# Part 1
aoc.mark_task_start()

def are_flipflops_off(modules):
    for mod_type, _, state, _ in modules.values():
        if mod_type == '%' and state[0] == 1:
            return False
    return True

PUSH_COUNT=1000
low_pulses, high_pulses = 0, 0
for step in range(1, PUSH_COUNT+1):
    signals = bcast_signals[:]
    i = 0
    low_pulses += 1

    # print(f'\nStep {step}')
    while signals:
        dest_name, pulse, src_name = signals.pop(0)
        if pulse:
            high_pulses += 1
        else:
            low_pulses += 1
        if dest_name not in modules:
            # print(f'> Module {dest_name} not in modules!')
            continue
        mod_type, receivers, state, connected_mod_pulses = modules[dest_name]
        pulse_to_send = pulse
        # send_msg = ''
        if mod_type == '%':
            if pulse == 0:
                state[0] = 0 if state[0] else 1
                # send_msg = f'  sending {state[0]} to {receivers}'
                pulse_to_send = state[0]
                for r_name in receivers:
                    signals.append((r_name, pulse_to_send, dest_name))
            # else:
                # print(f'flipflop received 1, ignoring')
        elif mod_type == '&':
            connected_mod_pulses[src_name] = pulse_to_send
            pulse_to_send = 1
            if sum(connected_mod_pulses.values()) == len(connected_mod_pulses):
                # print(f'       All sources 1 for {dest_name}: {connected_mod_pulses}')
                pulse_to_send = 0
            # send_msg = f'  sending {pulse_to_send} to {receivers}'
            for r_name in receivers:
                signals.append((r_name, pulse_to_send, dest_name))
        # print(f'{i+1}: {src_name} -> {pulse} -> {mod_type}{dest_name}')
        # print(f'  {send_msg}')

        # print(f'Iteration {i}, signals: {len(signals)}')
        if are_flipflops_off(modules) and not len(signals):
            # print(f'Breaking at {i}, signals: {len(signals)}')
            break
        i += 1

# print(f'{low_pulses}, {high_pulses}')
result1 = low_pulses * high_pulses
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()

dep = ['ln', 'db', 'vq', 'tf']
indexes = {x: [] for x in dep}
PUSH_COUNT=1_000_000_000 if not aoc.is_test_mode() else 0
done = False
for step in range(1, PUSH_COUNT+1):
    signals = bcast_signals[:]

    if done:
        break
    counter = 0
    names = []
    while signals:
        dest_name, pulse, src_name = signals.pop(0)
        if dest_name not in modules:
            if pulse == 0:
                done = True
            continue
        mod_type, receivers, state, connected_mod_pulses = modules[dest_name]
        pulse_to_send = pulse
        if mod_type == '%':
            if pulse == 0:
                state[0] = 0 if state[0] else 1
                pulse_to_send = state[0]
                for r_name in receivers:
                    signals.append((r_name, pulse_to_send, dest_name))
        elif mod_type == '&':
            connected_mod_pulses[src_name] = pulse_to_send
            pulse_to_send = 1
            if sum(connected_mod_pulses.values()) == len(connected_mod_pulses):
                pulse_to_send = 0
            elif dest_name in dep:
                indexes[dest_name].append(step)
            for r_name in receivers:
                signals.append((r_name, pulse_to_send, dest_name))

                
    if len([None for x in indexes.values() if len(x) > 1]) == 4:
        distances = [x[1] - x[0] for x in indexes.values()]
        result2 = math.lcm(*distances)
        break

result1 = low_pulses * high_pulses

aoc.print_result(2, result2, exp2)
