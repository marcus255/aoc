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

def header(func):
    def wrapper(task_path, mode):
        bar = '='*80
        print(f'{bar}')
        label = f'Running {task_path} in {mode} mode'
        print(f'| {label.ljust(len(bar) - 4)} |')
        print(bar)
        func(task_path, mode)
        print()
    return wrapper

@header
def run_task(task_path, mode):
    if len(sys.argv) == 1:
        sys.argv.append('')
    sys.argv[1] = mode
    import_task(task_path)

def main(args):
    dir = args.year if args.year else find_last_year(os.path.dirname(__file__))
    files = [f for f in os.listdir(dir) if f.startswith('task_') and f.endswith('.py')]
    if args.all:
        print(f'Running {args.year} tasks in {args.mode} mode')
        [run_task(os.path.join(dir, f), args.mode) for f in files]
        return

    task_script = f'task_{args.task}.py' if args.task else sorted(files)[-1]
    task_path = os.path.join(dir, task_script)
    run_task(task_path, args.mode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the last task file')
    parser.add_argument('mode', choices=['task', 'test'], nargs='?', default='task', help='Run in task or test mode')
    parser.add_argument('--year', type=str, help='Year of the task')
    parser.add_argument('--task', type=str, help='Task number')
    parser.add_argument('--all', action='store_true', help='Run all tasks')
    args = parser.parse_args()
    main(args)
