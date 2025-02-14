#pragma once

// TODO: fix relative paths
#include "../../framework/inc/aoc_task.h"
#include <string>

namespace Day_2024_02 {
class Task : public AocTask {
public:
    Task();

    std::string partOneSolution(const std::vector<std::string>& input) override;
    std::string partTwoSolution(const std::vector<std::string>& input) override;
};
}