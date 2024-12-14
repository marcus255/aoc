 #!/bin/bash

if [ $# -ne 2 ]
  then
    echo "Usage: $0 <year> <task number>"
    exit 1
fi

set -e

YEAR=$1
TASK=$2
BASEDIR=$(pwd)

pushd $YEAR
TASK_FILE="task_$TASK.py"
TEST_FILE="test_$TASK.txt"
INPUT_FILE="input_$TASK.txt"

echo "Generating files for task $TASK in directory $YEAR:"
echo "$TASK_FILE, $TEST_FILE, $INPUT_FILE"

cp $BASEDIR/common/template_task.py $TASK_FILE
dos2unix $TASK_FILE

echo "\n" > $TEST_FILE
dos2unix $TEST_FILE

echo "\n" >  $INPUT_FILE
dos2unix $INPUT_FILE

echo "Files generated"