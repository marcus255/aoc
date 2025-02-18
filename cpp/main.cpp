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
            auto task = TaskFactory::createTask(taskName);
            if (!task) {
                continue;
            }
            tasks.push_back(std::move(task));
        } catch (const std::runtime_error& e) {
            // TODO: Change to warning message visible in verbose mode
            std::cerr << "Error creating task '" << taskName << "': " << e.what() << std::endl;
            continue; // Skip this task and continue with the next one
        }
    }

    return tasks;
}

auto generateTaskNames(const std::string& year) {
    std::vector<std::string> taskNames;
    for (int i = 1; i <= 25; ++i) {
        std::stringstream ss;
        ss << year << "_" << std::setw(2) << std::setfill('0') << i;
        taskNames.push_back(ss.str());
    }
    return taskNames;
}

int main(int argc, char* argv[]) {
    bool runAll = false;
    bool runLast = false;
    std::string singleTask;
    std::string year = "2024";

    parseArguments(argc, argv, runAll, runLast, singleTask, year);
    bool single = !singleTask.empty();

    if ((runAll && runLast) || (runAll && single) || (runLast && single)) {
        showHelp(argv[0]);
        return 1;
    }

    auto taskNames = !singleTask.empty() ? std::vector<std::string>{singleTask} : generateTaskNames(year);
    auto tasksToRun = createTasks(taskNames);

    if (tasksToRun.empty()) {
        std::cerr << "No tasks for year " << year << " found" << std::endl;
        return 1;
    }

    if (runLast) {
        auto lastTask = std::move(tasksToRun.back());
        tasksToRun.clear();
        tasksToRun.push_back(std::move(lastTask));
    }

    for (auto& task : tasksToRun) {
        task->run();
    }

    return 0;
}