#pragma once

#include "../../framework/inc/aoc_task.h"

// List of task names
#define TASK_NAMES \
    X(2024_01) \
    X(2024_02) \
    X(2024_03) \
    /* <NEXT_TASK_MARKER> */
    // Do not change the marker comment, it is used by the task generator

// Macro to generate task class declarations
#define X(YEAR_DAY) \
namespace Task_##YEAR_DAY { \
    class Task : public AocTask { \
    public: \
        Task(); \
        std::string partOneSolution(const std::vector<std::string>& input) override; \
        std::string partTwoSolution(const std::vector<std::string>& input) override; \
    }; \
}
TASK_NAMES
#undef X
