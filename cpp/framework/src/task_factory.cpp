#include "../inc/task_factory.h"
#include "../../2024/inc/tasklist.h"

// Macro to generate task map entries
#define REGISTER_TASK(YEAR_DAY) \
    {#YEAR_DAY, []() -> std::unique_ptr<AocTask> { \
        return std::make_unique<Task_##YEAR_DAY>(); \
    }}

// Map of task names to task creators
std::unordered_map<std::string, TaskFactory::TaskCreator> TaskFactory::taskMap = {
    #define X(YEAR_DAY) REGISTER_TASK(YEAR_DAY),
    TASK_NAMES
    #undef X
};

std::unique_ptr<AocTask> TaskFactory::createTask(const std::string& taskName) {
    auto it = taskMap.find(taskName);
    if (it == taskMap.end()) {
        throw std::runtime_error("Task not defined: " + taskName);
    }
    return it->second();
}