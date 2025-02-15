#include "../inc/task_factory.h"
#include "../inc/aoc_task.h"
#include "../../2024/inc/tasklist.h"

std::unordered_map<std::string, TaskFactory::TaskCreator> TaskFactory::taskMap = {
    {"2024_01", []() -> std::unique_ptr<AocTask> { return std::make_unique<Day_2024_01::Task>(); }},
    {"2024_02", []() -> std::unique_ptr<AocTask> { return std::make_unique<Day_2024_02::Task>(); }},
    {"2024_03", []() -> std::unique_ptr<AocTask> { return std::make_unique<Day_2024_03::Task>(); }},
};

std::unique_ptr<AocTask> TaskFactory::createTask(const std::string& taskName) {
    auto it = taskMap.find(taskName);
    if (it == taskMap.end()) {
        throw std::runtime_error("Task not defined: " + taskName);
    }
    return it->second();
}