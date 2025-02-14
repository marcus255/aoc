#pragma once

#include "aoc_task.h"

#include <memory>
#include <string>
#include <unordered_map>

class TaskFactory {
public:
    using TaskCreator = std::unique_ptr<AocTask>(*)();

    static std::unique_ptr<AocTask> createTask(const std::string& taskName);

private:
    static std::unordered_map<std::string, TaskCreator> taskMap;
};