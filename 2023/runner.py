import os
import importlib

files = [f for f in os.listdir() if f.startswith('task_') and f.endswith('.py')]
files.sort()
last_module = files[-1][:-3]

i = importlib.import_module(last_module)
