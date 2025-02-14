#include "framework/inc/aoc_task.h"
#include "framework/inc/task_factory.h"
#include "framework/inc/argument_parser.h"
#include <memory>
#include <vector>
#include <string>
#include <iostream>

void runTasks(const std::vector<std::string>& taskNames) {
    std::vector<std::unique_ptr<AocTask>> tasks;

    for (const auto& taskName : taskNames) {
        tasks.push_back(TaskFactory::createTask(taskName));
    }

    for (auto& task : tasks) {
        task->run();
    }
}

int main(int argc, char* argv[]) {
    std::vector<std::string> taskNames;
    bool runAll = false;
    bool runLast = false;
    std::string singleTask;

    parseArguments(argc, argv, runAll, runLast, singleTask);

    // TODO: parse task names from tasklist.h or directory, sort alphabetically
    std::vector<std::string> allTaskNames = {"2024_01", "2024_02"};
    if (runAll) {
        taskNames = allTaskNames;
    } else if (runLast) {
        taskNames = {allTaskNames.back()};
    } else if (!singleTask.empty()) {
        taskNames = {singleTask};
    } else {
        showHelp(argv[0]);
        return 1;
    }

    runTasks(taskNames);

    return 0;
}