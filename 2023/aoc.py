import os
import sys
import re
import time

start_time = 0

class ColorPrint:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    debug = False

    @staticmethod
    def inf(s):
        return f'{ColorPrint.YELLOW}{s}{ColorPrint.END}'

    @staticmethod
    def err(s):
        return f'{ColorPrint.RED}{s}{ColorPrint.END}'

    @staticmethod
    def ok(s):
        return f'{ColorPrint.GREEN}{s}{ColorPrint.END}'

def is_test_mode():
    return len(sys.argv) == 2 and sys.argv[1] == 'test'

def get_test_vector_name(file_path):
    _, filename = os.path.split(os.path.normpath(file_path))
    p = re.compile('.*(\d{2}).*')
    m = p.match(filename)
    if not m:
        raise RuntimeError(f'Unable to extract day number from filename: {filename}')
    aoc_day = m.group(1)
    test_vector = f'input_{aoc_day}.txt'
    if is_test_mode():
        test_vector = f'test_{aoc_day}.txt'
    return test_vector

def get_lines(file_path):
    with open(get_test_vector_name(file_path), 'r') as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

def get_content(file_path, strip=True):
    with open(get_test_vector_name(file_path), 'r') as f:
        content = f.read()
    return content.strip() if strip else content

def mark_task_start():
    global start_time
    start_time = time.time()

def print_result(part, result, exp=None, year=2023):
    status, error = '', ''
    ok = (exp == result)
    time_spent_ms = (time.time() - start_time) * 1000
    exec_time = f'{time_spent_ms:4.0f} ms' if start_time else 'N/A'
    task_number = sys.argv[0].split(".")[0].split('_')[1]
    name = f'[ {exec_time} ] [ {year}-{task_number}-{part} ]'
    if is_test_mode():
        status = ColorPrint.ok('[ PASS ] ') if ok else ColorPrint.err('[ FAIL ] ')
        error = '' if ok else ColorPrint.err(f' <= Expected: {exp}')
        msg = f'{status}{name}: {result} {error}'
    else:
        msg = f'{name}: {ColorPrint.inf(result)}'
    print(msg)
