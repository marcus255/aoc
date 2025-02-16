#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 yyyy_dd"
    exit 1
fi

# Extract the argument
TASK_NAME=$1

# Validate the argument format (yyyy_dd)
if [[ ! "$TASK_NAME" =~ ^[0-9]{4}_[0-9]{2}$ ]]; then
    echo "Error: Argument must be in the format yyyy_dd, where y and d are single digits."
    exit 1
fi

# Define the source template file and the destination file
TEMPLATE_FILE="2024/src/cpp_task.template"
DEST_FILE="2024/src/task_${TASK_NAME}.cpp"

# Check if the template file exists
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "Template file $TEMPLATE_FILE does not exist."
    exit 1
fi

# Check if the destination file already exists
if [ -f "$DEST_FILE" ]; then
    echo "Destination file $DEST_FILE already exists. Aborting to prevent overwriting."
    exit 1
fi

# Copy the template file to the destination file
cp "$TEMPLATE_FILE" "$DEST_FILE"

# Check if the copy was successful
if [ $? -eq 0 ]; then
    # Replace <TASK_YEAR_DATE> with the actual task name in the destination file
    sed -i "s/<TASK_YEAR_DATE>/${TASK_NAME}/g" "$DEST_FILE"
    echo "Task file created: $DEST_FILE"
else
    echo "Failed to create task file."
    exit 1
fi

# Define the tasklist file
TASKLIST_FILE="2024/inc/tasklist.h"

# Insert the new task name above the "/* <NEXT_TASK_MARKER> */" line
sed -i "/\/\* <NEXT_TASK_MARKER> \*\//i \    X(${TASK_NAME}) \\\\" "$TASKLIST_FILE"

# Check if the insertion was successful
if [ $? -eq 0 ]; then
    echo "Task name added to 2024/inc/tasklist.h"
else
    echo "Failed to add task name to 2024/inc/tasklist.h"
    exit 1
fi

# Run cmake after adding new cpp file
echo "Running cmake..."
cmake .

# Check if cmake was successful
if [ $? -eq 0 ]; then
    echo "CMake configuration successful."
else
    echo "CMake configuration failed."
    exit 1
fi