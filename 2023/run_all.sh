 #!/bin/bash

echo "Test runs"
for i in {01..25}; do
    ls task_$i.py >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        python task_$i.py test;
    fi
    done

echo "Task runs"
for i in {01..25}; do
    ls task_$i.py >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        python task_$i.py;
    fi
    done