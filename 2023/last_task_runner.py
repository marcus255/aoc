import os
import sys
import importlib

files = [f for f in os.listdir() if f.startswith('task_') and f.endswith('.py')]
files.sort()
last_module = files[-1][:-3]

mode = 'task'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
        mode = 'test'

print('\n' + '='*80)
label = f'Running {last_module} in {mode} mode'
space = (80-len(label)-4) * ' '
print(f'| {label} {space}|')
print('='*80)
task = importlib.import_module(last_module)
print('='*80 + '\n')