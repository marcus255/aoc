import os
import sys
import importlib.util

def import_task(file_path):
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)

dir = '.'
files = [f for f in os.listdir(dir) if f.startswith('task_') and f.endswith('.py')]
files.sort()
last_module = '/'.join([dir, files[-1]])

mode = 'task'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    mode = 'test'

print('\n' + '='*80)
label = f'Running {last_module} in {mode} mode'
space = (80-len(label)-4) * ' '
print(f'| {label} {space}|')
print('='*80)
import_task(last_module)
print('='*80 + '\n')
