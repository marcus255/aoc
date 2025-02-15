#include "framework/inc/aoc_task.h"
#include "framework/inc/task_factory.h"
#include "framework/inc/argument_parser.h"
#include <memory>
#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>


auto createTasks(const std::vector<std::string>& taskNames) {
    std::vector<std::unique_ptr<AocTask>> tasks;

    for (const auto& taskName : taskNames) {
        try {
            tasks.push_back(TaskFactory::createTask(taskName));
        } catch (const std::runtime_error& e) {
            // TODO: Change to warning message visible in verbose mode
            // std::cerr << "Error creating task '" << taskName << "': " << e.what() << std::endl;
            continue; // Skip this task and continue with the next one
        }
    }

    return tasks;
}

int main(int argc, char* argv[]) {
    std::vector<std::string> taskNames;
    bool runAll = false;
    bool runLast = false;
    std::string singleTask;
    std::string year = "2024";

    parseArguments(argc, argv, runAll, runLast, singleTask, year);

    std::vector<std::string> allTaskNames;
    for (int i = 1; i <= 25; ++i) {
        std::stringstream ss;
        ss << year << "_" << std::setw(2) << std::setfill('0') << i;
        allTaskNames.push_back(ss.str());
    }

    auto allTasks = createTasks(allTaskNames);
    decltype(allTasks) tasksToRun;
    if (runAll) {
        tasksToRun = std::move(allTasks);
    } else if (runLast) {
        tasksToRun.push_back(std::move(allTasks.back()));
    } else if (!singleTask.empty()) {
        tasksToRun = createTasks({singleTask});
    } else {
        showHelp(argv[0]);
        return 1;
    }

    if (tasksToRun.empty()) {
        std::cerr << "No tasks for year " << year << " found" << std::endl;
        return 1;
    }

    for (auto& task : tasksToRun) {
        task->run();
    }

    return 0;
}