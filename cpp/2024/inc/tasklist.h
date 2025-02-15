#pragma once

#include "../../framework/inc/aoc_task.h"

#define GENERATE_TASK_CLASS(YEAR_DAY) \
namespace Day_##YEAR_DAY { \
class Task : public AocTask { \
public: \
    Task(); \
    std::string partOneSolution(const std::vector<std::string>& input) override; \
    std::string partTwoSolution(const std::vector<std::string>& input) override; \
}; \
}

GENERATE_TASK_CLASS(2024_01)
GENERATE_TASK_CLASS(2024_02)
GENERATE_TASK_CLASS(2024_03)