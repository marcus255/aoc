 #!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: $0 <task number>"
    exit 1
fi

set -e

TASK_FILE="task_$1.py"
TEST_FILE="test_$1.txt"
INPUT_FILE="input_$1.txt"

echo "Generating files for task $1:"
echo "$TASK_FILE, $TEST_FILE, $INPUT_FILE"

cp template_task.py $TASK_FILE
dos2unix $TASK_FILE

echo "\n" > $TEST_FILE
dos2unix $TEST_FILE

echo "\n" >  $INPUT_FILE
dos2unix $INPUT_FILE

echo "Files generated"