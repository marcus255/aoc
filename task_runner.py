import os
import sys
import argparse
import importlib.util

# Add "common" directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'common'))

def import_task(file_path):
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)

def find_last_year(dir):
    files = [d for d in os.listdir(dir) if all([os.path.isdir(d), d.startswith('20') and len(d) == 4])]
    return sorted(files)[-1]

def main(mode, year, task):
    dir = year if year else find_last_year(os.path.dirname(__file__))
    files = [f for f in os.listdir(dir) if f.startswith('task_') and f.endswith('.py')]
    task_script = f'task_{task}.py' if task else sorted(files)[-1]
    task_path = os.path.join(dir, task_script)

    print('\n' + '='*80)
    label = f'Running {task_path} in {mode} mode'
    space = (80-len(label)-4) * ' '
    print(f'| {label} {space}|')
    print('='*80)
    import_task(task_path)
    print('='*80 + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the last task file')
    parser.add_argument('mode', choices=['task', 'test'], nargs='?', default='task', help='Run in task or test mode')
    parser.add_argument('--year', type=str, required=False, help='Year of the task')
    parser.add_argument('--task', type=str, required=False, help='Task number')
    args = parser.parse_args()
    main(args.mode, args.year, args.task)
